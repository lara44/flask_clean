from flask import Flask
from app.interface.routes import register_routes

def create_app():
    app = Flask(__name__)

    # Inyección de dependencias futuras podría ir aquí (repositorios, servicios, etc.)
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
