from flask import Flask
from flask_mongoengine import MongoEngine
import uuid
import certifi
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required, hash_password


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'some-salt'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False


app.config['MONGODB_HOST'] = {
    'db': 'myapp',
    'host': "mongodb+srv://rohini:rohini12@cluster0.4b088.mongodb.net/myapp?retryWrites=true&w=majority",
    'tlsCAFile': certifi.where()
}

db = MongoEngine(app)
with app.app_context():
    try:
        db.connection.admin.command('ping')
        print("MongoDB connection successful!")
    except Exception as e:
        print("MongoDB connection failed:", e)

class Role(db.Document, RoleMixin):

    name = db.StringField(max_length=80, unique=True)

class User(db.Document, UserMixin):
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField()
    active = db.BooleanField(default=True)
    fs_uniquifier = db.StringField(unique=True)  
    roles = db.ListField(db.ReferenceField(Role), default=[])


user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/dashboard')
@login_required
def dashboard():
    return "This is a secure dashboard using MongoDB!"

@app.before_first_request
def create_user():
    print("Checking if admin user exists...")
    if not user_datastore.find_user(email='admin@example.com'):
        print("Creating admin user...")
        user_datastore.create_user(
            email='admin@example.com',
            password=hash_password('password123'),
            fs_uniquifier=str(uuid.uuid4())  
        )
        db.connection.admin.command('ping') 
        print("Admin user created.")

if __name__ == '__main__':
    app.run(debug=True)
