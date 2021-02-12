from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from .models import Role

class RoleDataSchema(Schema):
    class Meta:
        type_ = 'Role'
        strict = True

    id = fields.Int()
    role = fields.Str()

class RoleSchema(Schema):
    class Meta:
        type_ = 'Role'
        strict = True

    id = fields.Int()
    role = fields.Str()
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime()
    enabled = fields.Bool()
