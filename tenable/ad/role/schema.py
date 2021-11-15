from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class RolePermissionsSchema(CamelCaseSchema):
    entity_name = fields.Str()
    action = fields.Str()
    entity_ids = fields.List(fields.Int())
    dynamic_id = fields.Str()


class RoleSchema(CamelCaseSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    permissions = fields.Nested(RolePermissionsSchema, many=True)
