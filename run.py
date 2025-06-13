import os
from app import create_app, db

# Get configuration from environment or use default
config_name = os.environ.get('FLASK_CONFIG', 'default')
from config import config
app = create_app(config[config_name])

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)