from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), unique=False, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), unique=False, nullable=False
    )

    user = db.relationship("UserModel", back_populates="tasks")
