# Decorilla - Interior Design Service

A Flask web application for an online interior design service.

## Features

- User authentication (register, login, logout)
- Project management for interior design projects
- Design portfolio showcase
- Style quiz for personalized recommendations
- Responsive design for all devices

## Project Structure

```
decorilla/
├── app/                    # Application package
│   ├── __init__.py         # App initialization
│   ├── models/             # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── project.py
│   │   └── design.py
│   ├── routes/             # Route blueprints
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── auth.py
│   │   └── projects.py
│   ├── static/             # Static files
│   │   ├── styles/
│   │   └── javascript/
│   └── templates/          # HTML templates
├── migrations/             # Database migrations
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── config.py               # Configuration
├── requirements.txt        # Dependencies
└── run.py                  # Application entry point
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd decorilla
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:
   ```
   python run.py
   ```

## Development

- To create a new database migration after model changes:
  ```
  flask db migrate -m "Description of changes"
  flask db upgrade
  ```

- To run tests:
  ```
  pytest
  ```

## Deployment

For production deployment:

1. Set environment variables for production:
   ```
   FLASK_ENV=production
   FLASK_CONFIG=production
   SECRET_KEY=<strong-secret-key>
   DATABASE_URL=<production-database-url>
   ```

2. Use a production WSGI server like Gunicorn:
   ```
   gunicorn "app:create_app()"
   ```

## License

[MIT License](LICENSE)