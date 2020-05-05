from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Workspace(db.Model):
    __tablename__ = "workspace"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    users = db.relationship('User', secondary = )
    channels = db.relationship('Channel', cascade = "delete")
    dm_groups = db.relationship('')
