from flask import Flask, request, render_template
from flask_login import current_user
from user_model import db, UserModel


from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<db_name>.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_table():
    db.create_all()

email = raw_input("Please enter email \n")
user_name = raw_input("Please enter user name \n")
password = raw_input("Please enter password \n")

user = UserModel(email=email, username=user_name)
user.set_password(password)
db.session.add(user)
db.session.commit()