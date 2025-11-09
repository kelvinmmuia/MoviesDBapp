# movie database management system

import streamlit as st
import pandas as pd
import subprocess
import sys
import os
import time
from database import *

def main():
    st.set_page_config(
        page_title="Movie Database",
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2962FF;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .welcome-section {
        background: linear-gradient(135deg, #F0F2F6 0%, #FFFFFF 100%);
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #2962FF;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 3px solid #2962FF;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #2962FF;
    }
    .metric-label {
        color: #31333F;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    .sidebar-content {
        padding: 1rem;
    }
    .stButton>button {
        background: linear-gradient(135deg, #2962FF 0%, #1976D2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(41, 98, 255, 0.3);
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        border: 2px solid #F0F2F6;
        border-radius: 5px;
        padding: 0.5rem;
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus, .stSelectbox>div>div>select:focus {
        border-color: #2962FF;
        box-shadow: 0 0 0 2px rgba(41, 98, 255, 0.2);
    }
    .success-message {
        background: #E8F5E8;
        color: #2E7D32;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    .error-message {
        background: #FFEBEE;
        color: #C62828;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #D32F2F;
        margin: 1rem 0;
    }
    .info-message {
        background: #E3F2FD;
        color: #1565C0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2962FF;
        margin: 1rem 0;
    }
    .warning-message {
        background: #FFF3E0;
        color: #E65100;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #FF9800;
        margin: 1rem 0;
    }
    .dataframe-container {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">🎬 Movie Database Management System</h1>', unsafe_allow_html=True)

    # Enhanced sidebar with icons and better styling
    st.sidebar.markdown("""
    <div class="sidebar-content">
        <h3 style="color: #2962FF; margin-bottom: 1rem;">🎬 Navigation</h3>
    </div>
    """, unsafe_allow_html=True)

    menu_options = {
        "🏠 Home": "Home",
        "➕ Add Data": "Add Data",
        "📝 Update Data": "Update Data",
        "🗑️ Delete Data": "Delete Data",
        "🔍 Search Movies": "Search Movies",
        "📊 View Data": "View Data",
        "⚡ SQL Query Tool": "SQL Query Tool"
    }

    choice = st.sidebar.selectbox("Choose an option:", list(menu_options.keys()))
    choice = menu_options[choice]

    if choice == "Home":
        show_home()
    elif choice == "Add Data":
        show_add_data()
    elif choice == "Update Data":
        show_update_data()
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
    st.markdown("""
    <div class="welcome-section">
        <h2 style="color: #2962FF; margin-bottom: 1rem;">Welcome to Movie Database System</h2>
        <p style="font-size: 1.1rem; color: #31333F; margin-bottom: 1.5rem;">
            This is a comprehensive movie database management system built with Streamlit and SQLite.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #2962FF;">
                <strong style="color: #2962FF;">📝 Add Data</strong><br>
                <span style="color: #666;">Insert new movies, actors, directors, and genres</span>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #2962FF;">
                <strong style="color: #2962FF;">🔍 Search</strong><br>
                <span style="color: #666;">Find movies by title, year, actor, or genre</span>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #2962FF;">
                <strong style="color: #2962FF;">📊 View Data</strong><br>
                <span style="color: #666;">Browse all tables and relationships</span>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #2962FF;">
                <strong style="color: #2962FF;">⚡ SQL Queries</strong><br>
                <span style="color: #666;">Run custom SELECT queries</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📈 Database Statistics")

    # show some basic stats with enhanced styling
    col1, col2, col3 = st.columns(3)

    with col1:
        movies = get_table_data("Movie")
        movie_count = len(movies) if movies else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{movie_count}</div>
            <div class="metric-label">Total Movies</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        actors = get_table_data("Actor")
        actor_count = len(actors) if actors else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{actor_count}</div>
            <div class="metric-label">Total Actors</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        reviews = get_table_data("Review")
        if reviews:
            avg_rating = sum(r['Rating'] for r in reviews) / len(reviews)
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{avg_rating:.1f}</div>
                <div class="metric-label">Average Rating</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">0.0</div>
                <div class="metric-label">Average Rating</div>
            </div>
            """, unsafe_allow_html=True)

def show_generic_add_form(table_name, field_labels, input_types, insert_func, field_types=None, placeholders=None):
    """generic form for adding data"""
    st.markdown(f"### ➕ Add New {table_name}")
    st.markdown("---")

    # Define placeholders based on table and field
    if placeholders is None:
        placeholders = {}
        for label in field_labels:
            if "ID" in label:
                placeholders[label] = f"e.g., 12345 (unique {label.lower()})"
            elif "First Name" in label or "Last Name" in label:
                placeholders[label] = f"e.g., John (max 45 chars)"
            elif "Title" in label:
                placeholders[label] = f"e.g., Movie Title (max 45 chars)"
            elif "Email" in label:
                placeholders[label] = f"e.g., user@example.com (max 45 chars)"
            elif "Category" in label:
                placeholders[label] = f"e.g., Action (max 45 chars)"
            elif "Year" in label:
                placeholders[label] = f"e.g., 2024 (1900-2030)"
            elif "Rating" in label:
                placeholders[label] = f"e.g., 85 (1-100)"
            else:
                placeholders[label] = f"Enter {label.lower()}"

    with st.form(f"add_{table_name.lower()}"):
        inputs = []
        field_types = field_types or ["text"] * len(field_labels)

        for i, (label, field_type) in enumerate(zip(field_labels, field_types)):
            placeholder = placeholders.get(label, f"Enter {label.lower()}")

            if table_name == "Review" and label == "Rating":
                # Special case for Review rating (slider)
                inputs.append(st.slider(label, min_value=1, max_value=100, step=1, help="Rate from 1-100"))
            elif "ID" in label and field_type == "number":
                inputs.append(st.number_input(label, min_value=1, step=1, placeholder=placeholder, help=f"Enter unique {label.lower()}"))
            elif field_type == "text":
                inputs.append(st.text_input(label, placeholder=placeholder, help=f"Enter {label.lower()}"))
            elif field_type == "number":
                inputs.append(st.number_input(label, min_value=1, step=1, placeholder=placeholder, help=f"Enter {label.lower()}"))
            else:
                inputs.append(st.text_input(label, placeholder=placeholder, help=f"Enter {label.lower()}"))

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button(f"✅ Add {table_name}", use_container_width=True)

        if submitted:
            if all(str(inp).strip() for inp in inputs if isinstance(inp, str)) and all(inp for inp in inputs if not isinstance(inp, str)):
                result = insert_func(*inputs)
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown(f"""
                        <div class="success-message">
                            ✅ <strong>{table_name} added successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to add {table_name}:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    # Backward compatibility for functions that don't return error messages
                    if result:
                        st.markdown(f"""
                        <div class="success-message">
                            ✅ <strong>{table_name} added successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to add {table_name}.</strong> ID might already exist or database error occurred.
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please fill in all required fields.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_generic_delete_form(table_name, id_label, delete_func, is_text_id=False):
    """generic form for deleting data"""
    st.markdown(f"### 🗑️ Delete {table_name}")
    st.markdown("---")
    st.markdown("""
    <div class="warning-message">
        ⚠️ <strong>Warning:</strong> This action cannot be undone. Deleted records will be permanently removed from the database.
    </div>
    """, unsafe_allow_html=True)

    with st.form(f"delete_{table_name.lower()}"):
        # show existing data for reference
        data = get_table_data(table_name)
        if data:
            st.markdown(f"**📋 Existing {table_name}s:**")
            df = pd.DataFrame(data)
            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="info-message">
                ℹ️ No {table_name.lower()}s found in the database.
            </div>
            """, unsafe_allow_html=True)

        placeholder = f"e.g., 12345 (existing {id_label.lower()})" if not is_text_id else f"e.g., username (existing {id_label.lower()})"

        if is_text_id:
            record_id = st.text_input(f"{id_label} to Delete", placeholder=placeholder, help=f"Enter the {id_label.lower()} of the record to delete")
        else:
            record_id = st.number_input(f"{id_label} to Delete", min_value=1, step=1, placeholder=placeholder, help=f"Enter the {id_label.lower()} of the record to delete")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button(f"🗑️ Delete {table_name}", use_container_width=True)

        if submitted:
            if record_id:
                result = delete_func(record_id)
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown(f"""
                        <div class="success-message">
                            ✅ <strong>{table_name} with ID {record_id} deleted successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)  # Brief pause for user to see success message
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to delete {table_name}:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    # Backward compatibility
                    if result:
                        st.markdown(f"""
                        <div class="success-message">
                            ✅ <strong>{table_name} with ID {record_id} deleted successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)  # Brief pause for user to see success message
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to delete {table_name}.</strong> Record may not exist or has related records.
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="warning-message">
                    ⚠️ <strong>Please enter a valid {id_label}.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_add_data():
    """show forms to add data to tables"""
    st.markdown("## ➕ Add New Data")
    st.markdown("Choose a table below to add new records to your movie database.")

    table_options = {
        "🎭 Actor": "Actor",
        "🎬 Director": "Director",
        "🏷️ Genre": "Genre",
        "🎪 Movie": "Movie",
        "⭐ Review": "Review",
        "👤 User": "User",
        "🔗 Actor-Movie (Acts_in)": "Acts_in",
        "🔗 Genre-Movie (Belongs_to)": "Belongs_to",
        "🔗 Director-Movie (Directed_by)": "Directed_by"
    }

    table_choice = st.selectbox("Select Table to Add Data:", list(table_options.keys()))
    table = table_options[table_choice]

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
    st.markdown("## 🗑️ Delete Data")
    st.markdown("Select a table below to remove records from your movie database.")

    table_options = {
        "🎭 Actor": "Actor",
        "🎬 Director": "Director",
        "🏷️ Genre": "Genre",
        "🎪 Movie": "Movie",
        "⭐ Review": "Review",
        "👤 User": "User",
        "🔗 Actor-Movie (Acts_in)": "Acts_in",
        "🔗 Genre-Movie (Belongs_to)": "Belongs_to",
        "🔗 Director-Movie (Directed_by)": "Directed_by"
    }

    table_choice = st.selectbox("Select Table to Delete From:", list(table_options.keys()))
    table = table_options[table_choice]

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
    st.markdown("## 🔍 Search Movies")
    st.markdown("Find movies in your database using different search criteria.")

    search_options = {
        "📝 Title": "Title",
        "📅 Year": "Year",
        "🎭 Actor": "Actor",
        "🏷️ Genre": "Genre"
    }

    search_option_choice = st.selectbox("Search by:", list(search_options.keys()))
    search_option = search_options[search_option_choice]

    if search_option == "Title":
        col1, col2 = st.columns([3, 1])
        with col1:
            title = st.text_input("Enter movie title (partial match allowed)", help="Type part of the movie title")
        with col2:
            search_title = st.button("🔍 Search by Title", use_container_width=True)

        if search_title:
            if title.strip():
                with st.spinner("Searching movies..."):
                    results = search_movies_by_title(title.strip())
                if results:
                    st.markdown(f"### 🎬 Found {len(results)} movie{'s' if len(results) != 1 else ''}")
                    df = pd.DataFrame(results)
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="info-message">
                        ℹ️ No movies found with that title. Try a different search term.
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ Please enter a movie title to search.
                </div>
                """, unsafe_allow_html=True)

    elif search_option == "Year":
        col1, col2 = st.columns([3, 1])
        with col1:
            year = st.number_input("Enter release year", min_value=1900, max_value=2030, step=1, value=2024, help="Select the release year")
        with col2:
            search_year = st.button("🔍 Search by Year", use_container_width=True)

        if search_year:
            with st.spinner("Searching movies..."):
                results = search_movies_by_year(year)
            if results:
                st.markdown(f"### 🎬 Found {len(results)} movie{'s' if len(results) != 1 else ''} from {year}")
                df = pd.DataFrame(results)
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(df, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="info-message">
                    ℹ️ No movies found from {year}. Try a different year.
                </div>
                """, unsafe_allow_html=True)

    elif search_option == "Actor":
        col1, col2 = st.columns([3, 1])
        with col1:
            actor_name = st.text_input("Enter actor name (partial match allowed)", help="Type part of the actor's name")
        with col2:
            search_actor = st.button("🔍 Search by Actor", use_container_width=True)

        if search_actor:
            if actor_name.strip():
                with st.spinner("Searching movies by actor..."):
                    results = search_movies_by_actor(actor_name.strip())
                if results:
                    st.markdown(f"### 🎬 Found {len(results)} movie{'s' if len(results) != 1 else ''} with '{actor_name}'")
                    df = pd.DataFrame(results)
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="info-message">
                        ℹ️ No movies found with actor '{actor_name}'. Try a different name.
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ Please enter an actor name to search.
                </div>
                """, unsafe_allow_html=True)

    elif search_option == "Genre":
        col1, col2 = st.columns([3, 1])
        with col1:
            genre = st.text_input("Enter genre (partial match allowed)", help="Type part of the genre name")
        with col2:
            search_genre = st.button("🔍 Search by Genre", use_container_width=True)

        if search_genre:
            if genre.strip():
                with st.spinner("Searching movies by genre..."):
                    results = search_movies_by_genre(genre.strip())
                if results:
                    st.markdown(f"### 🎬 Found {len(results)} movie{'s' if len(results) != 1 else ''} in '{genre}' genre")
                    df = pd.DataFrame(results)
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="info-message">
                        ℹ️ No movies found in '{genre}' genre. Try a different genre.
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ Please enter a genre to search.
                </div>
                """, unsafe_allow_html=True)

def show_view_data():
    """view data from tables"""
    st.markdown("## 📊 View Database Tables")
    st.markdown("Select a table below to view all records in your movie database.")

    table_options = {
        "🎭 Actors": "Actor",
        "🎬 Directors": "Director",
        "🏷️ Genres": "Genre",
        "🎪 Movies": "Movie",
        "⭐ Reviews": "Review",
        "👤 Users": "User",
        "🔗 Actor-Movie Links": "Acts_in",
        "🔗 Genre-Movie Links": "Belongs_to",
        "🔗 Director-Movie Links": "Directed_by"
    }

    table_choice = st.selectbox("Select Table to View:", list(table_options.keys()))
    table = table_options[table_choice]

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        load_data = st.button("📊 Load Data", use_container_width=True)

    if load_data:
        with st.spinner(f"Loading {table} data..."):
            data = get_table_data(table)
        if data:
            st.markdown(f"### 📋 {table} Table")
            st.markdown(f"**Total Records:** {len(data)}")
            df = pd.DataFrame(data)
            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Add download button
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"{table.lower()}_data.csv",
                mime="text/csv"
            )
        else:
            st.markdown(f"""
            <div class="info-message">
                ℹ️ No data found in {table} table. Try adding some records first.
            </div>
            """, unsafe_allow_html=True)

def show_sql_query_tool():
    """sql query tool for custom queries"""
    st.markdown("## ⚡ SQL Query Tool")
    st.markdown("Execute custom SELECT queries on your movie database. Only SELECT statements are allowed for security.")
    st.markdown("""
    <div class="info-message">
        ℹ️ <strong>Safe Querying:</strong> Only SELECT statements are permitted. Dangerous operations like DROP, DELETE, UPDATE, INSERT, ALTER, CREATE, and TRUNCATE are blocked.
    </div>
    """, unsafe_allow_html=True)

    # sample queries for reference
    with st.expander("📚 Sample Queries (Click to expand)", expanded=False):
        st.markdown("**Click on any query below to copy it to the query box:**")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**🎬 Movies after 2000:**")
            st.code(
                """SELECT * FROM Movie
WHERE Release_year > 2000;""",
                language="sql"
            )

            st.markdown("**🎭 Movies with Actors:**")
            st.code(
                """SELECT m.Title, a.First_name, a.Last_name
FROM Movie m
JOIN Acts_in ai ON m.Movie_id = ai.Movie_Movie_id
JOIN Actor a ON ai.Actor_Actor_id = a.Actor_id;""",
                language="sql"
            )

        with col2:
            st.markdown("**📅 Movies by Release Year:**")
            st.code(
                """SELECT Title, Release_year
FROM Movie
ORDER BY Release_year DESC;""",
                language="sql"
            )

            st.markdown("**🏷️ Genre Statistics:**")
            st.code(
                """SELECT g.Category, COUNT(*) as Movie_Count
FROM Genre g
JOIN Belongs_to bt ON g.Genre_id = bt.Genre_Genre_id
GROUP BY g.Category;""",
                language="sql"
            )

    # query input
    query = st.text_area("Enter your SQL query:", height=150,
                        placeholder="SELECT * FROM Movie WHERE Release_year > 2000;",
                        help="Enter a SELECT query to execute on the database")

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        run_button = st.button("🚀 Run Query", use_container_width=True)

    with col2:
        clear_button = st.button("🧹 Clear", use_container_width=True)

    with col3:
        st.write("")  # spacer

    # handle clear button
    if clear_button:
        st.rerun()

    # handle run button
    if run_button:
        if not query.strip():
            st.markdown("""
            <div class="warning-message">
                ⚠️ <strong>Please enter a SQL query.</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Executing query..."):
                from database import execute_custom_query
                results, error = execute_custom_query(query.strip())

                if error:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ <strong>Query Error:</strong> {error}
                    </div>
                    """, unsafe_allow_html=True)
                elif results:
                    st.markdown(f"""
                    <div class="success-message">
                        ✅ <strong>Query executed successfully!</strong> Found {len(results)} row{'s' if len(results) != 1 else ''}.
                    </div>
                    """, unsafe_allow_html=True)

                    # create dataframe and display
                    df = pd.DataFrame(results)

                    # display results
                    st.markdown("### 📊 Query Results:")
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Add download button for results
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name="query_results.csv",
                        mime="text/csv"
                    )
                else:
                    st.markdown("""
                    <div class="info-message">
                        ℹ️ <strong>Query executed but returned no results.</strong> Try adjusting your query.
                    </div>
                    """, unsafe_allow_html=True)

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

def show_update_data():
    """show forms to update data in tables"""
    st.markdown("## 📝 Update Data")
    st.markdown("Select a table below to update existing records in your movie database.")

    table_options = {
        "🎭 Actor": "Actor",
        "🎬 Director": "Director",
        "🏷️ Genre": "Genre",
        "🎪 Movie": "Movie",
        "⭐ Review": "Review",
        "👤 User": "User"
    }

    table_choice = st.selectbox("Select Table to Update:", list(table_options.keys()))
    table = table_options[table_choice]

    if table == "Actor":
        show_update_actor_form()
    elif table == "Director":
        show_update_director_form()
    elif table == "Genre":
        show_update_genre_form()
    elif table == "Movie":
        show_update_movie_form()
    elif table == "Review":
        show_update_review_form()
    elif table == "User":
        show_update_user_form()

def show_update_actor_form():
    """form to update actor"""
    st.markdown("### 📝 Update Actor")
    st.markdown("---")

    # Get existing actors for selection
    actors = get_table_data("Actor")
    if not actors:
        st.markdown("""
        <div class="info-message">
            ℹ️ No actors found in the database. Add some actors first.
        </div>
        """, unsafe_allow_html=True)
        return

    actor_options = {f"{a['First_name']} {a['Last_name']} (ID: {a['Actor_id']})": a['Actor_id'] for a in actors}
    selected_actor = st.selectbox("Select Actor to Update:", list(actor_options.keys()))
    actor_id = actor_options[selected_actor]

    # Get current actor data
    current_actor = next((a for a in actors if a['Actor_id'] == actor_id), None)
    if not current_actor:
        st.error("Actor not found.")
        return

    with st.form(f"update_actor_{actor_id}"):
        st.markdown("**Current Values:**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"First Name: {current_actor['First_name']}")
        with col2:
            st.info(f"Last Name: {current_actor['Last_name']}")

        st.markdown("**New Values:**")
        new_first_name = st.text_input("First Name", value=current_actor['First_name'], placeholder="e.g., John (max 45 chars)", help="Enter the actor's first name")
        new_last_name = st.text_input("Last Name", value=current_actor['Last_name'], placeholder="e.g., Doe (max 45 chars)", help="Enter the actor's last name")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update Actor", use_container_width=True)

        if submitted:
            if new_first_name.strip() and new_last_name.strip():
                result = update_actor(actor_id, new_first_name.strip(), new_last_name.strip())
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>Actor updated successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to update actor:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Actor updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please fill in both first name and last name.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_update_director_form():
    """form to update director"""
    st.markdown("### 📝 Update Director")
    st.markdown("---")

    directors = get_table_data("Director")
    if not directors:
        st.markdown("""
        <div class="info-message">
            ℹ️ No directors found in the database. Add some directors first.
        </div>
        """, unsafe_allow_html=True)
        return

    director_options = {f"{d['First_name']} {d['Last_name']} (ID: {d['Director_id']})": d['Director_id'] for d in directors}
    selected_director = st.selectbox("Select Director to Update:", list(director_options.keys()))
    director_id = director_options[selected_director]

    current_director = next((d for d in directors if d['Director_id'] == director_id), None)
    if not current_director:
        st.error("Director not found.")
        return

    with st.form(f"update_director_{director_id}"):
        st.markdown("**Current Values:**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"First Name: {current_director['First_name']}")
        with col2:
            st.info(f"Last Name: {current_director['Last_name']}")

        st.markdown("**New Values:**")
        new_first_name = st.text_input("First Name", value=current_director['First_name'], placeholder="e.g., Christopher (max 45 chars)", help="Enter the director's first name")
        new_last_name = st.text_input("Last Name", value=current_director['Last_name'], placeholder="e.g., Nolan (max 45 chars)", help="Enter the director's last name")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update Director", use_container_width=True)

        if submitted:
            if new_first_name.strip() and new_last_name.strip():
                result = update_director(director_id, new_first_name.strip(), new_last_name.strip())
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>Director updated successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to update director:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Director updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please fill in both first name and last name.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_update_genre_form():
    """form to update genre"""
    st.markdown("### 📝 Update Genre")
    st.markdown("---")

    genres = get_table_data("Genre")
    if not genres:
        st.markdown("""
        <div class="info-message">
            ℹ️ No genres found in the database. Add some genres first.
        </div>
        """, unsafe_allow_html=True)
        return

    genre_options = {f"{g['Category']} (ID: {g['Genre_id']})": g['Genre_id'] for g in genres}
    selected_genre = st.selectbox("Select Genre to Update:", list(genre_options.keys()))
    genre_id = genre_options[selected_genre]

    current_genre = next((g for g in genres if g['Genre_id'] == genre_id), None)
    if not current_genre:
        st.error("Genre not found.")
        return

    with st.form(f"update_genre_{genre_id}"):
        st.markdown("**Current Value:**")
        st.info(f"Category: {current_genre['Category']}")

        st.markdown("**New Value:**")
        new_category = st.text_input("Category", value=current_genre['Category'], placeholder="e.g., Science Fiction (max 45 chars)", help="Enter the genre category")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update Genre", use_container_width=True)

        if submitted:
            if new_category.strip():
                result = update_genre(genre_id, new_category.strip())
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>Genre updated successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to update genre:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Genre updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please enter a category.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_update_movie_form():
    """form to update movie"""
    st.markdown("### 📝 Update Movie")
    st.markdown("---")

    movies = get_table_data("Movie")
    if not movies:
        st.markdown("""
        <div class="info-message">
            ℹ️ No movies found in the database. Add some movies first.
        </div>
        """, unsafe_allow_html=True)
        return

    movie_options = {f"{m['Title']} ({m['Release_year']}) (ID: {m['Movie_id']})": m['Movie_id'] for m in movies}
    selected_movie = st.selectbox("Select Movie to Update:", list(movie_options.keys()))
    movie_id = movie_options[selected_movie]

    current_movie = next((m for m in movies if m['Movie_id'] == movie_id), None)
    if not current_movie:
        st.error("Movie not found.")
        return

    with st.form(f"update_movie_{movie_id}"):
        st.markdown("**Current Values:**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"Title: {current_movie['Title']}")
        with col2:
            st.info(f"Release Year: {current_movie['Release_year']}")

        st.markdown("**New Values:**")
        new_title = st.text_input("Title", value=current_movie['Title'], placeholder="e.g., Inception (max 45 chars)", help="Enter the movie title")
        new_year = st.number_input("Release Year", value=current_movie['Release_year'], min_value=1900, max_value=2030, step=1, placeholder="e.g., 2010 (1900-2030)", help="Enter the release year")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update Movie", use_container_width=True)

        if submitted:
            if new_title.strip():
                result = update_movie(movie_id, new_title.strip(), new_year)
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>Movie updated successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to update movie:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Movie updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please enter a title.</strong>
                </div>
                """, unsafe_allow_html=True)

def show_update_review_form():
    """form to update review"""
    st.markdown("### 📝 Update Review")
    st.markdown("---")

    reviews = get_table_data("Review")
    if not reviews:
        st.markdown("""
        <div class="info-message">
            ℹ️ No reviews found in the database. Add some reviews first.
        </div>
        """, unsafe_allow_html=True)
        return

    # Get movie titles for better display
    movies = get_table_data("Movie")
    movie_dict = {m['Movie_id']: m['Title'] for m in movies} if movies else {}

    review_options = {f"Review ID {r['Review_id']} - Movie: {movie_dict.get(r['Movie_Movie_id'], f'ID {r['Movie_Movie_id']}')} - Rating: {r['Rating']}": r['Review_id'] for r in reviews}
    selected_review = st.selectbox("Select Review to Update:", list(review_options.keys()))
    review_id = review_options[selected_review]

    current_review = next((r for r in reviews if r['Review_id'] == review_id), None)
    if not current_review:
        st.error("Review not found.")
        return

    with st.form(f"update_review_{review_id}"):
        st.markdown("**Current Values:**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"Rating: {current_review['Rating']}")
        with col2:
            st.info(f"Movie ID: {current_review['Movie_Movie_id']}")

        st.markdown("**New Values:**")
        new_rating = st.slider("Rating", min_value=1, max_value=100, value=current_review['Rating'], step=1, help="Rate from 1-100")
        new_movie_id = st.number_input("Movie ID", value=current_review['Movie_Movie_id'], min_value=1, step=1, placeholder="e.g., 12345 (existing movie ID)", help="Enter the movie ID")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update Review", use_container_width=True)

        if submitted:
            result = update_review(review_id, new_rating, new_movie_id)
            if isinstance(result, tuple):
                success, error_msg = result
                if success:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Review updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ <strong>Failed to update review:</strong> {error_msg}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="success-message">
                    ✅ <strong>Review updated successfully!</strong>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
                time.sleep(1)
                st.rerun()

def show_update_user_form():
    """form to update user"""
    st.markdown("### 📝 Update User")
    st.markdown("---")

    users = get_table_data("User")
    if not users:
        st.markdown("""
        <div class="info-message">
            ℹ️ No users found in the database. Add some users first.
        </div>
        """, unsafe_allow_html=True)
        return

    user_options = {f"{u['User_id']} - {u['email']}": u['User_id'] for u in users}
    selected_user = st.selectbox("Select User to Update:", list(user_options.keys()))
    user_id = selected_user.split(' - ')[0]  # Extract user_id from the display string

    current_user = next((u for u in users if u['User_id'] == user_id), None)
    if not current_user:
        st.error("User not found.")
        return

    with st.form(f"update_user_{user_id}"):
        st.markdown("**Current Values:**")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"User ID: {current_user['User_id']}")
        with col2:
            st.info(f"Email: {current_user['email']}")

        st.markdown("**New Values:**")
        new_email = st.text_input("Email", value=current_user['email'], placeholder="e.g., newemail@example.com (max 45 chars)", help="Enter the user's email address")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("✅ Update User", use_container_width=True)

        if submitted:
            if new_email.strip():
                result = update_user(user_id, new_email.strip())
                if isinstance(result, tuple):
                    success, error_msg = result
                    if success:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>User updated successfully!</strong>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ <strong>Failed to update user:</strong> {error_msg}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>User updated successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            else:
                st.markdown("""
                <div class="warning-message">
                    ⚠️ <strong>Please enter an email address.</strong>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()