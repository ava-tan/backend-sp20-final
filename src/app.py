import json
from flask import Flask, request
import dao
import os
from db import db, Workspace, User, Channel, Message, Thread, DM, Dm_message

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

######################################################################################################

@app.route('/workspaces/', methods=['GET'])
def get_all_workspace():
    return success_response(dao.get_all_workspaces())

@app.route('/workspaces/<int:workspace_id>/', methods=['GET'])
def get_workspace_by_id(workspace_id):
    workspace = dao.get_workspace_by_id(workspace_id)
    if workspace is None:
        return failure_response("Workspace not found!")
    return success_response(workspace)

@app.route('/workspaces/', methods=['POST'])
def create_workspace():
    body = json.loads(request.data)
    workspace = dao.create_user(
        name=body.get('name'),
        url=body.get('url')
    )
    return success_response(workspace)

@app.route('/workspaces/<int:workspace_id>/', methods=['POST'])
def update_workspace_by_id(workspace_id):
    body = json.loads(request.data)
    workspace = update_workspace_by_id(workspace_id, body)
    if workspace is None:
         return failure_response("Workspace not found!")
    return success_response(workspace)

@app.route('/workspaces/<int:workspace_id>/add/', methods=['POST'])
def add_user_to_workspace(workspace_id):
    body = json.loads(request.data)
    workspace = dao.add_user_to_workspace(
        user_id=body.get('user_id'),
        workspace_id=workspace_id
    )
    if workspace is None:
        return failure_response("Cannot add user to workspace!")
    return success_response(workspace)


@app.route('/workspaces/<int:workspace_id>/', methods=['DELETE'])
def delete_workspace(workspace_id):
    workspace = dao.delete_workspace_by_id(workspace_id)
    if workspace is None:
         return failure_response("Workspace not found!")
    return success_response(workspace)

######################################################################################################

@app.route('/users/', methods=['GET'])
def get_all_users():
    return success_response(dao.get_all_users())

@app.route('/users/<int:user_id>/', methods=['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if workspace is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name=body.get('name'),
        email=body.get('email'),
        status = body.get('status'),
        active = body.get('active'),
        do_not_disturb = body.get('do_not_disturb')
    )
    return success_response(user)
    
@app.route('/users/<int:user_id>/', methods=['POST'])
def update_user_by_id(user_id):
    body = json.loads(request.data)
    user = update_user_by_id(user_id, body)
    if workspace is None:
         return failure_response("Workspace not found!")
    return success_response(workspace)

@app.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user= delete_user_by_id(user_id)
    if workspace is None:
         return failure_response("User not found!")
    return success_response(user)

######################################################################################################
@app.route('/channels/', methods=['GET'])
def get_all_channels(channel_id):
    return success_response(dao.get_all_channels())

@app.route('/workspaces/<int:workspace_id>/channels/', methods=['GET'])
def get_all_channels_of_workspace(workspace_id):
    channels = get_channels_in_workspace(workspace_id)
    if channels is None:
         return failure_response("Workspace not found!")
    return success_response(channels)

@app.route('/user/<int:user_id>/workspaces/<int:workspace_id>/channels/', methods=['GET'])
def get_all_channels_of_workspace_viewable_by_user(workspace_id, user_id):
    channels = get_channels_of_user_in_workspace(user_id, workspace_id)
    if channels is None:
         return failure_response("Unable to get channels of user in this workspace")
    return success_response(channels)

@app.route('/channels/<int:channel_id>', methods=['GET'])
def get_channel_by_id(channel_id):
    channel = dao.get_channel_by_id(channel_id)
    if workspace is None:
        return failure_response("User not found!")
    return success_response(user)


@app.route('/workspaces/<int:workspace_id>/channels/', methods=['POST'])
def create_channel():
    body = json.loads(request.data)
    channel = dao.create_channel(
        name=body.get('name'),
        description=body.get('description'),
        public = body.get('public')
    )
    return success_response(user)

@app.route('/channels/<int:channel_id>/', methods=['POST'])
def update_channel_by_id(channel_id):
    body = json.loads(request.data)
    channel = update_user_by_id(channel_id, body)
    if channel is None:
         return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/workspaces/<int:workspace_id>/channels/add/', methods=['POST'])
def add_user_to_channel(channel_id):
    body = json.loads(request.data)
    channel = dao.add_user_to_channel(
        user_id=body.get('user_id'),
        channel_id=channel_id
    )
    if channel is None:
        return failure_response("Cannot add user to channel!")
    return success_response(channel)

@app.route('/channels/<int:channel_id>/user/<int:user_id>', methods=['DELETE'])
def remove_user_from_channel(channel_id, user_id):
    channel = remove_user_from_channel(user_id, channel_id)
    if channel is None:
         return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/channels/<int:channel_id>/', methods=['DELETE'])
def delete_channel_by_id(channel_id)):
    channel= delete_channel_by_id(channel_id)
    if workspace is None:
         return failure_response("Channel not found!")
    return success_response(channel)

######################################################################################################

# def get_all_messages():

# def get_messages_in_channel(channel_id):

# def get_messages_sent_by_user(user_id):

# def create_message():


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
