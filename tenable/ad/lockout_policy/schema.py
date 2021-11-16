from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class LockoutPolicySchema(CamelCaseSchema):
    enabled = fields.Bool()
    lockout_duration = fields.Int()
    failed_attempt_threshold = fields.Int()
    failed_attempt_period = fields.Int()
