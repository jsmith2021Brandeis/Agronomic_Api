#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()
from sqlalchemy.orm import relationship
from app import app, db
import re

@dataclass
class Role(db.Model):
    """Data model for roles."""

    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64), index=False, nullable=False)
    createdAt = db.Column(db.DateTime, index=False, nullable=False)
    updatedAt = db.Column(db.DateTime, index=False, nullable=False)
    enabled = db.Column(db.Boolean, index=False, nullable=False)
