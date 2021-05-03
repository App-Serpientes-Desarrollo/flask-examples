from flask import Flask

# API STRUCTURE EndPoint
# GET     /user?id=id
# GET     /users
# POST    /user
# UPDATE  /user
# DELETE  /user?id=id

user_controller = Flask(__name__)

@app.route('/', methods=['GET'])
def get_user():
   
   return content, status.HTTP_201_CREATED
