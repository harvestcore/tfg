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
        "history", "reload", "tag"
    ]))
    data = fields.Dict(required=True)


class SingleImageTagProps(Schema):
    repository = fields.Str(required=True)
    tag = fields.Str(required=True)
    force = fields.Bool()


class BaseImageProps(Schema):
    operation = fields.Str(required=True, validate=validate.OneOf([
        "build", "get", "prune", "pull", "push", "remove", "search"
    ]))
    data = fields.Dict(required=True)


class ImageBuildProps(Schema):
    path = fields.Str(required=True)
    tag = fields.Str()
    quiet = fields.Bool(default=True)
    nocache = fields.Bool()
    rm = fields.Bool()
    pull = fields.Bool()
    forcerm = fields.Bool()
    dockerfile = fields.Str()
    buildargs = fields.Dict()
    container_limits = fields.Dict()
    shmsize = fields.Int()
    labels = fields.Dict()


class ImageGetProps(Schema):
    name = fields.Str(required=True)


class ImagePullProps(Schema):
    repository = fields.Str()
    tag = fields.Str()
    auth_config = fields.Dict()
    platform = fields.Str()


class ImagePushProps(Schema):
    repository = fields.Str(required=True)
    tag = fields.Str()
    stream = fields.Bool(default=False)
    auth_config = fields.Dict()


class ImageRemoveProps(Schema):
    image = fields.Str(required=True)
    force = fields.Bool()
    noprune = fields.Bool()


class ImageSearchProps(Schema):
    term = fields.Str(required=True)
