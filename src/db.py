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
    users = db.relationship('User', secondary = association_table_userworksp, back_populates='workspaces')
    channels = db.relationship('Channel', cascade = "delete")
    dm_groups = db.relationship('DM', cascade='delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.url = kwargs.get('url', '')

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'url':self.url,
            'users':[a.serialize() for a in self.users],
            'channels':[s.serialize() for s in self.channels],
            'direct messages':[c.serialize() for c in self.dm_groups]
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
    dm_messages = db.relationship('DMmessages', cascade='delete')

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
            'workspaces':[a.serialize() for a in self.workspaces],
            'channels':[s.serialize() for s in self.channels],
            'direct messages':[c.serialize() for c in self.dms]
            #wont return dm messages and messages
        } 



class Channel(db.Model):
    __tablename__='channel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    workspace =  db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False) #relationship one(workspace) to many (channel)
    users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #relationship one (channel) to many (users)
    messages = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False) #relationshipc one(channel) to many (users)
    public = db.Column(db.String, nullable=True) #public or private
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')

     def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'workspace':self.workspace.serialize(),
            'public': self.public,
            'users':[a.serialize() for a in self.users],
            'messages':[s.serialize() for s in self.messags],
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

    def serialize(self):
        return{
            'id':self.id,
            'sender':self.sender.serialize(),
            'content':self.content,
            'timestamp':self.timestamp,
            'channel':self.channel.serialize(),
            'thread' = self.thread.serialize()
        }    
        #add serialize for thread- it wont print the message then
        #add serialze for channel- it wont have channel then


class Thread(db.Model): 
    __tablename__='thread'
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column (db.String, nullable = False)
    content = db.Column (db.String, nullable = False)
    message = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False) #relationship one to one

    def __init__(self, **kwargs):
        self.content = kwargs.get('content', '')

    def serialize(self):
        return{
            'id':self.id,
            'timestamp':self.timestamp,
            'content':self.content,
            'message':self.message.serialize()
        }

           


class DM(db.Model):
    __tablename__='dm'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=True)
    workspace = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)#relationship one (workspace) to many (dms)
    users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.relationship('DMmessage', cascade='delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'woorkspace':self.workspace.serialize(), #just print name instead of serailzing? 
            'users':[a.serialize() for a in self.users], #just print name?
            'messages':[s.serialize() for s in self.messages]
        }

           

class DMmessage(db.Model):
    __tablename__='dm_message'
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column (db.String, nullable = False) 
    timestamp = db.Column (db.String, nullable = False)
    dm = db.Column(db.Integer, db.ForeignKey('dm.id'), nullable=False)

    def __init__(self, **kwargs):
        self.content = kwargs.get('content', '')

    def serialize(self):
        return{
            'id':self.id,
            'sender':self.sender.serialize(),
            'content':self.name,
            'timestamp':self.timestamp,
            'dm':self.dm.serialize()
        }
           

# many: db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
# one: db.relationship('Assignments', cascade='delete')

#how do i write a one to one relationship
#how do i make certain fields optional when initing
