# Import routes to make them available when importing the package
from app.routes.main import main_bp
from app.routes.auth import auth_bp
from app.routes.projects import projects_bp