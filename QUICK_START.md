Movie Database - Quick Start

1. Install MySQL
- Download and install MySQL Server from https://dev.mysql.com/downloads/mysql/
- Remember your root password during installation

2. Install Python Packages
- Open CMD, and navigate to the folder with the python script files.
pip install -r requirements.txt

3. Configure Password
- Open .env file
- Set MYSQL_ROOT_PASSWORD=your_mysql_password

4. Create Database
python database_creation.py

5. Run Application
streamlit run app.py

6. Open Browser
- Go to http://localhost:8501
- Start using the Movie Database!

Features
- Add new movies, actors, directors, etc.
- Delete records
- Link actors, genres, and directors to movies
- Search movies by title, year, actor, or genre
- View all data in tables
- Run custom SQL queries

That's it! the streamlit application is ready to use.