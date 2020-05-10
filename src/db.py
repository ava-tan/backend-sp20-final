from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table_userworksp = db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_chnworksp= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

association_table_chnusers= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

association_table_chnworksp= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

association_table_chnmsgs= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

association_table_chnthreads= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

class Workspace(db.Model):
    __tablename__ = "workspace"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    users = db.relationship('User', secondary = association_table_userworksp, back_populates='workspaces')
    channels = db.relationship('Channel', cascade = "delete")
    dm_groups = db.relationship('')

association_table_threaduser= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

association_table_threadmsg= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    
association_table_dmmsgs= db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    

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
    


class Channel(db.Model):
    __tablename__='channel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    workspace_id = #relationship
    users = #relationship
    messages = #relationship
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
    name = db.Column(db.String, nullable=True)
    workspaces = #relationship
    users = #relationship
    messages =

class DMmessage(db.Model):
    __tablename__='dm_message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column (db.String, nullable = False)
    timestamp = db.Column (db.String, nullable = False)
    dm = #relationship
