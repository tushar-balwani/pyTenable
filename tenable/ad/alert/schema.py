from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class AlertSchema(CamelCaseSchema):
    id = fields.Int()
    deviance_id = fields.Int()
    archived = fields.Str()
    read = fields.Str()
    date = fields.DateTime()
    directory_id = fields.Int()
    infrastructure_id = fields.Int()
    per_page = fields.Str()
    page = fields.Str()
