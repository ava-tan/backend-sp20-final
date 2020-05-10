# API Specification
## **Get Workspace by ID**
 **GET** /workspaces/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [<SERIALIZED USER WITH JUST NAME>, ... ],
         "channels": [<SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
     }
 }
```

## **Get all workspaces of a user**
 **GET** /{user id}/workspaces/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": [
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>,
               "url": <USER INPUT FOR URL>,
               "users": [<Serialized user with just name>],
               "channels": [<Serialized channels that are public]
         }
         {
               "id": <ID>,
               "name": <USER INPUT FOR NAME>,
               "url": <USER INPUT FOR URL>,
               "users": [<Serialized user with just name>],
               "channels": [<Serialized channels that are public]
         }
         ...
     ]
 }
```

## **Create a workspace**
 **POST** /workspaces/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "url": <USER INPUT FOR URL>,
         "users": [<SERIALIZED USER WITH JUST NAME>, ... ],
         "channels": [<SERIALIZED CHANNEL THAT IS PUBLIC>, ... ]
     }
 }
```
