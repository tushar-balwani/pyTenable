from marshmallow import fields, pre_load
from tenable.ad.base.schema import CamelCaseSchema


class LicenseSchema(CamelCaseSchema):
    customer_name = fields.Str()
    max_active_user_count = fields.Int()
    current_active_user_count = fields.Int()
    expiration_date_utc = fields.DateTime()
    in_app_eula = fields.Bool()
    features = fields.List(fields.Str())
    license = fields.Str()

    @pre_load()
    def convert(self, data, **kwargs):
        if data.get('expiration_dateUTC'):
            data['expirationDateUTC'] = data['expiration_dateUTC']
            del data['expiration_dateUTC']
        return data
