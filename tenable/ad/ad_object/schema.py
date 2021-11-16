from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class ADObjectAttributesSchema(CamelCaseSchema):
    name = fields.Str()
    value = fields.Str()
    value_type = fields.Bool()


class ADObjectSchema(CamelCaseSchema):
    # response keys
    id = fields.Int()
    directory_id = fields.Int()
    object_id = fields.Str()
    type = fields.Str()
    object_attributes = fields.Nested(ADObjectAttributesSchema, many=True)

    # common fields
    reasons = fields.List(fields.Int())

    # input values
    wanted_values = fields.List(fields.Str())
    page = fields.Str()
    per_page = fields.Str()
    expression = fields.Dict(fields.Str(), fields.Str())
    directories = fields.List(fields.Int())
    date_start = fields.DateTime()
    date_end = fields.DateTime()
    show_ignored = fields.Bool()

