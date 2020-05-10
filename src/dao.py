from db import db, Workspace, User, Channel, Message, Thread, DM, DMmessage

# Workspace methods
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

def update_workspace_by_id(workspace_id):
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

# User methods
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

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def update_user_by_id(user_id, name, email, status, active, do_not_disturb):
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

# Channel methods
def get_all_channels():
    return [c.serialize() for c in Channel.query.all()]

def get_channels_of_workspace(workspace_id):
    workspace = Workspace.query.filter_by(id=workspace_id).first()
    if workspace is None:
        return None
    return [c.serialize() for c in workspace.channels]

def create_channel(name, description, workspace_id, public):
    new_channel = Channel(
        name = name,
        description = description,
        workspace_id = workspace_id,
        public = public
    )
    db.session.add(new_channel)
    db.session.commit()
    return new_channel.serialize()

def get_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    return channel.serialize()

def delete_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    db.session.delete(channel)
    db.session.commit()
    return channel.serialize()
