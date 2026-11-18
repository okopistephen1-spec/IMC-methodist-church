from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Database extension
db = SQLAlchemy()

# Database migration extension
migrate = Migrate()

# User authentication extension
login_manager = LoginManager()