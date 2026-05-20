from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

from config import Config

# Load environment variables from .env file
load_dotenv()

# Initialize Flask extensions
mysql = MySQL()
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize extensions with app
    mysql.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Flask-Login settings
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    # -------------------------------
    # Basic Routes
    # -------------------------------

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {
            "status": "running",
            "project": "AI-Powered Role-Based SaaS Billing & Analytics Portal"
        }

    # -------------------------------
    # Error Handlers
    # -------------------------------

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("500.html"), 500

    # -------------------------------
    # Register Blueprints
    # -------------------------------

    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.user_routes import user_bp
    from routes.company_routes import company_bp
    from routes.subscription_routes import subscription_bp
    from routes.billing_routes import billing_bp
    from routes.invoice_routes import invoice_bp
    from routes.analytics_routes import analytics_bp
    from routes.notification_routes import notification_bp
    from routes.admin_routes import admin_bp
    from routes.finance_routes import finance_bp
    from routes.api_routes import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(subscription_bp)
    app.register_blueprint(billing_bp)
    app.register_blueprint(invoice_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(finance_bp)
    app.register_blueprint(api_bp)

    return app