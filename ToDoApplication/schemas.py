from marshmallow import Schema, fields


class PlainTaskSchema(Schema):
    task_id = fields.Int(dump_only=True)
    task_name = fields.Str(required=True)
    status = fields.Str(required=True)


class PlainUserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserSchema(PlainUserSchema):
    tasks = fields.Nested(PlainTaskSchema(), dump_only=True)


class TaskSchema(PlainTaskSchema):
    user_id = fields.Int(required=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True, load_only=True)


class UpdateTaskSchema(Schema):
    task_name = fields.Str()
    status = fields.Str()
