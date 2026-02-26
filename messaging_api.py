from flask import Flask,request,jsonify,session,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import smtplib
import random
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "@messaging-to-friend"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class User_Creation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_email = db.Column(db.String(200),nullable=False,unique=True)
    user_name = db.Column(db.String(150),nullable=False,unique=True)
    user_password = db.Column(db.String(150),nullable=False)


otp_storage = {}
Email_Admin = "pallapothugayathri23@gmail.com"
Pass_Admin = "lipk dqji vtbn wiox"
@app.route("/verification",methods=["POST"])
def verification():
    data = request.get_json()
    if not data or "user_email" not in data:
        return jsonify({"message": "Email required for verification."}), 400
    
    user_email = data["user_email"]
    session["user_email"] = user_email
    msg = EmailMessage()
    msg['From'] = Email_Admin
    msg["To"] = user_email
    msg["Subject"] = "Email Verification For The Messaging App"

    otp = random.randint(100000,999999)
    session['otp'] = otp
    otp_storage[user_email] = otp

    msg.set_content(f"These verification otp from the messaging app {otp}")
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(Email_Admin,Pass_Admin)
        server.send_message(msg)
    return jsonify({"message":"OTP send successfully."})
    
@app.route("/verification2",methods=["GET","POST"])
def verification2():
    data = request.get_json()
    session_otp = session.get("otp")
    stored_otp = str(otp_storage.get(data["email"]))
    print(session.get("otp"))
    if data["otp"] == stored_otp:
        del otp_storage[data["email"]]
        return jsonify({"message":"Email Verified"})
    else:
        return jsonify({"message":"OTP not match."})
    
@app.route("/user_create",methods=['GET','POST'])
def create_user():
    user_data = request.get_json()
    if not user_data or 'user_name' not in user_data or "user_password" not in user_data:
        return jsonify({'message':'There is a Problem in user creation.'})
    new_user = User_Creation(
        user_email = user_data["user_email"],
        user_name = user_data['user_name'],
        user_password = generate_password_hash(user_data["user_password"])
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"user created successfully."})
    except Exception as e:
        return jsonify({"message":"Problem in Creation."})

@app.route("/user_login",methods=["GET","POST"])
def user_login():
    user_data = request.get_json()
    user_name = user_data["user_name"]
    user_pass = user_data["user_password"]
    if "user_name" not in user_data or "user_password" not in user_data or not user_data:
        return jsonify({"message":"there is a not sent full data."})  
    user = User_Creation.query.filter_by(user_name = user_name).first()

    if user and check_password_hash(user.user_password,user_pass):
        return jsonify({"message":"User Successfully Login."})
    else:
        return jsonify({"message":"User Credentials are Wrong."})



@app.route("/debug_users")
def debug_users():
    users = User_Creation.query.all()

    for user in users:
        print(user.id, user.user_email, user.user_name)

    return jsonify({"message": "Printed all users in terminal"})






with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)