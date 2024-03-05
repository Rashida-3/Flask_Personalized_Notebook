from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.secret_key='your_secret_key'

def create_app():
    from auth import auth_blueprint
    from notes import notes_blueprint
    

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(notes_blueprint)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    create_app().run(debug=True)