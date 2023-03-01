from flask import Flask
from routes.tasks import task_bp 
from routes.auth import auth_bp
app = Flask(__name__)


app.register_blueprint(task_bp)
app.register_blueprint(auth_bp)