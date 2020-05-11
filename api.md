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
 **GET** /workspaces/{workspace id}/channels/{channel id}/
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
