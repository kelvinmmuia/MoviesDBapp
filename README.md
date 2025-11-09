# 🎬 Movie Database Management System

A beautiful and comprehensive movie database management system built with Streamlit, featuring a professional blue and gray theme.

## 🌐 Live Demo

Access the deployed application at: [https://moviesdbapp.streamlit.app/](https://moviesdbapp.streamlit.app/)

## ✨ Features

- **🎭 Actor Management**: Add, view, and manage movie actors
- **🎬 Director Management**: Handle film directors and their information
- **🏷️ Genre Management**: Organize movies by genre categories
- **🎪 Movie Database**: Complete movie catalog with titles and release years
- **⭐ Review System**: Rate movies and track user reviews
- **🔍 Advanced Search**: Search movies by title, year, actor, or genre
- **📊 Data Visualization**: View all database tables with export options
- **⚡ SQL Query Tool**: Execute custom SELECT queries safely
- **🔗 Relationship Management**: Link actors, directors, and genres to movies

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Streamlit

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kelvinmmuia/MoviesDBapp.git
   cd MoviesDBapp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database:**
   ```bash
   python database_creation.py
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 🎨 Design Features

- **Professional UI**: Clean, modern interface with intuitive navigation
- **Blue & Gray Theme**: Eye-strain reducing color palette with purposeful color usage
- **Responsive Design**: Works seamlessly across different screen sizes
- **Interactive Elements**: Hover effects, loading spinners, and smooth transitions
- **Accessibility**: High contrast ratios and semantic color coding

## 📁 Project Structure

```
MoviesDBapp/
├── app.py                    # Main Streamlit application
├── database.py              # Database operations (SQLite)
├── database_creation.py     # Database initialization script
├── MovieDatabase.db         # SQLite database file
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Database**: SQLite
- **Styling**: Custom CSS with Streamlit theme configuration
- **Deployment**: Streamlit Cloud

## 📊 Database Schema

The application uses a relational database with the following tables:
- `Actor` - Movie actors
- `Director` - Film directors
- `Genre` - Movie genres
- `Movie` - Movie catalog
- `Review` - Movie ratings
- `User` - User accounts
- `Acts_in` - Actor-Movie relationships
- `Belongs_to` - Genre-Movie relationships
- `Directed_by` - Director-Movie relationships

## 🔒 Security Features

- **Safe SQL Queries**: Only SELECT statements allowed in the query tool
- **Input Validation**: Form validation and error handling
- **No External Dependencies**: Self-contained SQLite database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **GitHub**: [kelvinmmuia](https://github.com/kelvinmmuia)
- **Live App**: [https://moviesdbapp.streamlit.app/](https://moviesdbapp.streamlit.app/)

---

**Built with ❤️ using Streamlit**