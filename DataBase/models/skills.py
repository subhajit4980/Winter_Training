from config import db

class Skills(db.Model):
    __tablename__ = 'skills'# table name should be same as filename user
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255), nullable=False)
    confidence_score=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
