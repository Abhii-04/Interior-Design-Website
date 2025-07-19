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
        # Use Render PostgreSQL connection string as default
        SQLALCHEMY_DATABASE_URI = 'postgresql://interior_website_user:JRFWFFhBrxOsPCnAud7UTlqfHZNZsJfl@dpg-d1th3gadbo4c73dj8tdg-a/interior_website'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
