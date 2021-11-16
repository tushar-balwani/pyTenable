from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class AttackTypeOptionsSchema(CamelCaseSchema):
    id = fields.Int()
    codename = fields.Str()
    profile_id = fields.Int()
    attack_type_id = fields.Int()
    directory_id = fields.Int()
    value = fields.Str()
    value_type = fields.Str()
    name = fields.Str()
    description = fields.Str()
    translations = fields.List(fields.Str())
    staged = fields.Bool() #conflict
    per_page = fields.Str()
    page = fields.Str()
