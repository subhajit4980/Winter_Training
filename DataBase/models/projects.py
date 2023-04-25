from config import db

class Project(db.Model):
    __tablename__ = 'projects'# table name should be same as filename user
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    desc=db.Column(db.String(255), nullable=False)
    start_date=db.Column(db.String(255), nullable=False)
    end_date=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    