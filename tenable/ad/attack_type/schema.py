from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class AttackTypeAttributesSchema(CamelCaseSchema):
    name = fields.Str()
    url = fields.URL()
    type = fields.Str()


class AttackTypeVectorTemplateReplacementsSchema(CamelCaseSchema):
    name = fields.Str()
    value_type = fields.Str()


class AttackTypeSchema(CamelCaseSchema):
    id = fields.Int()
    name = fields.Str()
    yarn_rules = fields.Str()
    description = fields.Str()
    workload_quota = fields.Int()
    mitre_attack_description = fields.Str()
    criticity = fields.Str()
    resources = fields.Nested(AttackTypeAttributesSchema, many=True)
    vector_template = fields.Str()
    vector_template_replacements = fields.Nested(AttackTypeVectorTemplateReplacementsSchema, many=True)
