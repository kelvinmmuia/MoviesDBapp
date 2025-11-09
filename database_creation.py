# Convert MySQL database to SQLite

import sqlite3
from pathlib import Path

# SQLite database path
DB_PATH = Path(__file__).parent / 'MovieDatabase.db'

def create_sqlite_database():
    """Create SQLite database from MySQL schema"""

    # Connect to SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables (SQLite syntax - no ENGINE, CHARSET, etc.)
    tables_sql = [
        """
        CREATE TABLE IF NOT EXISTS Actor (
            Actor_id INTEGER PRIMARY KEY,
            First_name TEXT,
            Last_name TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Director (
            Director_id INTEGER PRIMARY KEY,
            First_name TEXT,
            Last_name TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Genre (
            Genre_id INTEGER PRIMARY KEY,
            Category TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Movie (
            Movie_id INTEGER PRIMARY KEY,
            Title TEXT,
            Release_year INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Review (
            Review_id INTEGER PRIMARY KEY,
            Rating INTEGER,
            Movie_Movie_id INTEGER,
            FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS User (
            User_id TEXT PRIMARY KEY,
            email TEXT,
            Review_Review_id INTEGER,
            FOREIGN KEY (Review_Review_id) REFERENCES Review (Review_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Acts_in (
            Actor_Actor_id INTEGER,
            Movie_Movie_id INTEGER,
            PRIMARY KEY (Actor_Actor_id, Movie_Movie_id),
            FOREIGN KEY (Actor_Actor_id) REFERENCES Actor (Actor_id),
            FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Belongs_to (
            Genre_Genre_id INTEGER,
            Movie_Movie_id INTEGER,
            PRIMARY KEY (Genre_Genre_id, Movie_Movie_id),
            FOREIGN KEY (Genre_Genre_id) REFERENCES Genre (Genre_id),
            FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Directed_by (
            Movie_Movie_id INTEGER,
            Director_Director_id INTEGER,
            PRIMARY KEY (Movie_Movie_id, Director_Director_id),
            FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id),
            FOREIGN KEY (Director_Director_id) REFERENCES Director (Director_id)
        )
        """
    ]

    # Execute table creation
    for sql in tables_sql:
        cursor.execute(sql)

    # Insert sample data
    sample_data = [
        # Actor data
        ("INSERT OR IGNORE INTO Actor VALUES (?, ?, ?)", [
            (122856, 'Jack', 'Black'),
            (135795, 'Johnny', 'Depp'),
            (175966, 'Chris', 'Hemsworth'),
            (246802, 'Natalie', 'Portman'),
            (446902, 'Scarlett', 'Johansson'),
            (629578, 'Jennifer', 'Lawrence'),
            (754201, 'Marilyn', 'Monroe'),
            (853301, 'Morgan', 'Freeman'),
            (918273, 'Harrison', 'Ford'),
            (987654, 'Emma', 'Stone')
        ]),

        # Director data
        ("INSERT OR IGNORE INTO Director VALUES (?, ?, ?)", [
            (113579, 'Alfred', 'Hitchcock'),
            (146802, 'Emilio', 'Fernandez'),
            (234680, 'Nora', 'Ephron'),
            (366802, 'Spike', 'Lee'),
            (586802, 'John', 'Huston'),
            (597913, 'Agnes', 'Varda'),
            (630246, 'Sidney', 'Lumet'),
            (723456, 'Chantal', 'Akerman'),
            (801234, 'Stanley', 'Kubrick'),
            (990123, 'Hayao', 'Miyazaki')
        ]),

        # Genre data
        ("INSERT OR IGNORE INTO Genre VALUES (?, ?)", [
            (334497, 'Science Fiction'),
            (456789, 'Action'),
            (542261, 'Western'),
            (670518, 'Comedy'),
            (732871, 'Fantasy'),
            (765903, 'Thriller'),
            (845309, 'Romance'),
            (846342, 'Adventure'),
            (956721, 'Horror'),
            (968025, 'Musical')
        ]),

        # Movie data
        ("INSERT OR IGNORE INTO Movie VALUES (?, ?, ?)", [
            (121798, 'Coraline', 2009),
            (121978, 'The Iron Giant', 1999),
            (294658, 'Toy Story', 1995),
            (305542, 'The Lion King', 1994),
            (478548, 'Coco', 2017),
            (585388, 'The Godfather', 1972),
            (614005, 'Spirited Away', 2001),
            (751896, 'Moana', 2016),
            (831719, 'Jaws', 1975),
            (896786, 'Up', 2009)
        ]),

        # Review data
        ("INSERT OR IGNORE INTO Review VALUES (?, ?, ?)", [
            (123456, 78, 585388),
            (248420, 81, 831719),
            (270372, 89, 614005),
            (324700, 50, 121978),
            (398999, 80, 121978),
            (521197, 96, 478548),
            (649391, 43, 305542),
            (930639, 75, 294658),
            (969856, 67, 751896),
            (975311, 91, 896786)
        ]),

        # User data
        ("INSERT OR IGNORE INTO User VALUES (?, ?, ?)", [
            ('alice', 'alice@email.com', 969856),
            ('angrybirds', 'angrybirds@email.com', 270372),
            ('beefeater', 'beefeater@emai.com', 521197),
            ('bigbadhat', 'bigbadhat@email.com', 398999),
            ('blueberyy', 'blueberry@email.com', 649391),
            ('chicken', 'chicken@email.com', 324700),
            ('froggy', 'froggy@email.com', 123456),
            ('scarypear', 'scarypear@email.com', 930639),
            ('tennisfan', 'tennisfan@email.com', 975311),
            ('yellowbear', 'yellowbear@email.com', 248420)
        ]),

        # Acts_in data
        ("INSERT OR IGNORE INTO Acts_in VALUES (?, ?)", [
            (122856, 121798), (135795, 121798), (987654, 121798),
            (246802, 121978), (446902, 121978), (918273, 121978),
            (122856, 294658), (135795, 294658), (987654, 294658),
            (135795, 305542), (853301, 305542), (987654, 305542),
            (122856, 478548), (135795, 478548),
            (853301, 585388), (918273, 585388),
            (246802, 614005), (446902, 614005), (629578, 614005),
            (122856, 751896), (175966, 751896), (629578, 751896),
            (122856, 831719), (175966, 831719),
            (122856, 896786), (754201, 896786), (853301, 896786)
        ]),

        # Belongs_to data
        ("INSERT OR IGNORE INTO Belongs_to VALUES (?, ?)", [
            (956721, 121798), (846342, 121978), (670518, 294658),
            (846342, 294658), (846342, 305542), (968025, 305542),
            (846342, 478548), (968025, 478548), (456789, 585388),
            (732871, 614005), (846342, 614005), (846342, 751896),
            (765903, 831719), (732871, 896786)
        ]),

        # Directed_by data
        ("INSERT OR IGNORE INTO Directed_by VALUES (?, ?)", [
            (585388, 113579), (121798, 146802), (478548, 146802),
            (751896, 146802), (831719, 234680), (585388, 366802),
            (896786, 586802), (121798, 597913), (121978, 597913),
            (121978, 630246), (614005, 723456), (305542, 801234),
            (305542, 990123)
        ])
    ]

    # Insert all sample data
    for sql, data_list in sample_data:
        for data in data_list:
            cursor.execute(sql, data)

    # Commit and close
    conn.commit()
    conn.close()

    print("SQLite database created successfully with sample data!")

if __name__ == "__main__":
    create_sqlite_database()