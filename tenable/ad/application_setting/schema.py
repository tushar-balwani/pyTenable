from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class ApplicationSettingsSchema(CamelCaseSchema):
    user_registration = fields.Bool()
    keep_audit_log = fields.Bool()
    log_retention_period = fields.Int()
    smtp_server_address = fields.Str()
    smtp_server_port = fields.Int()
    smtp_account = fields.Str()
    smtp_account_password = fields.Str()
    smtp_user_startTLS = fields.Bool()
    tls = fields.Bool()
    email_sender = fields.Str()
    default_role_ids = fields.List(fields.Int())
    default_profile_id = fields.Int()
    internal_certificate = fields.Str()
