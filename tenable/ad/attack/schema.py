from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class AttackAttributesSchema(CamelCaseSchema):
    name = fields.Str()
    value = fields.Str()
    value_type = fields.Str()


class AttackVectorSchema(CamelCaseSchema):
    template = fields.Str()
    attributes = fields.Nested(AttackAttributesSchema, many=True)


class AttackPathSchema(CamelCaseSchema):
    ip = fields.Str()
    hostname = fields.Str()


class AttackSchema(CamelCaseSchema):
    id = fields.Int()
    directory_id = fields.Int()
    attack_type_id = fields.Int()
    dc = fields.Str()
    date = fields.DateTime()
    vector = fields.Nested(AttackVectorSchema)
    source = fields.Nested(AttackPathSchema)
    destination = fields.Nested(AttackPathSchema)
    is_closed = fields.Bool()
    resource_type = fields.Str()
    resource_value = fields.Str()
    date_end = fields.DateTime()
    date_start = fields.DateTime()
    include_closed = fields.Bool()
    limit = fields.Str()
    order = fields.Str()
    search = fields.Str()
