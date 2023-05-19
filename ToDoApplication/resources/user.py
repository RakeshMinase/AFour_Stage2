from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
# import math
from LoggedInUserId import LOGINUSERID
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt,
    create_refresh_token,
    get_jwt_identity,
)
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from blocklist import BLOCKLIST

blp = Blueprint("Users", "users", description="Operations on users")
# LOGINUSERID = 1


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()
        print(user.user_id)
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.user_id, fresh=True)
            refresh_token = create_refresh_token(user.user_id)
            LOGINUSERID.clear()
            LOGINUSERID.append(user.user_id)
            print(LOGINUSERID[0])
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        abort(400, message="Invalid credentials")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": new_token}, 200


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        LOGINUSERID.clear()
        return {"Message": "Successfully logged out"}, 200


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        print(user_data)
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(400, message="Username already exists")
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered!"}


@blp.route("/user")
class UserTesting(MethodView):

    @jwt_required()
    def delete(self):
        user = UserModel.query.get_or_404(LOGINUSERID[0])
        if user:
            db.session.delete(user)
            db.session.commit()
            jti = get_jwt()["jti"]
            BLOCKLIST.add(jti)
            LOGINUSERID.clear()
            return {"message": "User Deleted"}, 200
        else:
            abort(400, message="User not deleted")
