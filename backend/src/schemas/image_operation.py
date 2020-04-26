from marshmallow import fields, Schema, validate


class ImageObj(Schema):
    id = fields.Str()
    labels = fields.Dict()
    short_id = fields.Str()
    tags = fields.Str()


class RegistryDataObj(Schema):
    id = fields.Str()
    short_id = fields.Str()


class BaseSingleImageProps(Schema):
    name = fields.Str(required=True)
    operation = fields.Str(required=True, validate=validate.OneOf([
        "history", "reload"
    ]))
    data = fields.Dict(required=True)


class SingleImageTagProps(Schema):
    repository = fields.Str(required=True)
    tag = fields.Str(required=True)
    force = fields.Bool()


class BaseImageProps(Schema):
    operation = fields.Str(required=True, validate=validate.OneOf([
        "get", "prune", "pull", "remove", "search"
    ]))
    data = fields.Dict(required=True)


class ImageGetProps(Schema):
    name = fields.Str(required=True)


class ImagePullProps(Schema):
    repository = fields.Str()
    tag = fields.Str()
    auth_config = fields.Dict()
    platform = fields.Str()


class ImageRemoveProps(Schema):
    image = fields.Str(required=True)
    force = fields.Bool(default=True)
    noprune = fields.Bool()


class ImageSearchProps(Schema):
    term = fields.Str(required=True)
