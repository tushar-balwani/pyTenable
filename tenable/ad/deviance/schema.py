from marshmallow import fields
from tenable.ad.base.schema import CamelCaseSchema


class DevianceAttributesSchema(CamelCaseSchema):
    name = fields.Str()
    value = fields.Str()


class DevianceReplacementsSchema(CamelCaseSchema):
    name = fields.Str()
    value = fields.Str()
    value_type = fields.Str()


class DevianceDescriptionSchema(CamelCaseSchema):
    template = fields.Str()
    replacements = fields.Nested(DevianceReplacementsSchema, many=True)


class DevianceSchema(CamelCaseSchema):
    id = fields.Int()
    directory_id = fields.Int()
    checker_id = fields.Int()
    profile_id = fields.Int()
    ad_object_id = fields.Int()
    reason_id = fields.Int()
    resolved_at = fields.DateTime()
    event_date = fields.DateTime()
    ignore_until = fields.DateTime()
    deviance_provider_id = fields.Str()
    attributes = fields.Nested(DevianceAttributesSchema, many=True)
    description = fields.Nested(DevianceDescriptionSchema)

    # input params
    page = fields.Str()
    per_page = fields.Str()
    batch_size = fields.Str()
    last_identifier_seen = fields.Str()
    resolved = fields.Str()
    expression = fields.Dict(fields.Str(), fields.Str())
    show_ignored = fields.Bool
