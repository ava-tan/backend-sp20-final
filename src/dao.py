from db import db, Workspace, User, Channel, Message, Thread, DM, Dm_message
from time import time, ctime

# WORKSPACE
def get_all_workspaces():
    return [w.serialize() for w in Workspace.query.all()]

def get_workspaces_of_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [w.serialize() for w in user.workspaces]

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

def add_user_to_workspace(user_id, workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    workspace.users.append(user)
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

def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

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
        if user in c.users:
            user_channels.append(c)
    return [ch.serialize() for ch in user_channels]

# If channel is public, add all members of workspace to this channel when channel is created
def create_channel(name, description, workspace_id, public):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    new_channel = Channel(
        name = name,
        description = description,
        workspace = workspace_id,
        public = public
    )
    db.session.add(new_channel)
    if new_channel.public == True:
        for u in workspace.users:
            new_channel.users.append(u)
    workspace.channels.append(new_channel)
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

def add_user_to_channel(user_id, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    channel.users.append(user)
    db.session.commit()
    return channel.serialize()

def remove_user_from_channel(user_id, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    channel.users.remove(user)
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

def get_message_by_id(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    return message.serialize()

def create_message(sender_id, content, channel_id):
    new_message = Message(
        sender = sender_id,
        content = content,
        channel = channel_id
    )
    db.session.add(new_message)
    db.session.commit()
    return new_message.serialize()

def update_message_by_id(message_id, body):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    message.content = body.get("content", message.content)
    message.timestamp = ctime()
    db.session.commit()
    return message.serialize()

def delete_message_by_id(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    db.session.delete(message)
    db.session.commit()
    return message.serialize()

# THREAD
def get_all_threads():
    return [t.serialize() for t in Thread.query.all()]

def get_all_threads_of_message(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    return [t.serialize_for_message() for t in messages.threads]

def get_thread_by_id(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    if thread is None:
        return None
    return thread.serialize()

def create_thread(sender_id, content, message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    new_thread = Thread(
        sender = sender_id,
        content = content,
        message = message_id
    )
    db.session.add(new_thread)
    message.threads.append(new_thread)
    db.session.commit()
    return new_thread.serialize()


def update_thread_by_id(thread_id, body):
    thread = Thread.query.filter_by(id=thread_id).first()
    if thread is None:
        return None
    thread.content = body.get("content", thread.content)
    thread.timestamp = ctime()
    db.session.commit()
    return thread.serialize()

def delete_thread_by_id(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    if thread is None:
        return None
    db.session.delete(thread)
    db.session.commit()
    return thread.serialize()

# DM
def get_all_dms():
    return [d.serialize() for d in DM.query.all()]

def get_dms_of_user_in_workspace(user_id, workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    user = User.query.filter_by(id=user_id).first()
    if user or workspace is None:
        return None
    user_dms = []
    for d in workspace.dm_groups:
        if user in d.users:
            user_dms.append(d)
    return [dm.serialize() for dm in user_dms]

def get_dm_by_id(dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    return dm.serialize()

def create_dm(workspace_id, user_id):
    new_dm = DM(
        workspace = workspace_id
    )
    db.session.add(new_dm)
    db.session.commit()
    new_dm.serialize()
    add_user_to_DM(new_dm.id, user_id)

def add_user_to_DM(user_id, dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    dm.users.append(user)
    db.session.commit()
    return dm.serialize()

def delete_dm(dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    db.session.delete(dm)
    db.session.commit()
    return dm.serialize()

# DM Messages
def get_all_dm_messages():
    return [d.serialize() for d in Dm_message.query.all()]

def get_all_dm_messages_in_dm(dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    return [d.serialize_for_dm() for d in dm.messages]

def create_dm_message(sender_id, content, dm_id):
    new_dm_message = Dm_message(
        sender = sender_id,
        content = content,
        dm = dm_id
    )
    db.session.add(new_dm_message)
    db.session.commit()
    return new_dm_message.serialize()

def update_dm_message_by_id(dm_message_id, body):
    dm_message = Dm_message.query.filter_by(id=dm_message_id).first()
    if dm_message is None:
        return None
    dm_message.content = boyd.get("content", dm_message.content)
    dm_message.timestamp = ctime()
    db.session.commit()
    return dm_message.serialize()

def delete_dm_message_by_id(dm_message_id):
    dm_message = Dm_message.query.filter_by(id=dm_message_id).first()
    if dm_message is None:
        return None
    db.session.delete(dm_message)
    db.session.commit()
    return dm_message.serialize()
