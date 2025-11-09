# movie database management system

import streamlit as st
import pandas as pd
import subprocess
import sys
import os
from database import *

def main():
    st.set_page_config(page_title="Movie Database", page_icon=None, layout="wide")
    st.title("Movie Database Management System")

    menu = ["Home", "Add Data", "Delete Data", "Search Movies", "View Data", "SQL Query Tool"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        show_home()
    elif choice == "Add Data":
        show_add_data()
    elif choice == "Delete Data":
        show_delete_data()
    elif choice == "Search Movies":
        show_search_movies()
    elif choice == "View Data":
        show_view_data()
    elif choice == "SQL Query Tool":
        show_sql_query_tool()

def show_home():
    """show home page"""
    st.header("Welcome to Movie Database System")
    st.write("This is a simple movie database management system.")
    st.write("Use the navigation menu to:")
    st.write("- Add new data to tables")
    st.write("- Search for movies")
    st.write("- View existing data")

    # show some basic stats
    col1, col2, col3 = st.columns(3)

    with col1:
        movies = get_table_data("Movie")
        if movies:
            st.metric("Total Movies", len(movies))
        else:
            st.metric("Total Movies", "0")

    with col2:
        actors = get_table_data("Actor")
        if actors:
            st.metric("Total Actors", len(actors))
        else:
            st.metric("Total Actors", "0")

    with col3:
        reviews = get_table_data("Review")
        if reviews:
            avg_rating = sum(r['Rating'] for r in reviews) / len(reviews)
            st.metric("Average Rating", f"{avg_rating:.1f}")
        else:
            st.metric("Average Rating", "0")

def show_generic_add_form(table_name, field_labels, input_types, insert_func, field_types=None):
    """generic form for adding data"""
    st.subheader(f"Add New {table_name}")

    with st.form(f"add_{table_name.lower()}"):
        inputs = []
        field_types = field_types or ["text"] * len(field_labels)

        for i, (label, field_type) in enumerate(zip(field_labels, field_types)):
            if table_name == "Review" and label == "Rating":
                # Special case for Review rating (slider)
                inputs.append(st.slider(label, min_value=1, max_value=100, step=1))
            elif "ID" in label and field_type == "number":
                inputs.append(st.number_input(label, min_value=1, step=1))
            elif field_type == "text":
                inputs.append(st.text_input(label))
            elif field_type == "number":
                inputs.append(st.number_input(label, min_value=1, step=1))
            else:
                inputs.append(st.text_input(label))

        submitted = st.form_submit_button(f"Add {table_name}")

        if submitted:
            if all(inputs):
                if insert_func(*inputs):
                    st.success(f"{table_name} added successfully!")
                else:
                    st.error(f"Failed to add {table_name}. ID might already exist.")
            else:
                st.error("Please fill in all fields")

def show_generic_delete_form(table_name, id_label, delete_func, is_text_id=False):
    """generic form for deleting data"""
    st.subheader(f"Delete {table_name}")

    with st.form(f"delete_{table_name.lower()}"):
        # show existing data for reference
        data = get_table_data(table_name)
        if data:
            st.write(f"Existing {table_name}s:")
            df = pd.DataFrame(data)
            st.dataframe(df)

        if is_text_id:
            record_id = st.text_input(f"{id_label} to Delete")
        else:
            record_id = st.number_input(f"{id_label} to Delete", min_value=1, step=1)

        submitted = st.form_submit_button(f"Delete {table_name}", type="secondary")

        if submitted:
            if record_id:
                if delete_func(record_id):
                    st.success(f"{table_name} with ID {record_id} deleted successfully!")
                    st.rerun()
                else:
                    st.error(f"Failed to delete {table_name}. May not exist or has related records.")
            else:
                st.error(f"Please enter a {id_label}")

def show_add_data():
    """show forms to add data to tables"""
    st.header("Add New Data")

    table = st.selectbox("Select Table", ["Actor", "Director", "Genre", "Movie", "Review", "User", "Acts_in", "Belongs_to", "Directed_by"])

    if table == "Actor":
        show_generic_add_form("Actor", ["Actor ID", "First Name", "Last Name"], "number_input", insert_actor)
    elif table == "Director":
        show_generic_add_form("Director", ["Director ID", "First Name", "Last Name"], "number_input", insert_director)
    elif table == "Genre":
        show_generic_add_form("Genre", ["Genre ID", "Category"], "number_input", insert_genre, ["number", "text"])
    elif table == "Movie":
        show_generic_add_form("Movie", ["Movie ID", "Title", "Release Year"], "number_input", insert_movie, ["number", "text", "number"])
    elif table == "Review":
        show_generic_add_form("Review", ["Review ID", "Rating", "Movie ID"], "number_input", insert_review, ["number", "slider", "number"])
    elif table == "User":
        show_generic_add_form("User", ["User ID", "Email", "Review ID"], "text_input", insert_user, ["text", "text", "number"])
    elif table == "Acts_in":
        show_acts_in_form()
    elif table == "Belongs_to":
        show_belongs_to_form()
    elif table == "Directed_by":
        show_directed_by_form()

def show_delete_data():
    """show forms to delete data from tables"""
    st.header("Delete Data")
    st.warning("Warning: This action cannot be undone. Deleted records will be permanently removed from the database.")

    table = st.selectbox("Select Table", ["Actor", "Director", "Genre", "Movie", "Review", "User", "Acts_in", "Belongs_to", "Directed_by"])

    if table == "Actor":
        show_generic_delete_form("Actor", "Actor ID", delete_actor)
    elif table == "Director":
        show_generic_delete_form("Director", "Director ID", delete_director)
    elif table == "Genre":
        show_generic_delete_form("Genre", "Genre ID", delete_genre)
    elif table == "Movie":
        show_generic_delete_form("Movie", "Movie ID", delete_movie)
    elif table == "Review":
        show_generic_delete_form("Review", "Review ID", delete_review)
    elif table == "User":
        show_generic_delete_form("User", "User ID", delete_user, is_text_id=True)
    elif table == "Acts_in":
        show_delete_acts_in_form()
    elif table == "Belongs_to":
        show_delete_belongs_to_form()
    elif table == "Directed_by":
        show_delete_directed_by_form()


def show_search_movies():
    """search movies functionality"""
    st.header("Search Movies")

    search_option = st.selectbox("Search by:", ["Title", "Year", "Actor", "Genre"])

    if search_option == "Title":
        title = st.text_input("Enter movie title (partial match allowed)")
        if st.button("Search by Title"):
            if title:
                results = search_movies_by_title(title)
                if results:
                    st.subheader(f"Found {len(results)} movies")
                    df = pd.DataFrame(results)
                    st.dataframe(df)
                else:
                    st.info("No movies found with that title")

    elif search_option == "Year":
        year = st.number_input("Enter release year", min_value=1900, max_value=2030, step=1)
        if st.button("Search by Year"):
            results = search_movies_by_year(year)
            if results:
                st.subheader(f"Found {len(results)} movies from {year}")
                df = pd.DataFrame(results)
                st.dataframe(df)
            else:
                st.info(f"No movies found from {year}")

    elif search_option == "Actor":
        actor_name = st.text_input("Enter actor name (partial match allowed)")
        if st.button("Search by Actor"):
            if actor_name:
                results = search_movies_by_actor(actor_name)
                if results:
                    st.subheader(f"Found {len(results)} movies with that actor")
                    df = pd.DataFrame(results)
                    st.dataframe(df)
                else:
                    st.info("No movies found with that actor")

    elif search_option == "Genre":
        genre = st.text_input("Enter genre (partial match allowed)")
        if st.button("Search by Genre"):
            if genre:
                results = search_movies_by_genre(genre)
                if results:
                    st.subheader(f"Found {len(results)} movies in that genre")
                    df = pd.DataFrame(results)
                    st.dataframe(df)
                else:
                    st.info("No movies found in that genre")

def show_view_data():
    """view data from tables"""
    st.header("View Database Tables")

    table = st.selectbox("Select Table to View", ["Actor", "Director", "Genre", "Movie", "Review", "User", "Acts_in", "Belongs_to", "Directed_by"])

    if st.button("Load Data"):
        data = get_table_data(table)
        if data:
            st.subheader(f"{table} Table ({len(data)} records)")
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info(f"No data found in {table} table")

def show_sql_query_tool():
    """sql query tool for custom queries"""
    st.header("SQL Query Tool")
    st.write("Enter any SELECT query to execute. Only SELECT statements are allowed for security.")

    # sample queries for reference
    st.subheader("Sample Queries:")
    st.write("Click on any query to copy it to the query box above:")

    col1, col2 = st.columns(2)

    with col1:
        st.code(
            """SELECT * FROM Movie
WHERE Release_year > 2000;""",
            language="sql"
        )

        st.code(
            """SELECT m.Title, a.First_name, a.Last_name
FROM Movie m
JOIN Acts_in ai ON m.Movie_id = ai.Movie_Movie_id
JOIN Actor a ON ai.Actor_Actor_id = a.Actor_id;""",
            language="sql"
        )

    with col2:
        st.code(
            """SELECT Title, Release_year
FROM Movie
ORDER BY Release_year DESC;""",
            language="sql"
        )

        st.code(
            """SELECT g.Category, COUNT(*) as Movie_Count
FROM Genre g
JOIN Belongs_to bt ON g.Genre_id = bt.Genre_Genre_id
GROUP BY g.Category;""",
            language="sql"
        )

    # query input
    query = st.text_area("Enter your SQL query:", height=150,
                        placeholder="SELECT * FROM Movie WHERE Release_year > 2000;")

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        run_button = st.button("Run Query", type="primary")

    with col2:
        clear_button = st.button("Clear")

    with col3:
        st.write("")  # spacer

    # handle clear button
    if clear_button:
        st.rerun()

    # handle run button
    if run_button:
        if not query.strip():
            st.error("Please enter a SQL query")
        else:
            with st.spinner("Executing query..."):
                from database import execute_custom_query
                results, error = execute_custom_query(query.strip())

                if error:
                    st.error(f"Query Error: {error}")
                elif results:
                    st.success(f"Query executed successfully! Found {len(results)} rows.")

                    # create dataframe and display
                    df = pd.DataFrame(results)

                    # display results
                    st.subheader("Query Results:")
                    st.dataframe(df)
                else:
                    st.info("Query executed but returned no results.")

def show_acts_in_form():
    """form to add actor-movie relationship"""
    st.subheader("Add Actor to Movie")

    with st.form("add_acts_in"):
        # show existing data for reference
        st.write("Existing Actors:")
        actors = get_table_data("Actor")
        if actors:
            actor_df = pd.DataFrame(actors)
            st.dataframe(actor_df)

        st.write("Existing Movies:")
        movies = get_table_data("Movie")
        if movies:
            movie_df = pd.DataFrame(movies)
            st.dataframe(movie_df)

        actor_id = st.number_input("Actor ID", min_value=1, step=1)
        movie_id = st.number_input("Movie ID", min_value=1, step=1)

        submitted = st.form_submit_button("Add Actor to Movie")

        if submitted:
            if insert_acts_in(actor_id, movie_id):
                st.success(f"Actor {actor_id} added to Movie {movie_id} successfully!")
            else:
                st.error("Failed to add relationship. Check if Actor ID and Movie ID exist.")

def show_belongs_to_form():
    """form to add genre-movie relationship"""
    st.subheader("Add Genre to Movie")

    with st.form("add_belongs_to"):
        # show existing data for reference
        st.write("Existing Genres:")
        genres = get_table_data("Genre")
        if genres:
            genre_df = pd.DataFrame(genres)
            st.dataframe(genre_df)

        st.write("Existing Movies:")
        movies = get_table_data("Movie")
        if movies:
            movie_df = pd.DataFrame(movies)
            st.dataframe(movie_df)

        genre_id = st.number_input("Genre ID", min_value=1, step=1)
        movie_id = st.number_input("Movie ID", min_value=1, step=1)

        submitted = st.form_submit_button("Add Genre to Movie")

        if submitted:
            if insert_belongs_to(genre_id, movie_id):
                st.success(f"Genre {genre_id} added to Movie {movie_id} successfully!")
            else:
                st.error("Failed to add relationship. Check if Genre ID and Movie ID exist.")

def show_directed_by_form():
    """form to add director-movie relationship"""
    st.subheader("Add Director to Movie")

    with st.form("add_directed_by"):
        # show existing data for reference
        st.write("Existing Directors:")
        directors = get_table_data("Director")
        if directors:
            director_df = pd.DataFrame(directors)
            st.dataframe(director_df)

        st.write("Existing Movies:")
        movies = get_table_data("Movie")
        if movies:
            movie_df = pd.DataFrame(movies)
            st.dataframe(movie_df)

        movie_id = st.number_input("Movie ID", min_value=1, step=1)
        director_id = st.number_input("Director ID", min_value=1, step=1)

        submitted = st.form_submit_button("Add Director to Movie")

        if submitted:
            if insert_directed_by(movie_id, director_id):
                st.success(f"Director {director_id} added to Movie {movie_id} successfully!")
            else:
                st.error("Failed to add relationship. Check if Director ID and Movie ID exist.")

def show_delete_acts_in_form():
    """form to delete actor-movie relationship"""
    st.subheader("Remove Actor from Movie")

    with st.form("delete_acts_in"):
        # show existing relationships for reference
        st.write("Existing Actor-Movie Relationships:")
        acts_in = get_table_data("Acts_in")
        if acts_in:
            acts_df = pd.DataFrame(acts_in)
            st.dataframe(acts_df)

        actor_id = st.number_input("Actor ID", min_value=1, step=1)
        movie_id = st.number_input("Movie ID", min_value=1, step=1)

        submitted = st.form_submit_button("Remove Actor from Movie", type="secondary")

        if submitted:
            if delete_acts_in(actor_id, movie_id):
                st.success(f"Actor {actor_id} removed from Movie {movie_id} successfully!")
                st.rerun()
            else:
                st.error("Failed to remove relationship. Check if relationship exists.")

def show_delete_belongs_to_form():
    """form to delete genre-movie relationship"""
    st.subheader("Remove Genre from Movie")

    with st.form("delete_belongs_to"):
        # show existing relationships for reference
        st.write("Existing Genre-Movie Relationships:")
        belongs_to = get_table_data("Belongs_to")
        if belongs_to:
            belongs_df = pd.DataFrame(belongs_to)
            st.dataframe(belongs_df)

        genre_id = st.number_input("Genre ID", min_value=1, step=1)
        movie_id = st.number_input("Movie ID", min_value=1, step=1)

        submitted = st.form_submit_button("Remove Genre from Movie", type="secondary")

        if submitted:
            if delete_belongs_to(genre_id, movie_id):
                st.success(f"Genre {genre_id} removed from Movie {movie_id} successfully!")
                st.rerun()
            else:
                st.error("Failed to remove relationship. Check if relationship exists.")

def show_delete_directed_by_form():
    """form to delete director-movie relationship"""
    st.subheader("Remove Director from Movie")

    with st.form("delete_directed_by"):
        # show existing relationships for reference
        st.write("Existing Director-Movie Relationships:")
        directed_by = get_table_data("Directed_by")
        if directed_by:
            directed_df = pd.DataFrame(directed_by)
            st.dataframe(directed_df)

        movie_id = st.number_input("Movie ID", min_value=1, step=1)
        director_id = st.number_input("Director ID", min_value=1, step=1)

        submitted = st.form_submit_button("Remove Director from Movie", type="secondary")

        if submitted:
            if delete_directed_by(movie_id, director_id):
                st.success(f"Director {director_id} removed from Movie {movie_id} successfully!")
                st.rerun()
            else:
                st.error("Failed to remove relationship. Check if relationship exists.")

if __name__ == "__main__":
    main()