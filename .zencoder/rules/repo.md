---
description: Repository Information Overview
alwaysApply: true
---

# Interior Design Website Information

## Summary
A Flask-based web application for an interior design service, inspired by Decorilla. The application provides portfolio management, user authentication, admin dashboard, and various interactive features like quizzes and consultations.

## Structure
- **app.py**: Main Flask application with routes and initialization
- **models.py**: Database models for users, projects, designs, and admin content
- **config.py**: Application configuration including database settings
- **run_app.py**: Application startup script
- **setup_admin.py**: Database and admin user setup script
- **templates/**: HTML templates for all pages
- **static/**: CSS, JavaScript, and image assets
- **migrations/**: Database migration files

## Language & Runtime
**Language**: Python
**Version**: Python 3.x
**Framework**: Flask 3.1.1
**Database**: PostgreSQL
**ORM**: SQLAlchemy 2.0.28

## Dependencies
**Main Dependencies**:
- Flask-Login 0.6.3: User authentication
- Flask-SQLAlchemy 3.1.1: Database ORM
- Flask-Bcrypt 1.0.1: Password hashing
- Flask-Migrate 4.0.5: Database migrations
- Werkzeug 3.1.3: WSGI utilities
- Jinja2 3.1.6: Template engine

**Development Dependencies**:
- python-dotenv 1.0.1: Environment variable management

## Build & Installation
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database and admin user
python setup_admin.py

# Run the application
python run_app.py
```

## Database
**Type**: PostgreSQL
**Configuration**: 
- Host: localhost
- Port: 5432
- Database: interior_design
- User: postgres

**Models**:
- User: User accounts and authentication
- Project: User projects
- Design: Design concepts
- DesignImage: Images for designs
- Review: User reviews
- AdminUser: Admin user management
- Card: Service cards for various pages
- FAQ: Frequently asked questions
- QuizQuestion: Quiz functionality
- PortfolioItem: Portfolio projects with CRUD operations

## Testing
No specific testing framework is configured in the project. Manual testing through the web interface is the primary method.

## Key Features
- **User Authentication**: Registration, login, and profile management
- **Admin Dashboard**: Content management for portfolio, FAQs, and services
- **Portfolio Management**: Dynamic portfolio display with filtering
- **Interactive Elements**: Quizzes, consultations, and reviews
- **Responsive Design**: Mobile-friendly interface

## Admin Access
- Default credentials: admin / admin123
- Admin dashboard: http://localhost:5000/admin
- Portfolio management: http://localhost:5000/admin/portfolio