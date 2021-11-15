from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class EmailNotifierSchema(CamelCaseSchema):
    id = fields.Int()
    address = fields.Str()
    criticity_threshold = fields.Int()
    directories = fields.List(fields.Int())
    description = fields.Str()
    checkers = fields.List(fields.Int())
    attack_types = fields.List(fields.Int())
    profiles = fields.List(fields.Int())
    should_notify_on_initial_full_security_check = fields.Bool()
    input_type = fields.Str()
