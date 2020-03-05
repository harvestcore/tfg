from marshmallow import fields, Schema, validate


class BaseSchema(Schema):
    enabled = fields.Bool(dump_only=True)
    deleted = fields.Bool(dump_only=True)
    # creation_time = fields.DateTime(dump_only=True)
    # last_modified = fields.DateTime(dump_only=True)
    # delete_time = fields.DateTime(dump_only=True)


class QuerySchema(Schema):
    query = fields.Dict(required=True)
    filter = fields.Dict()
