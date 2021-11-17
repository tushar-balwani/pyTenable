from marshmallow import Schema, fields


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def endcap(s):
    parts = s.split("_")
    return parts[0] + "".join(i.title() for i in parts[1:len(parts) - 1]) + parts[-1].upper()


class CamelCaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        endcaps = ['search_user_dn', 'expiration_date_utc']
        if field_name in endcaps:
            field_obj.data_key = endcap(field_obj.data_key or field_name)
        else:
            field_obj.data_key = camelcase(field_obj.data_key or field_name)
