# 🎬 Movie Database Management System

A beautiful and comprehensive movie database management system built with Streamlit, featuring a professional blue and gray theme.

## 🌐 Live Demo

Access the deployed application at: [https://moviesdbapp.streamlit.app/](https://moviesdbapp.streamlit.app/)

## ✨ Features

- **🎭 Complete CRUD Operations**: Create, Read, Update, and Delete for all database entities
- **➕ Add Data**: Insert new actors, directors, genres, movies, reviews, and users
- **📝 Update Data**: Modify existing records with form validation
- **🗑️ Delete Data**: Remove records with automatic relationship cleanup
- **🔍 Advanced Search**: Find movies by title, year, actor, or genre
- **📊 Data Visualization**: View all database tables with CSV export options
- **⚡ SQL Query Tool**: Execute custom SELECT queries with security restrictions
- **🔗 Relationship Management**: Link actors, directors, and genres to movies
- **🎨 Professional UI**: Beautiful blue and gray theme with responsive design

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
├── app.py                    # Main Streamlit application with full CRUD operations
├── database.py              # SQLite database operations and validation
├── database_creation.py     # Database initialization with sample data
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml         # Professional blue & gray theme configuration
├── .gitignore              # Git ignore rules (excludes .db, .sql files)
└── README.md               # Project documentation
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

- **Safe SQL Queries**: Only SELECT statements allowed in the query tool (blocks DROP, DELETE, UPDATE, INSERT, ALTER, CREATE, TRUNCATE)
- **Comprehensive Input Validation**: Type checking, range validation, length limits, and format validation
- **Error Handling**: Detailed error messages guide users to correct inputs
- **Self-contained Database**: SQLite with no external server dependencies
- **Foreign Key Protection**: Automatic relationship cleanup during deletions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Learning Outcomes

This project demonstrates:
- **Full CRUD Operations**: Complete database management workflow
- **Database Design**: Relational database schema with foreign keys
- **UI/UX Design**: Professional web application development
- **Data Validation**: Input sanitization and error handling
- **SQL Security**: Safe query execution and injection prevention
- **Deployment**: Cloud hosting and version control best practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

- **GitHub**: [kelvinmmuia](https://github.com/kelvinmmuia)
- **Live App**: [https://moviesdbapp.streamlit.app/](https://moviesdbapp.streamlit.app/)
- **LinkedIn**: [Your LinkedIn Profile]

---

**🎬 Built with ❤️ using Streamlit - Perfect for learning database management and web app development!**