from config import db

class Experience(db.Model):
    __tablename__ = 'experience'# table name should be same as filename user
    id=db.Column(db.Integer, primary_key=True)
    company_name=db.Column(db.String(255), nullable=False)
    role=db.Column(db.String(255), nullable=False)
    role_desc=db.Column(db.String(255), nullable=False)
    start_date=db.Column(db.String(255), nullable=False)
    end_date=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

