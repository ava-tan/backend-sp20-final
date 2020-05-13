from flask_sqlalchemy import SQLAlchemy
from time import time, ctime
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
    users = db.relationship('User', secondary = association_table_userworksp, back_populates='workspaces')
    channels = db.relationship('Channel', cascade = "delete")
    dm_groups = db.relationship('DM', cascade='delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.url = kwargs.get('url', '')

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'users': [a.serialize_name() for a in self.users],
            'channels': [s.serialize_name() for s in self.channels],
            'direct messages': [c.serialize_for_channel() for c in self.dm_groups]
        }

    def serialize_name(self):
        return{
            'id':self.id,
            'name':self.name,
            'url':self.url
        }


class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=True)
    active = db.Column (db.Boolean, nullable = False)
    do_not_disturb = db.Column (db.Boolean, nullable = False)
    workspaces = db.relationship('Workspace', secondary=association_table_userworksp, back_populates='users')
    channels = db.relationship('Channel', cascade='delete')  #relationship one (user) to many (channels)
    messages = db.relationship('User', cascade='delete') #relationship one (user) to many (dms)
    dms = db.relationship('DM', cascade='delete') #relationship one (user) to many (dms)
    dm_messages = db.relationship('Dm_messages', cascade='delete')
    threads = db.relationship('Thread', cascade='delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.status = kwargs.get('status', '')
        self.active = kwargs.get('active', '')
        self.do_not_disturb = kwargs.get('do_not_disturb', '')

   def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'status':self.status,
            'active':self.active,
            'do_not_disturb':self.do_not_disturb,
            'workspaces':[a.serialize_name() for a in self.workspaces],
            'channels':[s.serialize_name() for s in self.channels],
            'direct messages':[c.serialize_for_channel() for c in self.dms]
            #wont return dm messages and messages
        }

    def serialize_name(self):
        return{
            'id': self.id,
            'name': self.name
        }


class Channel(db.Model):
    __tablename__='channel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    workspace =  db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False) #relationship one(workspace) to many (channel)
    users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #relationship one (channel) to many (users)
    messages = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False) #relationshipc one(channel) to many (users)
    public = db.Column(db.Boolean, nullable=True) #public or private

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.workspace = kwargs.get('workspace', '')
        self.public = kwargs.get('public', '')

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'workspace': self.workspace.serialize(),
            'public': self.public,
            'users': [a.serialize_name() for a in self.users],
            'messages': [s.serialize(serialize_for_channel() for s in self.messages]
        }

     def serialize_name(self):
         return{
            'id': self.id,
            'name': self.name,
            'description': self.description
         }


class Message(db.Model):
    __tablename__='message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column (db.String, nullable = False)
    timestamp = db.Column (db.String, nullable = False)
    channel = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    thread = db.relationship('Thread', cascade='delete') #relationship one (message) to one (threads)

    def __init__(self, **kwargs):
        self.sender = kwargs.get('sender', '')
        self.content = kwargs.get('content', '')
        self.timestamp = ctime()
        self.channel = kwargs.get('channel', '')

    def serialize(self):
        return{
            'id':self.id,
            'sender':self.sender.serialize_name(),
            'content':self.content,
            'timestamp':self.timestamp,
            'channel':self.channel.serialize_name(),
            'thread' = [a.serialize_for_message() for a in self.threads]
        }

    def serialize_for_thread(self):
        return{
            'id': self.id,
            'sender': self.sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
            'channel': self.channel.serialize()
        }

    def serialize_for_channel(self):
        return{
            'id':self.id,
            'sender':self.sender.serialize_name(),
            'content':self.content,
            'timestamp':self.timestamp,
            'threads' = [a.serialize_for_message() for a in self.threads]
        }


class Thread(db.Model):
    __tablename__='thread'
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column (db.String, nullable = False)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column (db.String, nullable = False)
    message = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False) 

    def __init__(self, **kwargs):
        self.sender = kwargs.get('sender', '')
        self.content = kwargs.get('content', '')
        self.timestamp = ctime()
        self.message = kwargs.get('message', '')

    def serialize(self):
        return{
            'id': self.id,
            'sender': self.sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
            'message': self.message.serialize_for_thread()
        }

     def serialize_for_message(self):
        return{
            'id': self.id,
            'sender': self.sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
        }


class DM(db.Model):
    __tablename__='dm'
    id = db.Column(db.Integer, primary_key = True)
    workspace = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)#relationship one (workspace) to many (dms)
    users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.relationship('Dm_message', cascade='delete')

    def __init__(self, **kwargs):
        self.workspace = kwargs.get('workspace', '')

    def serialize(self):
        return{
            'id': self.id,
            'workspace': self.workspace.serialize_name(),
            'users': [a.serialize_name() for a in self.users],
            'messages': [s.serialize_for_dm() for s in self.messages]
        }

    def serialize_for_dm_message(self):
        return{
            'id': self.id,
            'workspace': self.workspace.serialize_name(),
            'users': [a.serialize_name() for a in self.users]
        }


class Dm_message(db.Model):
    __tablename__='dm_message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column (db.String, nullable = False)
    timestamp = db.Column (db.String, nullable = False)
    dm = db.Column(db.Integer, db.ForeignKey('dm.id'), nullable=False)

    def __init__(self, **kwargs):
        self.content = kwargs.get('content', '')
        self.timestamp = ctime()
        self.dm = kwargs.get('dm', '')

    def serialize(self):
        return{
            'id': self.id,
            'sender': self.sender.serialize_name(),
            'content': self.name,
            'timestamp': self.timestamp,
            'dm': self.dm.serialize_for_dm_messages()
        }

    def serialize_for_dm(self):
        return{
            'id': self.id,
            'sender': self.sender.serialize(),
            'content': self.name,
            'timestamp': self.timestamp
        }
