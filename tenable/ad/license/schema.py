from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class LicenseSchema(CamelCaseSchema):
    customer_name = fields.Str()
    max_active_user_count = fields.Int()
    current_active_user_count = fields.Int()
    expiration_date_UTC = fields.DateTime()
    in_app_eula = fields.Bool()
    features = fields.List(fields.Str())
