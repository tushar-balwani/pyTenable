from marshmallow import fields, pre_load
from tenable.ad.base.schema import CamelCaseSchema


class LDAPConfigurationAllowedGroupsSchema(CamelCaseSchema):
    name = fields.Str()
    default_role_ids = fields.List(fields.Int())
    default_profile_id = fields.Int()


class LDAPConfigurationSchema(CamelCaseSchema):
    enabled = fields.Bool()
    url = fields.Str()
    search_user_dn = fields.Str()
    search_user_password = fields.Str()
    user_search_base = fields.Str()
    user_search_filter = fields.Str()
    allowed_groups = fields.Nested(LDAPConfigurationAllowedGroupsSchema, many=True)

    @pre_load()
    def convert(self, data, **kwargs):
        if data.get('search_userDN'):
            data['searchUserDN'] = data['search_userDN']
            del data['search_userDN']
        return data
