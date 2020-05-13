# API Specification
## **Get a specific workspace**
 **GET** /workspaces/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
         "channels": [ <SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
     }
 }
```

## **Get all workspaces of a user**
 **GET** /user/{user id}/workspaces/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>,
               "url": <USER INPUT FOR URL>,
               "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
               "channels": [ <SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
         }
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>,
               "url": <USER INPUT FOR URL>,
               "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
               "channels": [ <SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
         }
         ...
     ]
 }
```

## **Create a workspace**
 **POST** /workspaces/
 ###### Request
 ```yaml
 {
     "name": <USER INPUT>,
     "url": <USER INPUT>      
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [],
         "channels": [],
         "direct messages": []
     }
 }
```

## **Update a workspace**
 **POST** /workspaces/{id}/
 ###### Request
```yaml
 {
     "name": <USER INPUT FOR NAME>,
     "url": <USER INPUT FOR URL>      
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [],
         "channels": [],
     }
 }
```

## **Add user to a workspace**
 **POST** /workspaces/{id}/users/add/
 ###### Request
```yaml
 {
     "user_id": <USER INPUT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": <SERIALIZED WORKSPACE>
 }
```

## **Delete a specific workspace**
 **DELETE** /workspaces/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
         "channels": [ <SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
     }
 }
```

## **Get a specific user**
 **GET** /users/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "email": <USER INPUT FOR EMAIL>,
         "status": <USER INPUT FOR STATUS>,
         "active": <USER INPUT FOR ACTIVE>,
         "do_not_disturb": <USER INPUT FOR DO NOT DISTURB>,
         "workspaces": [ <SERIALIZED WORKSPACE>, ... ]
     }
 }
```

## **Create a user**
 **POST** /users/
  ###### Request
```yaml
 {
     "name": <USER INPUT FOR NAME>,
     "email": <USER INPUT FOR EMAIL>,
     "status": <USER INPUT FOR STATUS>,
     "active": true or false,
     "do_not_disturb": true or false
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "email": <USER INPUT FOR URL>,
         "status": <USER INPUT FOR STATUS>,
         "active": <USER INPUT FOR ACTIVE>,
         "do_not_disturb": <USER INPUT FOR DO NOT DISTURB>,
         "workspaces": [],
         "channels": [],
         "direct messages": []
     }
 }
```

## **Edit a user**
 **POST** /users/{id}/
  ###### Request
```yaml
 {
     "name": <USER INPUT FOR NAME (OPTIONAL)>,
     "email": <USER INPUT FOR EMAIL (OPTIONAL)>,
     "status": <USER INPUT FOR STATUS (OPTIONAL)>,
     "active": true or false (OPTIONAL),
     "do_not_disturb": true or false (OPTIONAL)
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "email": <USER INPUT FOR URL>,
         "status": <USER INPUT FOR STATUS>,
         "active": <USER INPUT FOR ACTIVE>,
         "do_not_disturb": <USER INPUT FOR DO NOT DISTURB>,
         "workspaces": [ <SERIALIZED WORKSPACE>, ... ],
         "channels": [ <SERIALIZED CHANNEL>, ... ],
         "direct messages": [ <SERIALIZED DM>, ... ]
     }
 }
```

## **Delete a specific user**
 **DELETE** /users/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "email": <USER INPUT FOR EMAIL>,
         "status": <USER INPUT FOR STATUS>,
         "active": <USER INPUT FOR ACTIVE>,
         "do_not_disturb": <USER INPUT FOR DO NOT DISTURB>,
         "workspaces": [ <SERIALIZED WORKSPACE>, ... ]
     }
 }
```

## **Get all channels of a workspace**
 **GET** /workspaces/{id}/channels/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>
         }
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>
         }
         ...
     ]
 }
```

## **Get all channels of a workspace viewable by a user**
 **GET** /user/{user id}/workspaces/{workspace id}/channels/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>
         }
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>
         }
         ...
     ]
 }
```

## **Get a specific channel**
 **GET** /channels/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "workspace": <SERIALIZED WORKSPACE>,
         "public": <USER INPUT FOR PUBLIC>,
         "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
         "messages": [ <SERIALIZED MESSAGE WITHOUT CHANNEL FIELD>, ... ]
     }
 }
```

## **Create a channel**
 **POST** /workspaces/{id}/channels/
  ###### Request
```yaml
 {
     "name": <USER INPUT FOR NAME>,
     "description": <USER INPUT FOR DESCRIPTION (OPTIONAL)>,
     "public": true or false
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "workspace": <SERIALIZED WORKSPACE>,
         "public": <USER INPUT FOR PUBLIC>,
         "users": [],
         "messages": []
     }
 }
```

## **Update a channel**
 **POST** /channels/{id}/
 ###### Request
```yaml
 {
     "name": <USER INPUT FOR NAME (OPTIONAL)>,
     "description": <USER INPUT FOR DESCRIPTION (OPTIONAL)>      
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "workspace": <SERIALIZED WORKSPACE>,
         "public": <USER INPUT FOR PUBLIC>,
         "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
         "messages": [ <SERIALIZED MESSAGE WITHOUT CHANNEL FIELD>, , ... ]
     }
 }
```

## **Add user to a channel**
 **POST** /channels/{id}/users/add/
 ###### Request
```yaml
 {
     "user_id": <USER INPUT FOR USER ID>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": <SERIALIZED CHANNEL>
 }
```

## **Remove user from a channel**
 **DELETE** /channels/{user id}/users/{user id}
###### Response
 ```yaml
 {
     "success": true,
     "data": <SERIALIZED CHANNEL>
 }
```

## **Delete a specific channel**
 **DELETE** /channels/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "workspace": <SERIALIZED WORKSPACE>,
         "public": <USER INPUT FOR PUBLIC>,
         "users": [ <SERIALIZED USER WITH JUST NAME>, ... ],
         "messages": [ <SERIALIZED MESSAGE WITHOUT CHANNEL FIELD>, ... ]
     }
 }
```

## **Get all messages of a channel**
 **GET** /channels/{id}/messages/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>,
               "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
         }
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>,
               "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
         }
         ...
     ]
 }
```

## **Get all messages sent by a user**
 **GET** /users/{id}/messages/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>,
               "channel": <SERIALIZED COURSE WITH NAME AND DESCRIPTION>,
               "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
         }
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>,
               "channel": <SERIALIZED COURSE WITH JUST NAME AND DESCRIPTION>,
               "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
         }
         ...
     ]
 }
```

## **Create a message**
 **POST** /channels/{id}/messages/
  ###### Request
```yaml
 {
     "sender": <USER INPUT FOR SENDER ID>,
     "content": <USER INPUT FOR CONTENT>
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "channel": <SERIALIZED CHANNEL WITH NAME AND DESCRIPTION>,
         "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
     }
 }
```

## **Update a message**
 **POST** /messages/{id}/
 ###### Request
```yaml
 {
     "content": <USER INPUT FOR CONTENT>      
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "channel": <SERIALIZED CHANNEL WITH NAME AND DESCRIPTION>,
         "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
     }
 }
```

## **Delete a specific message**
 **DELETE** /messages/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
          "id": <ID>,
          "sender": <USER INPUT FOR SENDER ID>,
          "content": <USER INPUT FOR CONTENT>,
          "timestamp": <TIME WHEN MESSAGE SENT>,
          "channel": <SERIALIZED COURSE WITH JUST NAME AND DESCRIPTION>,
          "threads": [ <SERIALIZED THREAD WITHOUT MESSAGE FIELD>, ... ]
     }
 }
```

## **Get all threads of a message**
 **GET** /messages/{id}/threads/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>
         }
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>
         }
         ...
     ]
 }
```

## **Get a specific thread**
 **GET** /threads/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <TIME WHEN THREAD CREATED>,
         "message": <SERIALIZED MESSAGE WITHOUT THREAD FIELD>
     }
 }
```

## **Create a thread message**
 **POST** /messages/{id}/threads/
  ###### Request
```yaml
 {
     "sender": <USER INPUT FOR SENDER ID>,
     "content": <USER INPUT FOR CONTENT>
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "message": <SERIALIZED MESSAGE WITHOUT THREAD FIELD>
     }
 }
```

## **Update a thread**
 **POST** /threads/{id}/
 ###### Request
```yaml
 {
     "content": <USER INPUT FOR CONTENT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "message": <SERIALIZED MESSAGE WITHOUT THREAD FIELD>
     }
 }
```

## **Delete a specific thread**
 **DELETE** /threads/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <TIME WHEN THREAD CREATED>,
         "message": <SERIALIZED MESSAGE WITHOUT THREAD FIELD>
     }
 }
```

## **Get all DMs of a workspace viewable by a user**
 **GET** /user/{user id}/workspaces/{workspace id}/dms/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "workspace": <USER INPUT FOR WORKSPACE ID>,
               "users": [ <SERIALIZED USER WITH ONLY ID AND NAME>, ... ]
               "messages": [ <SERIALIZED DM_MESSAGE WITHOUT DM FIELD>, ... ]
         }
         {
               "id": <ID>,
               "workspace": <USER INPUT FOR WORKSPACE ID>,
               "users": [ <SERIALIZED USER WITH ONLY ID AND NAME>, ... ]
               "messages": [ <SERIALIZED DM_MESSAGE WITHOUT DM FIELD>, ... ]
         }
         ...
     ]
 }
```

## **Get a specific DM group**
 **GET** /dms/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "workspace": <USER INPUT FOR WORKSPACE ID>,
         "users": [ <SERIALIZED USER WITH ONLY ID AND NAME>, ... ]
         "messages": [ <SERIALIZED DM_MESSAGE WITHOUT DM FIELD>, ... ]
     }
 }
```

## **Create a DM group**
 **POST** /workspaces/{workspace id}/users/{user id}/dms/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "workspace": <USER INPUT FOR WORKSPACE ID>,
         "users": [ <SERIALIZED USER WITH ONLY ID AND NAME> ] #only include user who created DM
         "messages": []
     }
 }
```

## **Add user to a DM group**
 **POST** /dms/{id}/users/add/
 ###### Request
```yaml
 {
     "user_id": <USER INPUT FOR USER ID>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": <SERIALIZED DM>
 }
```

## **Delete a specific DM group**
 **DELETE** /dms/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "workspace": <USER INPUT FOR WORKSPACE ID>,
         "users": [ <SERIALIZED USER WITH ONLY ID AND NAME>, ... ]
         "messages": [ <SERIALIZED DM_MESSAGE WITHOUT DM FIELD>, ... ]
     }
 }
```

## **Get all DM messages in a DM Group**
 **GET** /dms/{id}/dm-messages/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>
         }
         {
               "id": <ID>,
               "sender": <USER INPUT FOR SENDER ID>,
               "content": <USER INPUT FOR CONTENT>,
               "timestamp": <TIME WHEN MESSAGE SENT>
         }
         ...
     ]
 }
```

## **Create a DM message**
 **POST** /dms/{id}/dm-messages/
  ###### Request
```yaml
 {
     "sender": <USER INPUT FOR SENDER ID>,
     "content": <USER INPUT FOR CONTENT>
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "dm": <SERIALIZED DM WITHOUT MESSAGES FIELD>
     }
 }
```

## **Update a message**
 **POST** /dm-messages/{id}/
 ###### Request
```yaml
 {
     "content": <USER INPUT FOR CONTENT>      
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <NOW>,
         "dm": <SERIALIZED DM WITHOUT MESSAGES FIELD>
     }
 }
```

## **Delete a specific DM message**
 **DELETE** /dm-messages/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "sender": <USER INPUT FOR SENDER ID>,
         "content": <USER INPUT FOR CONTENT>,
         "timestamp": <TIME WHEN MESSAGE SENT>,
         "dm": <SERIALIZED DM WITHOUT MESSAGES FIELD>
     }
 }
```
