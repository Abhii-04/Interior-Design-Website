import os
from datetime import timedelta

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    
    # Database settings
    # Check if DATABASE_URL environment variable exists (for production)
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        # Local PostgreSQL settings
        POSTGRES_USER = 'postgres'  # default superuser
        POSTGRES_PASSWORD = 'qwertyuiop'  # replace with the password you set during installation
        POSTGRES_HOST = 'localhost'
        POSTGRES_PORT = '5432'
        POSTGRES_DB = 'interior_design'
        SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
