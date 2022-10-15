from flask import request
from ..models import db, User, UserSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

user_schema = UserSchema()

class SignInView(Resource):
    
    def post(self):
        try:
            password1 = request.json["password1"]
            password2 = request.json["password2"]

            new_user = User(username=request.json["username"], password = password1, email=request.json["email"])
            db.session.add(new_user)
            db.session.commit()
            return 'Usuario creado exitosamente', 201
        except IntegrityError:
            db.session.rollback()
            return 'Error en la creación del usuario',409
        
