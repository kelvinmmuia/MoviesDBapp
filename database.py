# database operations

import sqlite3
import os
from pathlib import Path

# Use SQLite database file
DB_PATH = Path(__file__).parent / 'MovieDatabase.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def execute_query(query, params=None):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            if query.strip().upper().startswith('SELECT'):
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
            conn.commit()
            return True
    except Exception as e:
        print(f"Database error: {e}")
        return None

def get_table_data(table_name):
    """get all data from a table"""
    query = f"SELECT * FROM {table_name}"
    return execute_query(query)

def insert_actor(actor_id, first_name, last_name):
    """insert new actor"""
    query = "INSERT INTO Actor (Actor_id, First_name, Last_name) VALUES (%s, %s, %s)"
    return execute_query(query, (actor_id, first_name, last_name))

def insert_director(director_id, first_name, last_name):
    """insert new director"""
    query = "INSERT INTO Director (Director_id, First_name, Last_name) VALUES (%s, %s, %s)"
    return execute_query(query, (director_id, first_name, last_name))

def insert_genre(genre_id, category):
    """insert new genre"""
    query = "INSERT INTO Genre (Genre_id, Category) VALUES (%s, %s)"
    return execute_query(query, (genre_id, category))

def insert_movie(movie_id, title, release_year):
    """insert new movie"""
    query = "INSERT INTO Movie (Movie_id, Title, Release_year) VALUES (%s, %s, %s)"
    return execute_query(query, (movie_id, title, release_year))

def insert_review(review_id, rating, movie_id):
    """insert new review"""
    query = "INSERT INTO Review (Review_id, Rating, Movie_Movie_id) VALUES (%s, %s, %s)"
    return execute_query(query, (review_id, rating, movie_id))

def insert_user(user_id, email, review_id):
    """insert new user"""
    query = "INSERT INTO User (User_id, email, Review_Review_id) VALUES (%s, %s, %s)"
    return execute_query(query, (user_id, email, review_id))

def insert_acts_in(actor_id, movie_id):
    """insert actor-movie relationship"""
    query = "INSERT INTO Acts_in (Actor_Actor_id, Movie_Movie_id) VALUES (%s, %s)"
    return execute_query(query, (actor_id, movie_id))

def insert_belongs_to(genre_id, movie_id):
    """insert genre-movie relationship"""
    query = "INSERT INTO Belongs_to (Genre_Genre_id, Movie_Movie_id) VALUES (%s, %s)"
    return execute_query(query, (genre_id, movie_id))

def insert_directed_by(movie_id, director_id):
    """insert director-movie relationship"""
    query = "INSERT INTO Directed_by (Movie_Movie_id, Director_Director_id) VALUES (%s, %s)"
    return execute_query(query, (movie_id, director_id))

def search_movies_by_title(title):
    """search movies by title"""
    query = "SELECT * FROM Movie WHERE Title LIKE %s"
    return execute_query(query, (f"%{title}%",))

def search_movies_by_year(year):
    """search movies by release year"""
    query = "SELECT * FROM Movie WHERE Release_year = %s"
    return execute_query(query, (year,))

def search_movies_by_actor(actor_name):
    """search movies by actor name"""
    query = """
    SELECT m.* FROM Movie m
    JOIN Acts_in ai ON m.Movie_id = ai.Movie_Movie_id
    JOIN Actor a ON ai.Actor_Actor_id = a.Actor_id
    WHERE CONCAT(a.First_name, ' ', a.Last_name) LIKE %s
    """
    return execute_query(query, (f"%{actor_name}%",))

def search_movies_by_genre(genre):
    """search movies by genre"""
    query = """
    SELECT m.* FROM Movie m
    JOIN Belongs_to bt ON m.Movie_id = bt.Movie_Movie_id
    JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
    WHERE g.Category LIKE %s
    """
    return execute_query(query, (f"%{genre}%",))

def delete_actor(actor_id):
    """delete actor by id"""
    # First delete related records from junction tables
    query1 = "DELETE FROM Acts_in WHERE Actor_Actor_id = %s"
    execute_query(query1, (actor_id,))
    # Then delete the actor
    query2 = "DELETE FROM Actor WHERE Actor_id = %s"
    return execute_query(query2, (actor_id,))

def delete_director(director_id):
    """delete director by id"""
    # First delete related records from junction tables
    query1 = "DELETE FROM Directed_by WHERE Director_Director_id = %s"
    execute_query(query1, (director_id,))
    # Then delete the director
    query2 = "DELETE FROM Director WHERE Director_id = %s"
    return execute_query(query2, (director_id,))

def delete_genre(genre_id):
    """delete genre by id"""
    # First delete related records from junction tables
    query1 = "DELETE FROM Belongs_to WHERE Genre_Genre_id = %s"
    execute_query(query1, (genre_id,))
    # Then delete the genre
    query2 = "DELETE FROM Genre WHERE Genre_id = %s"
    return execute_query(query2, (genre_id,))

def delete_movie(movie_id):
    """delete movie by id"""
    # First delete related records from junction tables
    query1 = "DELETE FROM Acts_in WHERE Movie_Movie_id = %s"
    execute_query(query1, (movie_id,))
    query2 = "DELETE FROM Belongs_to WHERE Movie_Movie_id = %s"
    execute_query(query2, (movie_id,))
    query3 = "DELETE FROM Directed_by WHERE Movie_Movie_id = %s"
    execute_query(query3, (movie_id,))
    query4 = "DELETE FROM Review WHERE Movie_Movie_id = %s"
    execute_query(query4, (movie_id,))
    # Then delete the movie
    query5 = "DELETE FROM Movie WHERE Movie_id = %s"
    return execute_query(query5, (movie_id,))

def delete_review(review_id):
    """delete review by id"""
    # First delete related records from User table
    query1 = "DELETE FROM User WHERE Review_Review_id = %s"
    execute_query(query1, (review_id,))
    # Then delete the review
    query2 = "DELETE FROM Review WHERE Review_id = %s"
    return execute_query(query2, (review_id,))

def delete_user(user_id):
    """delete user by id"""
    query = "DELETE FROM User WHERE User_id = %s"
    return execute_query(query, (user_id,))

def delete_acts_in(actor_id, movie_id):
    """delete actor-movie relationship"""
    query = "DELETE FROM Acts_in WHERE Actor_Actor_id = %s AND Movie_Movie_id = %s"
    return execute_query(query, (actor_id, movie_id))

def delete_belongs_to(genre_id, movie_id):
    """delete genre-movie relationship"""
    query = "DELETE FROM Belongs_to WHERE Genre_Genre_id = %s AND Movie_Movie_id = %s"
    return execute_query(query, (genre_id, movie_id))

def delete_directed_by(movie_id, director_id):
    """delete director-movie relationship"""
    query = "DELETE FROM Directed_by WHERE Movie_Movie_id = %s AND Director_Director_id = %s"
    return execute_query(query, (movie_id, director_id))

def execute_custom_query(sql_query):
    """execute custom sql query and return dataframe"""
    # basic validation - reject dangerous keywords
    dangerous_keywords = ['DROP', 'DELETE', 'UPDATE', 'INSERT', 'ALTER', 'CREATE', 'TRUNCATE']
    query_upper = sql_query.strip().upper()

    # allow only SELECT queries for safety
    if not query_upper.startswith('SELECT'):
        return None, "Only SELECT queries are allowed for security reasons"

    # check for dangerous keywords
    for keyword in dangerous_keywords:
        if keyword in query_upper:
            return None, f"Query contains forbidden keyword: {keyword}"

    # execute the query
    results = execute_query(sql_query)
    if results is None:
        return None, "Query execution failed"

    if not results:
        return None, "Query returned no results"

    return results, None