from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from config import db,SECRET_KEY
from os import path,getcwd,environ
from dotenv import load_dotenv
from models.user import User
# from models.projects import Project
from models.certificate import Certificate
from models.skills import Skills
from models.education import Education
from models.personaldetails import Personaldetails
from models.experience import Experience

load_dotenv(path.join(getcwd(),'.env'))

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] =False
    app.config['SQLALCHEMY_ECHO'] =False
    app.secret_key =SECRET_KEY

    db.init_app(app)
    print("db initialized successfully")
    with app.app_context():
        @app.route("/signup",methods=['POST'])
        def signup():
            data=request.form.to_dict(flat=True)
            new_user=User(
                username=data['username']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="user added successfully")
                #PERSONAL DETAILS

        @app.route("/add_personal_details",methods=['POST'])
        def add_personal_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            personal_data = request.get_json()
            new_personal_details = Personaldetails(
                name=personal_data['name'],
                phone=personal_data['phone'],
                email=personal_data['email'],
                address=personal_data['address'],
                linkedin_url=personal_data['linkedin_link'],
                user_id=user.id
            )
            db.session.add(new_personal_details)
            db.session.commit()
            print(personal_data)
            return jsonify(msg="personal details added sudccessfully")
        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app
if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
