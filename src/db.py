from flask_sqlalchemy import SQLAlchemy
from time import time, ctime
db = SQLAlchemy()

association_table_userworksp = db.Table('association_userworksp', db.Model.metadata,
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_userchannel = db.Table('association_userchannel', db.Model.metadata,
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_userdms = db.Table('association_userdms', db.Model.metadata,
    db.Column('dm_id', db.Integer, db.ForeignKey('dm.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

class Workspace(db.Model):
    __tablename__ = "workspace"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    users = db.relationship('User', secondary = association_table_userworksp, back_populates='workspaces')
    channels = db.relationship('Channel', cascade = 'delete')
    dm_groups = db.relationship('Dm', cascade='delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.url = kwargs.get('url', '')

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'users': [a.serialize_name() for a in self.users],
            'public channels': [s.serialize_name() for s in self.channels],
            'direct messages': [c.serialize_for_dm_message() for c in self.dm_groups]
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
    # channels = db.relationship('Channel', cascade='delete')  #relationship one (user) to many (channels)
    channels = db.relationship('Channel', secondary=association_table_userchannel, back_populates='users')
    messages = db.relationship('Message', cascade='delete') #relationship one (user) to many (dms)
    # dms = db.relationship('DM', cascade='delete') #relationship one (user) to many (dms)
    dms = db.relationship('Dm', secondary=association_table_userdms, back_populates='users')
    dm_messages = db.relationship('Dm_message', cascade='delete')
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
            'direct messages':[c.serialize_for_dm_message() for c in self.dms]
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
    workspace =  db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=True) #relationship one(workspace) to many (channel)
    # users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) #relationship one (channel) to many (users)
    users = db.relationship('User', secondary = association_table_userchannel, back_populates='channels')
    # messages = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=True) #relationshipc one(channel) to many (users)
    messages = db.relationship('Message', cascade='delete')
    public = db.Column(db.Boolean, nullable=True) #public or private

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.workspace = kwargs.get('workspace', '')
        self.public = kwargs.get('public', '')

    def serialize(self):
        workspace = Workspace.query.filter_by(id=self.workspace).first()
        if workspace is None:
            return None
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'workspace': workspace.serialize_name(),
            'public': self.public,
            'users': [a.serialize_name() for a in self.users],
            'messages': [s.serialize_for_channel() for s in self.messages]
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
    threads = db.relationship('Thread', cascade='delete') #relationship one (message) to one (threads)

    def __init__(self, **kwargs):
        self.sender = kwargs.get('sender', '')
        self.content = kwargs.get('content', '')
        self.timestamp = ctime()
        self.channel = kwargs.get('channel', '')

    def serialize(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        channel = Channel.query.filter_by(id=self.channel).first()
        if channel is None:
            return None
        return{
            'id':self.id,
            'sender':sender.serialize_name(),
            'content':self.content,
            'timestamp':self.timestamp,
            'channel':channel.serialize_name(),
            'threads': [a.serialize_for_message() for a in self.threads]
        }

    def serialize_for_thread(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        channel = Channel.query.filter_by(id=self.channel).first()
        if channel is None:
            return None
        return{
            'id': self.id,
            'sender': sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
            'channel': channel.serialize_name()
        }

    def serialize_for_channel(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        return{
            'id':self.id,
            'sender':sender.serialize_name(),
            'content':self.content,
            'timestamp':self.timestamp,
            'threads': [a.serialize_for_message() for a in self.threads]
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
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        message = Message.query.filter_by(id=self.message).first()
        if message is None:
            return None
        return{
            'id': self.id,
            'sender': sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
            'message': message.serialize_for_thread()
        }

    def serialize_for_message(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        return{
            'id': self.id,
            'sender': sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp
        }


class Dm(db.Model):
    __tablename__='dm'
    id = db.Column(db.Integer, primary_key = True)
    workspace = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)#relationship one (workspace) to many (dms)
    # users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # users = db.relationship('User', secondary = association_table_userdms, back_populates='dms')
    users = db.relationship('User', secondary = association_table_userdms, back_populates='dms')
    messages = db.relationship('Dm_message', cascade='delete')
 
    def __init__(self, **kwargs):
        self.workspace = kwargs.get('workspace', '')

    def serialize(self):
        workspace = Workspace.query.filter_by(id=self.workspace).first()
        if workspace is None:
            return None
        return{
            'id': self.id,
            'workspace': workspace.serialize_name(),
            'users': [a.serialize_name() for a in self.users],
            'messages': [s.serialize_for_dm() for s in self.messages]
        }

    def serialize_for_dm_message(self):
        workspace = Workspace.query.filter_by(id=self.workspace).first()
        if workspace is None:
            return None
        return{
            'id': self.id,
            'workspace': workspace.serialize_name(),
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
        self.sender = kwargs.get('sender', '')
        self.content = kwargs.get('content', '')
        self.timestamp = ctime()
        self.dm = kwargs.get('dm', '')

    def serialize(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        dm = Dm.query.filter_by(id=self.dm).first()
        if dm is None:
            return None
        return{
            'id': self.id,
            'sender': sender.serialize_name(),
            'content': self.content,
            'timestamp': self.timestamp,
            'dm': dm.serialize_for_dm_message()
        }

    def serialize_for_dm(self):
        sender = User.query.filter_by(id=self.sender).first()
        if sender is None:
            return None
        return{
            'id': self.id,
            'sender': sender.serialize(),
            'content': self.content,
            'timestamp': self.timestamp
        }
