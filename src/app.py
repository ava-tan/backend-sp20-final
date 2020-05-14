import json
from flask import Flask, request
import dao
import os
from db import db, Workspace, User, Channel, Message, Thread, Dm, Dm_message

app = Flask(__name__)
db_filename = "slack.db"

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

@app.route('/')
def hello_world():
    return ("Hello World!")

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

@app.route('/users/<int:user_id>/workspaces/', methods=['GET'])
def get_workspaces_of_user(user_id):
    workspaces = dao.get_workspaces_of_user(user_id)
    if workspaces is None:
         return failure_response("User not found!")
    return success_response(workspaces)

@app.route('/workspaces/', methods=['POST'])
def create_workspace():
    body = json.loads(request.data)
    workspace = dao.create_workspace(
        name=body.get('name'),
        url=body.get('url')
    )
    return success_response(workspace)

@app.route('/workspaces/<int:workspace_id>/', methods=['POST'])
def update_workspace_by_id(workspace_id):
    body = json.loads(request.data)
    workspace = dao.update_workspace_by_id(workspace_id, body)
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
    if user is None:
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
    user = dao.update_user_by_id(user_id, body)
    if user is None:
         return failure_response("Workspace not found!")
    return success_response(user)

@app.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user= dao.delete_user_by_id(user_id)
    if user is None:
         return failure_response("User not found!")
    return success_response(user)

######################################################################################################
@app.route('/channels/', methods=['GET'])
def get_all_channels():
    return success_response(dao.get_all_channels())

@app.route('/workspaces/<int:workspace_id>/channels/', methods=['GET'])
def get_all_channels_of_workspace(workspace_id):
    channels = dao.get_channels_in_workspace(workspace_id)
    if channels is None:
         return failure_response("Workspace not found!")
    return success_response(channels)

@app.route('/user/<int:user_id>/workspaces/<int:workspace_id>/channels/', methods=['GET'])
def get_all_channels_of_workspace_viewable_by_user(workspace_id, user_id):
    channels = dao.get_channels_of_user_in_workspace(user_id, workspace_id)
    if channels is None:
         return failure_response("Unable to get channels of user in this workspace")
    return success_response(channels)

@app.route('/channels/<int:channel_id>/', methods=['GET'])
def get_channel_by_id(channel_id):
    channel = dao.get_channel_by_id(channel_id)
    if channel is None:
        return failure_response("Channel not found!")
    return success_response(channel)


@app.route('/workspaces/<int:id>/channels/', methods=['POST'])
def create_channel(id):
    body = json.loads(request.data)
    # channel = dao.create_channel(
    #     name=body.get('name'),
    #     description=body.get('description'),
    #     workspace_id = id,
    #     public = body.get('public')
    # )
    channel = dao.create_channel(body.get('name'),body.get('description'),id,body.get('public'))
    return success_response(channel)

@app.route('/channels/<int:channel_id>/', methods=['POST'])
def update_channel_by_id(channel_id):
    body = json.loads(request.data)
    channel = dao.update_user_by_id(channel_id, body)
    if channel is None:
         return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/channels/<int:channel_id>/add/', methods=['POST'])
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
    channel = dao.remove_user_from_channel(user_id, channel_id)
    if channel is None:
         return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/channels/<int:channel_id>/', methods=['DELETE'])
def delete_channel_by_id(channel_id):
    channel= dao.delete_channel_by_id(channel_id)
    if channel is None:
         return failure_response("Channel not found!")
    return success_response(channel)

######################################################################################################

@app.route('/messages/', methods=['GET'])
def get_all_messages():
    return success_response(dao.get_all_messages())

@app.route('/channels/<int:channel_id>/messages/', methods=['GET'])
def get_messages_in_channel(channel_id):
    messages = dao.get_messages_in_channel(channel_id)
    if messages is None:
         return failure_response("Channel not found!")
    return success_response(messages)

@app.route('/users/<int:user_id>/messages/', methods=['GET'])
def get_messages_sent_by_user(user_id):
    messages = dao.get_messages_sent_by_user(user_id)
    if messages is None:
         return failure_response("User not found!")
    return success_response(messages)

@app.route('/channels/<int:id>/messages/', methods=['POST'])
def create_message(id):
    body = json.loads(request.data)
    message = dao.create_message(
        sender_id=body.get('sender'),
        content = body.get('content'),
        channel_id=id
    )
    return success_response(message)

@app.route('/messages/<int:message_id>/', methods=['POST'])
def update_message_by_id(message_id):
    body = json.loads(request.data)
    message = dao.update_message_by_id(message_id, body)
    if message is None:
         return failure_response("Message not found!")
    return success_response(message)

@app.route('/messages/<int:message_id>/', methods=['DELETE'])
def delete_message(message_id):
    message = dao.delete_message_by_id(message_id)
    if message is None:
         return failure_response("Message not found!")
    return success_response(message)

######################################################################################################

@app.route('/threads/', methods=['GET'])
def get_all_threads():
    return success_response(dao.get_all_dms())

@app.route('/messages/<int:message_id>/threads/', methods=['GET'])
def get_threads_of_message(message_id):
    threads = dao.get_threads_of_message(thread_id)
    if thread is None:
        return failure_response("Message not found!")
    return success_response(threads)

@app.route('/threads/<int:thread_id>/', methods=['GET'])
def get_thread_by_id(thread_id):
    thread = dao.get_thread_by_id(thread_id)
    if thread is None:
        return failure_response("Thread not found!")
    return success_response(thread)

@app.route('/messages/<int:message_id>/threads/', methods=['GET'])
def create_thread(message_id):
    body = json.loads(request.data)
    thread = dao.create_thread(
        sender=body.get('sender'),
        content = content,
        message=message_id
    )
    return success_response(thread)

@app.route('/threads/<int:thread_id>/', methods=['POST'])
def update_thread(thread_id):
    body = json.loads(request.data)
    thread = dao.update_thread_by_id(thread_id, body.get('content'))
    if thread is None:
         return failure_response("Thread not found!")
    return success_response(thread)

@app.route('/threads/<int:thread_id>/', methods=['DELETE'])
def delete_thread(thread_id):
    thread= dao.delete_thread_by_id(thread_id)
    if thread is None:
         return failure_response("Thread not found!")
    return success_response(thread)

######################################################################################################

@app.route('/dms/', methods=['GET'])
def get_all_dms():
    return success_response(dao.get_all_dms())

@app.route('/dms/<int:dm_id>/', methods=['GET'])
def get_dm_by_id():
    dm = dao.get_dm_by_id(dm_id)
    if dm_message is None:
        return failure_response("DM not found!")
    return success_response(dm_message)

@app.route('/workspaces/<int:workspace_id>/users/<int:user_id>/dms/', methods=['POST'])
def create_dm(workspace_id, user_id):
    dm = dao.create_dm(workspace_id, user_id)
    return success_response(dm)

@app.route('/dms/<int:dm_id>/users/add', methods=['POST'])
def add_member_to_dm(dm_id):
    body = json.loads(request.data)
    dm = dao.add_user_to_channel(
        user_id=body.get('user_id'),
        dm_id=dm_id
    )
    if dm is None:
        return failure_response("Cannot add user to dm!")
    return success_response(dm)

@app.route('/dms/<int:dm_id>/', methods=['DELETE'])
def delete_dm(dm_id):
    dm= dao.delete_dm(dm_id)
    if dm is None:
         return failure_response("DM not found!")
    return success_response(dm)

######################################################################################################

@app.route('/dms/<int:dm_id>/', methods=['GET'])
def get_all_dm_messages():
    return success_response(dao.get_all_dm_messages())

@app.route('/dms/<int:dm_id>/dm-messages/dm-messages/', methods=['GET'])
def get_all_dmmessages_in_dm():
    dm_message = dao.get_dm_messages_by_id(dm_id)
    if dm_message is None:
        return failure_response("DM not found!")
    return success_response(dm_message)

@app.route('/dms/<int:dm_id>dm-messages/', methods=['POST'])
def create_dmmessage(dm_id):
    body = json.loads(request.data)
    dm_message = dao.create_dm_message(
        sender_id=body.get('sender_id'),
        content=body.get('description'),
        dm_id = dm_id
    )
    return success_response(dm_message)

@app.route('/dm-messages/<int:dm_message_id>/', methods=['POST'])
def update_dmmessage(dmmessage_id):
    body = json.loads(request.data)
    dm_message = dao.update_dm_message_by_id(dm_message_id, body)
    if dm_message is None:
         return failure_response("DM not found!")
    return success_response(dm_message)

@app.route('/dm-messages/<int:dm_message_id>/', methods=[''])
def delete_dmmessage(dm_message_id):
    dm_message= dao.delete_dm_message_by_id(dm_message_id)
    if dm_message is None:
         return failure_response("DM not found!")
    return success_response(dm_message)
######################################################################################################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
