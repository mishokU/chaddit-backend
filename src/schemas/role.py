from . import fields, Schema

class RoleSchema(Schema):
  role_id = fields.Int(dump_oly = True)
  role_name = fields.Str()