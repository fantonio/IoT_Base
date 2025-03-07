from flask import Flask, render_template, redirect, url_for, session
from extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.devices import devices_bp
    from routes.workspace import workspace_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(devices_bp)
    app.register_blueprint(workspace_bp)

    # Criando um blueprint para a página inicial
    from flask import Blueprint
    main_bp = Blueprint('main', __name__)

    @main_bp.route('/')
    def index():
        if 'user_id' in session:
            return render_template(url_for('templates/index.html'))
        return redirect('auth.login')

    return app

app = create_app()

# Criando o banco de dados se não existir
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)