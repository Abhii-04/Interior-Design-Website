import os
from app import create_app, db
from flask_cors import CORS

# Get configuration from environment or use default
config_name = os.environ.get('FLASK_CONFIG', 'default')
from config import config
app = create_app(config[config_name])

# Enable CORS for all routes
CORS(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Enable debug mode for auto-reloading when code changes
    # Host 0.0.0.0 makes the server accessible from any device on the network
    # Use port 5000 by default, but allow it to be overridden by environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=True)