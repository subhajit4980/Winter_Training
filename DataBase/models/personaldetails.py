from config import db

class Personaldetails(db.Model):
    __tablename__ = 'personaldetails'# table name should be same as filename user
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    phone=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    address=db.Column(db.String(455), nullable=False)
    linkedin_url=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)