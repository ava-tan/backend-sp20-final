from db import db, Workspace, User, Channel, Message, Thread, DM, DMmessage

# WORKSPACE
def get_all_workspaces():
    return [w.serialize() for w in Workspace.query.all()]

def create_workspace(name, url):
    new_workspace = Workspace(
        name = name,
        url = url
    )
    db.session.add(new_workspace)
    db.session.commit()
    return new_workspace.serialize()

def get_workspace_by_id(workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    return workspace.serialize()

def update_workspace_by_id(workspace_id, body):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    workspace.name = body.get("name", workspace.name)
    workspace.url = body.get("url", workspace.url)
    db.session.commit()
    return workspace.serialize()

def delete_workspace_by_id(workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    db.session.delete(workspace)
    db.session.commit()
    return workspace.serialize()

# USER
def get_all_users():
    return [u.serialize() for u in User.query.all()]

def create_user(name, email, status, active, do_not_disturb):
    new_user = User(
        name = name,
        email = email,
        status = status,
        active = active,
        do_not_disturb = do_not_disturb
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def update_user_by_id(user_id, body):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    user.name = body.get("name", user.name)
    user.email = body.get("email", user.email)
    user.status = body.get("status", user.status)
    user.active = body.get("active", user.active)
    user.do_not_disturb = body.get("do_not_disturb", user.do_not_disturb)
    db.session.commit()
    return user.serialize()

def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def add_user_to_workspace(user_id, workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    workspace.users.append(user)
    db.session.commit()
    return workspace.serialize()

def add_user_to_channel(user_id, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    channel.users.append(user)
    db.session.commit()
    return channel.serialize()

def add_user_to_DM(user_id, dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    dm.users.append(user)
    db.session.commit()
    return dm.serialize()

def remove_user_from_channel(user_id, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    channel.users.remove(user)
    db.session.commit()
    return channel.serialize()

# CHANNEL
def get_all_channels():
    return [c.serialize() for c in Channel.query.all()]

def get_channels_in_workspace(workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    return [c.serialize() for c in workspace.channels]

# Return all channels that user is in within a specific workspace
def get_channels_of_user_in_workspace(user_id, workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    user = User.query.filter_by(id=user_id).first()
    if user or workspace is None:
        return None
    user_channels = []
    for c in workspace.channels:
        if user in channels_in_workspace:
            user_channels.append(c)
    return [ch.serialize for ch in user_channels]

# If channel is public, add all members of workspace to this channel when channel is created
def create_channel(name, description, workspace_id, public):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    new_channel = Channel(
        name = name,
        description = description,
        workspace_id = workspace_id,
        public = public
    )
    db.session.add(new_channel)
    if new_channel.public == True:
        for u in workspace.users:
            new_channel.users.append(u)
    db.session.commit()
    return new_channel.serialize()

def get_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    return channel.serialize()

def update_channel_by_id(channel_id, body):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    channel.name = body.get("name", channel.name)
    channel.description = body.get("description", channel.description)
    db.session.commit()
    return channel.serialize()

def delete_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    db.session.delete(channel)
    db.session.commit()
    return channel.serialize()

# MESSAGE
def get_all_messages():
    return [m.serialize() for m in Message.query.all()]

def get_messages_in_channel(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    return [m.serialize() for m in channel.messages]

def get_messages_sent_by_user(user_id):
    user = User.query.filter_by(id=user.id).first()
    if user is None:
        return None
    return [m.serialize() for m in user.messages]

def create_message(sender_id, content, channel_id, ):
    new_message = Message(

    )

def update_message_by_id(message_id, body):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    message.content = body.get("content", message.content)
    db.session.commit()
    return message.serialize()

def delete_message_by_id(message_id):
