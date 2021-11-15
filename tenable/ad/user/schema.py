from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class UserSchema(CamelCaseSchema):
    id = fields.Int()
    surname = fields.Str()
    name = fields.Str()
    email = fields.Email()
    password = fields.Str()
    locked_out = fields.Bool()
    department = fields.Str()
    role = fields.List(fields.Int())
    biography = fields.Str()
    active = fields.Bool()
    picture = fields.List(fields.Int())
    roles = fields.List(fields.Int())
    identifier = fields.Str()
    provider = fields.Str()
    eula_version = fields.Int()
    authToken = fields.Str()


class UserPermissionsSchema(CamelCaseSchema):
    entity_name = fields.Str()
    action = fields.Str()
    entity_ids = fields.List(fields.Int())
    dynamic_ids = fields.Str()


class UserRolesSchema(CamelCaseSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    permissions = fields.Nested(UserPermissionsSchema)


class UserInfoSchema(UserSchema):
    internal = fields.Bool()
    role = fields.Nested(UserRolesSchema)

