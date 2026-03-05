from database import init_database
from flask import Flask
from routes import main_bp

def main():
    init_database()
    app = Flask(__name__)
    app.register_blueprint(main_bp)

if __name__ == "__main__":
    main()