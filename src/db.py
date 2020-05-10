from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table_userworksp = db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

class Workspace(db.Model):
    __tablename__ = "workspace"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    users = db.relationship("User", secondary = )
    channels = db.relationship("Channel", cascade = "delete")
    dm_groups = db.relationship('')

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.url = kwargs.get("url", "")

    def serialize(self):
    users = db.relationship('User', secondary = association_table_userworksp, back_populates='workspaces')
    channels = db.relationship('Channel', cascade = "delete")
    dm_groups = db.relationship('')


class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column (db.String, nullable = False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=True)
    active = db.Column (db.Boolean, nullable = False)
    do_not_disturb = db.Column (db.Boolean, nullable = False)
    workspaces = db.relationship('Workspace', secondary=association_table_userworksp, back_populates='users')
<<<<<<< HEAD
=======


class Channel(db.Model):
    __tablename__='channel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    workspace_id = #relationship
    users = #relationship
    public = db.Column(db.String, nullable=True) #public or private
    
class Message(db.Model):
    __tablename__='message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column (db.String, nullable = False)
    timestamp = db.Column (db.String, nullable = False)
    channel = #relationship
    threads = #relationship
    
class Thread(db.Model):
    __tablename__='thread'
    id = db.Column(db.Integer, primary_key = True)
    sender = #relationship
    timestamp = db.Column (db.String, nullable = False)
    message = #relationship

class DM(db.Model):
    __tablename__='dm'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column (db.String, nullable = False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=True)
    active = db.Column (db.Boolean, nullable = False)
    do_not_disturb = db.Column (db.Boolean, nullable = False)
    workspaces = db.relationship('Workspace', secondary=association_table_userworksp, back_populates='users')
    
class DMmessage(db.Model):
    __tablename__='dm_message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column (db.String, nullable = False)
    timestamp = db.Column (db.String, nullable = False)
    dm = #relationship
>>>>>>> d2f6303d905a49a2f2d42e10f3127357f2a0d16b
