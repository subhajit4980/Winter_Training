from config import db

class User(db.Model):
    __tablename__ = 'user'# table name should be same as filename user
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), nullable=False)
    # projects=db.relationship('Project',backref='user')
    PersonalDetails=db.relationship('Personaldetails',backref='user')
    # Experience=db.relationship('Experience',backref='user')
    # Education=db.relationship('Education',backref='user')
    # Certificate=db.relationship('Certificate',backref='user')
    # skills=db.relationship('Skills',backref='user')