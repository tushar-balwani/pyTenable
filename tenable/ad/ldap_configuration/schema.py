from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class LDAPConfigurationAllowedGroupsSchema(CamelCaseSchema):
    name = fields.Str()
    default_role_ids = fields.List(fields.Int())
    default_profile_id = fields.Int()


class LDAPConfigurationSchema(CamelCaseSchema):
    enabled = fields.Bool()
    url = fields.URL()
    search_userDN = fields.Str()
    search_user_password = fields.Str()
    user_search_base = fields.Str()
    user_search_filter = fields.Str()
    allowed_groups = fields.Nested(LDAPConfigurationAllowedGroupsSchema, many=True)
