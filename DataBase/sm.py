from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path,getcwd,environ
from dotenv import load_dotenv
from models.user1 import User
from models.personaldetails import PersonalDetails
from models.projects import Projects
from models.experiences import Experience
from models.educations import Education
from models.skills import Skill
from models.certificates import Certificate

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(_name_)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():

        @app.route("/signup",methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data['username']

            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="user added sudccessfully")

            #PERSONAL DETAILS

        @app.route("/add_personal_details",methods=['POST'])
        def add_personal_details():
            username = request.args.get('username')
            user1 = User.query.filter_by(username=username).first()

            personal_data = request.get_json()
            new_personal_details = PersonalDetails(
                name=personal_data['name'],
                email=personal_data['email'],
                phone=personal_data['phone'],
                # address=personal_data['address'],
                linkedin_url=personal_data['linkedin_link'],
                user_id=user1.id
            )
            db.session.add(new_personal_details)
            db.session.commit()
            print(personal_data)
            return jsonify(msg="personal details added sudccessfully")

#PROJECTS..
        @app.route("/add_projects",methods=['POST'])
        def add_projects():
            username = request.args.get('username')
            user1 = User.query.filter_by(username=username).first()

            project_data = request.get_json()
            for project in project_data["data"]:
                new_project = Projects(
                    name=project['name'],
                    desc=project['description'],
                    start_date=project['start_date'],
                    end_date=project['end_date'],
                    user_id=user1.id
                )
            
                db.session.add(new_project)
                db.session.commit()
            return jsonify(msg="project data added sudccessfully")

#EXPERIENCES...
        @app.route("/add_experiences",methods=['POST'])
        def add_experiences():
            username = request.args.get('username')
            user1 = User.query.filter_by(username=username).first()

            experience_data = request.get_json()
            for experience in experience_data["data"]:
                new_experience = Experience(
                    company_name=project['company_name'],
                    role=project['role'],
                    role_desc=project['role_description'],
                    start_date=project['start_date'],
                    end_date=project['end_date'],
                    user_id=user1.id
                )
            
                db.session.add(new_experience)
                db.session.commit()
            return jsonify(msg="experience added sudccessfully")

            #repeat the abvove for others....


        @app.route("get_resume_json",methods=["GET"])
        def get_resume_json():
            recv_username=request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            personal_details = PersonalDetails.query.filter_by(user_id=user1.id).first()
            experience = Experience.query.filter_by(user_id=user1.id).first()
            projects = Projects.query.filter_by(user_id=user1.id).first()
            educations = Education.query.filter_by(user_id=user1.id).first()
            certificates = Certificate.query.filter_by(user_id=user1.id).first()
            skills = Skill.query.filter_by(user_id=user1.id).first()

            resume_data = {
                "name": personal_details.name,
                "email": personal_details.email,
                "phone": personal_details.phone,
                "linkedin_url": personal_details.linkedin_url
            }

            # experience
            for exp in experiences:
                experiences_data.append({
                    "company_name":exp.company_name,
                    "role":exp.role,
                    "role_desc":exp.role_desc,
                    "start_date":exp.start_date,
                    "end_date":exp.end_date
                })
            resume_data["experiences"] = experiences_data

#repeat the above process for others..

            return resume_data

        # db.drop_all()
        db.create_all()
        db.session.commit()

        return app

if _name_ == '_main_':
    app = create_app()
    app.run(debug=True)