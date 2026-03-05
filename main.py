from database import init_database
from flask import Flask
from routes import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

def init():
    init_database()

def create_app():
    init()
    return app

def main():
    init()
    app.run(debug=True, host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
