from db import db, Workspace, User, Channel, Message, Thread, DM, DMmessage

# Workspace
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

def get_workspace_by_url(workspace_url):
    workspace = Workspace.query.filter_by(url=workspace_url).first()
    if workspace is None:
        return None
    return workspace.serialize()

def delete_workspace_by_url(workspace_url):
    workspace = Workspace.query.filter_by(url=workspace_url).first()
    if workspace is None:
        return None
    db.session.delete(workspace)
    db.session.commit()
    return workspace.serialize()

# User
def get_all_users():
    return [u.serialize() for u in User.query.all()]

def create_user(name, email, status, active, do_not_disturb):
    new_user = User(
        name = name,
        email = email,
        status = active,
        do_not_disturb = do_not_disturb
    )

def delete_user(email):
    user = User.query.filter_by(email=user_email).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def add_user_to_workspace(email, workspace_url):
    workspace = Workspace.query.filter_by(url=workspace_url).first()
    if workspace is None:
        return None
    user = User.query.filter_by(email=email).first()
    workspace.users.append(user)
    db.session.commit()
    return workspace.serialize()

def add_user_to_channel(email, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(email=email).first()
    channel.users.append(user)
    db.session.commit()
    return channel.serialize()

def add_user_to_DM(email, dm_id):
    dm = DM.query.filter_by(id=dm_id).first()
    if dm is None:
        return None
    user = User.query.filter_by(email=email).first()
    dm.users.append(user)
    db.session.commit()
    return dm.serialize()

def remove_user_from_channel(email, channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(email=email).first()
    channel.users.remove(user)
    db.session.commit()
    return channel.serialize()

# Channel
def get_all_channels():
    return [c.serialize() for c in Channel.query.all()]

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
    db.session.delete(workspace)
    db.session.commit()
    return channel.serialize()