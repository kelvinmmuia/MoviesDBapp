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
            return True, None
    except Exception as e:
        print(f"Database error: {e}")
        return False, str(e)

def get_table_data(table_name):
    """get all data from a table"""
    query = f"SELECT * FROM {table_name}"
    return execute_query(query)

def insert_actor(actor_id, first_name, last_name):
    """insert new actor"""
    # Validate inputs
    try:
        actor_id = int(actor_id)
        if actor_id <= 0:
            return False, "Actor ID must be a positive integer"
        if not first_name.strip() or not last_name.strip():
            return False, "First name and last name cannot be empty"
        if len(first_name.strip()) > 45 or len(last_name.strip()) > 45:
            return False, "Names cannot exceed 45 characters"
    except ValueError:
        return False, "Actor ID must be a valid integer"

    query = "INSERT INTO Actor (Actor_id, First_name, Last_name) VALUES (?, ?, ?)"
    result = execute_query(query, (actor_id, first_name.strip(), last_name.strip()))
    return result

def insert_director(director_id, first_name, last_name):
    """insert new director"""
    # Validate inputs
    try:
        director_id = int(director_id)
        if director_id <= 0:
            return False, "Director ID must be a positive integer"
        if not first_name.strip() or not last_name.strip():
            return False, "First name and last name cannot be empty"
        if len(first_name.strip()) > 45 or len(last_name.strip()) > 45:
            return False, "Names cannot exceed 45 characters"
    except ValueError:
        return False, "Director ID must be a valid integer"

    query = "INSERT INTO Director (Director_id, First_name, Last_name) VALUES (?, ?, ?)"
    result = execute_query(query, (director_id, first_name.strip(), last_name.strip()))
    return result

def insert_genre(genre_id, category):
    """insert new genre"""
    # Validate inputs
    try:
        genre_id = int(genre_id)
        if genre_id <= 0:
            return False, "Genre ID must be a positive integer"
        if not category.strip():
            return False, "Category cannot be empty"
        if len(category.strip()) > 45:
            return False, "Category cannot exceed 45 characters"
    except ValueError:
        return False, "Genre ID must be a valid integer"

    query = "INSERT INTO Genre (Genre_id, Category) VALUES (?, ?)"
    result = execute_query(query, (genre_id, category.strip()))
    return result

def insert_movie(movie_id, title, release_year):
    """insert new movie"""
    # Validate inputs
    try:
        movie_id = int(movie_id)
        release_year = int(release_year)
        if movie_id <= 0:
            return False, "Movie ID must be a positive integer"
        if not title.strip():
            return False, "Title cannot be empty"
        if len(title.strip()) > 45:
            return False, "Title cannot exceed 45 characters"
        if release_year < 1900 or release_year > 2030:
            return False, "Release year must be between 1900 and 2030"
    except ValueError:
        return False, "Movie ID and Release Year must be valid integers"

    query = "INSERT INTO Movie (Movie_id, Title, Release_year) VALUES (?, ?, ?)"
    result = execute_query(query, (movie_id, title.strip(), release_year))
    return result

def insert_review(review_id, rating, movie_id):
    """insert new review"""
    # Validate inputs
    try:
        review_id = int(review_id)
        rating = int(rating)
        movie_id = int(movie_id)
        if review_id <= 0:
            return False, "Review ID must be a positive integer"
        if rating < 1 or rating > 100:
            return False, "Rating must be between 1 and 100"
        if movie_id <= 0:
            return False, "Movie ID must be a positive integer"
    except ValueError:
        return False, "Review ID, Rating, and Movie ID must be valid integers"

    query = "INSERT INTO Review (Review_id, Rating, Movie_Movie_id) VALUES (?, ?, ?)"
    result = execute_query(query, (review_id, rating, movie_id))
    return result

def insert_user(user_id, email, review_id):
    """insert new user"""
    # Validate inputs
    try:
        review_id = int(review_id)
        if not user_id.strip():
            return False, "User ID cannot be empty"
        if not email.strip():
            return False, "Email cannot be empty"
        if len(user_id.strip()) > 25:
            return False, "User ID cannot exceed 25 characters"
        if len(email.strip()) > 45:
            return False, "Email cannot exceed 45 characters"
        if '@' not in email or '.' not in email:
            return False, "Email must be in valid format (contain @ and .)"
    except ValueError:
        return False, "Review ID must be a valid integer"

    query = "INSERT INTO User (User_id, email, Review_Review_id) VALUES (?, ?, ?)"
    result = execute_query(query, (user_id.strip(), email.strip(), review_id))
    return result

def insert_acts_in(actor_id, movie_id):
    """insert actor-movie relationship"""
    # Validate inputs
    try:
        actor_id = int(actor_id)
        movie_id = int(movie_id)
        if actor_id <= 0 or movie_id <= 0:
            return False, "Actor ID and Movie ID must be positive integers"
    except ValueError:
        return False, "Actor ID and Movie ID must be valid integers"

    query = "INSERT INTO Acts_in (Actor_Actor_id, Movie_Movie_id) VALUES (?, ?)"
    result = execute_query(query, (actor_id, movie_id))
    return result

def insert_belongs_to(genre_id, movie_id):
    """insert genre-movie relationship"""
    # Validate inputs
    try:
        genre_id = int(genre_id)
        movie_id = int(movie_id)
        if genre_id <= 0 or movie_id <= 0:
            return False, "Genre ID and Movie ID must be positive integers"
    except ValueError:
        return False, "Genre ID and Movie ID must be valid integers"

    query = "INSERT INTO Belongs_to (Genre_Genre_id, Movie_Movie_id) VALUES (?, ?)"
    result = execute_query(query, (genre_id, movie_id))
    return result

def insert_directed_by(movie_id, director_id):
    """insert director-movie relationship"""
    # Validate inputs
    try:
        movie_id = int(movie_id)
        director_id = int(director_id)
        if movie_id <= 0 or director_id <= 0:
            return False, "Movie ID and Director ID must be positive integers"
    except ValueError:
        return False, "Movie ID and Director ID must be valid integers"

    query = "INSERT INTO Directed_by (Movie_Movie_id, Director_Director_id) VALUES (?, ?)"
    result = execute_query(query, (movie_id, director_id))
    return result

def search_movies_by_title(title):
    """search movies by title"""
    query = "SELECT * FROM Movie WHERE Title LIKE ?"
    return execute_query(query, (f"%{title}%",))

def search_movies_by_year(year):
    """search movies by release year"""
    query = "SELECT * FROM Movie WHERE Release_year = ?"
    return execute_query(query, (year,))

def search_movies_by_actor(actor_name):
    """search movies by actor name"""
    query = """
    SELECT m.* FROM Movie m
    JOIN Acts_in ai ON m.Movie_id = ai.Movie_Movie_id
    JOIN Actor a ON ai.Actor_Actor_id = a.Actor_id
    WHERE (a.First_name || ' ' || a.Last_name) LIKE ?
    """
    return execute_query(query, (f"%{actor_name}%",))

def search_movies_by_genre(genre):
    """search movies by genre"""
    query = """
    SELECT m.* FROM Movie m
    JOIN Belongs_to bt ON m.Movie_id = bt.Movie_Movie_id
    JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
    WHERE g.Category LIKE ?
    """
    return execute_query(query, (f"%{genre}%",))

def delete_actor(actor_id):
    """delete actor by id"""
    # Validate input
    try:
        actor_id = int(actor_id)
        if actor_id <= 0:
            return False, "Actor ID must be a positive integer"
    except ValueError:
        return False, "Actor ID must be a valid integer"

    # First delete related records from junction tables
    query1 = "DELETE FROM Acts_in WHERE Actor_Actor_id = ?"
    execute_query(query1, (actor_id,))
    # Then delete the actor
    query2 = "DELETE FROM Actor WHERE Actor_id = ?"
    return execute_query(query2, (actor_id,))

def delete_director(director_id):
    """delete director by id"""
    # Validate input
    try:
        director_id = int(director_id)
        if director_id <= 0:
            return False, "Director ID must be a positive integer"
    except ValueError:
        return False, "Director ID must be a valid integer"

    # First delete related records from junction tables
    query1 = "DELETE FROM Directed_by WHERE Director_Director_id = ?"
    execute_query(query1, (director_id,))
    # Then delete the director
    query2 = "DELETE FROM Director WHERE Director_id = ?"
    return execute_query(query2, (director_id,))

def delete_genre(genre_id):
    """delete genre by id"""
    # Validate input
    try:
        genre_id = int(genre_id)
        if genre_id <= 0:
            return False, "Genre ID must be a positive integer"
    except ValueError:
        return False, "Genre ID must be a valid integer"

    # First delete related records from junction tables
    query1 = "DELETE FROM Belongs_to WHERE Genre_Genre_id = ?"
    execute_query(query1, (genre_id,))
    # Then delete the genre
    query2 = "DELETE FROM Genre WHERE Genre_id = ?"
    return execute_query(query2, (genre_id,))

def delete_movie(movie_id):
    """delete movie by id"""
    # Validate input
    try:
        movie_id = int(movie_id)
        if movie_id <= 0:
            return False, "Movie ID must be a positive integer"
    except ValueError:
        return False, "Movie ID must be a valid integer"

    # First delete related records from junction tables
    query1 = "DELETE FROM Acts_in WHERE Movie_Movie_id = ?"
    execute_query(query1, (movie_id,))
    query2 = "DELETE FROM Belongs_to WHERE Movie_Movie_id = ?"
    execute_query(query2, (movie_id,))
    query3 = "DELETE FROM Directed_by WHERE Movie_Movie_id = ?"
    execute_query(query3, (movie_id,))
    query4 = "DELETE FROM Review WHERE Movie_Movie_id = ?"
    execute_query(query4, (movie_id,))
    # Then delete the movie
    query5 = "DELETE FROM Movie WHERE Movie_id = ?"
    return execute_query(query5, (movie_id,))

def delete_review(review_id):
    """delete review by id"""
    # Validate input
    try:
        review_id = int(review_id)
        if review_id <= 0:
            return False, "Review ID must be a positive integer"
    except ValueError:
        return False, "Review ID must be a valid integer"

    # First delete related records from User table
    query1 = "DELETE FROM User WHERE Review_Review_id = ?"
    execute_query(query1, (review_id,))
    # Then delete the review
    query2 = "DELETE FROM Review WHERE Review_id = ?"
    return execute_query(query2, (review_id,))

def delete_user(user_id):
    """delete user by id"""
    # Validate input
    if not user_id.strip():
        return False, "User ID cannot be empty"

    query = "DELETE FROM User WHERE User_id = ?"
    return execute_query(query, (user_id.strip(),))

def delete_acts_in(actor_id, movie_id):
    """delete actor-movie relationship"""
    # Validate inputs
    try:
        actor_id = int(actor_id)
        movie_id = int(movie_id)
        if actor_id <= 0 or movie_id <= 0:
            return False, "Actor ID and Movie ID must be positive integers"
    except ValueError:
        return False, "Actor ID and Movie ID must be valid integers"

    query = "DELETE FROM Acts_in WHERE Actor_Actor_id = ? AND Movie_Movie_id = ?"
    return execute_query(query, (actor_id, movie_id))

def delete_belongs_to(genre_id, movie_id):
    """delete genre-movie relationship"""
    # Validate inputs
    try:
        genre_id = int(genre_id)
        movie_id = int(movie_id)
        if genre_id <= 0 or movie_id <= 0:
            return False, "Genre ID and Movie ID must be positive integers"
    except ValueError:
        return False, "Genre ID and Movie ID must be valid integers"

    query = "DELETE FROM Belongs_to WHERE Genre_Genre_id = ? AND Movie_Movie_id = ?"
    return execute_query(query, (genre_id, movie_id))

def delete_directed_by(movie_id, director_id):
    """delete director-movie relationship"""
    # Validate inputs
    try:
        movie_id = int(movie_id)
        director_id = int(director_id)
        if movie_id <= 0 or director_id <= 0:
            return False, "Movie ID and Director ID must be positive integers"
    except ValueError:
        return False, "Movie ID and Director ID must be valid integers"

    query = "DELETE FROM Directed_by WHERE Movie_Movie_id = ? AND Director_Director_id = ?"
    return execute_query(query, (movie_id, director_id))

def update_actor(actor_id, first_name, last_name):
    """update actor by id"""
    # Validate inputs
    try:
        actor_id = int(actor_id)
        if actor_id <= 0:
            return False, "Actor ID must be a positive integer"
        if not first_name.strip() or not last_name.strip():
            return False, "First name and last name cannot be empty"
        if len(first_name.strip()) > 45 or len(last_name.strip()) > 45:
            return False, "Names cannot exceed 45 characters"
    except ValueError:
        return False, "Actor ID must be a valid integer"

    query = "UPDATE Actor SET First_name = ?, Last_name = ? WHERE Actor_id = ?"
    result = execute_query(query, (first_name.strip(), last_name.strip(), actor_id))
    return result

def update_director(director_id, first_name, last_name):
    """update director by id"""
    # Validate inputs
    try:
        director_id = int(director_id)
        if director_id <= 0:
            return False, "Director ID must be a positive integer"
        if not first_name.strip() or not last_name.strip():
            return False, "First name and last name cannot be empty"
        if len(first_name.strip()) > 45 or len(last_name.strip()) > 45:
            return False, "Names cannot exceed 45 characters"
    except ValueError:
        return False, "Director ID must be a valid integer"

    query = "UPDATE Director SET First_name = ?, Last_name = ? WHERE Director_id = ?"
    result = execute_query(query, (first_name.strip(), last_name.strip(), director_id))
    return result

def update_genre(genre_id, category):
    """update genre by id"""
    # Validate inputs
    try:
        genre_id = int(genre_id)
        if genre_id <= 0:
            return False, "Genre ID must be a positive integer"
        if not category.strip():
            return False, "Category cannot be empty"
        if len(category.strip()) > 45:
            return False, "Category cannot exceed 45 characters"
    except ValueError:
        return False, "Genre ID must be a valid integer"

    query = "UPDATE Genre SET Category = ? WHERE Genre_id = ?"
    result = execute_query(query, (category.strip(), genre_id))
    return result

def update_movie(movie_id, title, release_year):
    """update movie by id"""
    # Validate inputs
    try:
        movie_id = int(movie_id)
        release_year = int(release_year)
        if movie_id <= 0:
            return False, "Movie ID must be a positive integer"
        if not title.strip():
            return False, "Title cannot be empty"
        if len(title.strip()) > 45:
            return False, "Title cannot exceed 45 characters"
        if release_year < 1900 or release_year > 2030:
            return False, "Release year must be between 1900 and 2030"
    except ValueError:
        return False, "Movie ID and Release Year must be valid integers"

    query = "UPDATE Movie SET Title = ?, Release_year = ? WHERE Movie_id = ?"
    result = execute_query(query, (title.strip(), release_year, movie_id))
    return result

def update_review(review_id, rating, movie_id):
    """update review by id"""
    # Validate inputs
    try:
        review_id = int(review_id)
        rating = int(rating)
        movie_id = int(movie_id)
        if review_id <= 0:
            return False, "Review ID must be a positive integer"
        if rating < 1 or rating > 100:
            return False, "Rating must be between 1 and 100"
        if movie_id <= 0:
            return False, "Movie ID must be a positive integer"
    except ValueError:
        return False, "Review ID, Rating, and Movie ID must be valid integers"

    query = "UPDATE Review SET Rating = ?, Movie_Movie_id = ? WHERE Review_id = ?"
    result = execute_query(query, (rating, movie_id, review_id))
    return result

def update_user(user_id, email):
    """update user by id"""
    # Validate inputs
    if not user_id.strip():
        return False, "User ID cannot be empty"
    if not email.strip():
        return False, "Email cannot be empty"
    if len(email.strip()) > 45:
        return False, "Email cannot exceed 45 characters"
    if '@' not in email or '.' not in email:
        return False, "Email must be in valid format (contain @ and .)"

    query = "UPDATE User SET email = ? WHERE User_id = ?"
    result = execute_query(query, (email.strip(), user_id.strip()))
    return result

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