from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import TaskSchema, UpdateTaskSchema
from flask_jwt_extended import jwt_required
from LoggedInUserId import LOGINUSERID
from flask import request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import TaskModel

blp = Blueprint("tasks", __name__, description="Operations on tasks")


@blp.route("/tasks")
class TaskList(MethodView):
    @jwt_required()
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        # print(LOGINUSERID[0])
        # return TaskModel.query.all()
        try:
            return TaskModel.query.filter(TaskModel.user_id == LOGINUSERID[0])
        except IndexError:
            abort(400, message="Log in again")

    @jwt_required()
    @blp.response(201, TaskSchema)
    def post(self):
        task_data = request.get_json()
        try:
            task = TaskModel(user_id=LOGINUSERID[0], **task_data)
        except IndexError:
            abort(400, message="Log in again")
        try:
            db.session.add(task)
            db.session.commit()
            return task
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occured while creating the task")


@blp.route("/task/<string:task_id>")
class Task(MethodView):
    @jwt_required()
    @blp.response(201, TaskSchema)
    def get(self, task_id):
        task = TaskModel.query.filter(TaskModel.user_id == LOGINUSERID[0], TaskModel.task_id == task_id).first()
        if task:
            return task
        else:
            abort(400, message="This task is not presend for the given user")

    @jwt_required()
    def delete(self, task_id):
        task = TaskModel.query.filter(TaskModel.user_id == LOGINUSERID[0], TaskModel.task_id == task_id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return {"message": "Task deleted"}
        else:
            abort(400, message="This task is not presend for the given user")

    @jwt_required()
    @blp.arguments(UpdateTaskSchema)
    @blp.response(200, TaskSchema)
    def put(self, task_data, task_id):
        task = TaskModel.query.filter(TaskModel.user_id == LOGINUSERID[0], TaskModel.task_id == task_id).first()
        if task:
            if task.task_name:
                task.task_name = task_data["task_name"]
            if task.status:
                task.status = task_data["status"]
        else:
            abort(400, message="This task is not presend for the given user")

        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while updating the task")
