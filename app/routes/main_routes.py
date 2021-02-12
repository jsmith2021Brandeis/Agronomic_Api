'''AgroFides Data-Collection API routes'''
import random
import time
from flask import jsonify
from werkzeug.exceptions import HTTPException
from app import app,db
from flask import jsonify, request
from app.models import Role
from app.serializer import (RoleSchema)

@app.errorhandler(HTTPException)
def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors"""
    return jsonify({
        "code" : error.code,
        "name" : error.name,
        "description" : error.description
    }), error.code

@app.route('/')
@app.route('/index')
def index():
    '''Main entry point'''
    # TODO: return swagger spec for api
    return jsonify({'meta': {'message': 'Welcome to AgroFides Bare-Bones API'}})

@app.route('/roles')
def list_roles():
    '''Lists access roles'''
    roles = Role.query.all()
    role_schema = RoleSchema(many=True)
    return jsonify({
        'data': role_schema.dump(roles)
    })

@app.route('/roles/<roleid>')
def get_role(roleid):
    '''Gets an access role'''
    role = Role.query.get(roleid)
    if role is None:
        return jsonify({"errors": [{"id": "ROLE_NOTFOUND", "status": 404, "title": "Role not found"}]}), 404
    role_schema = RoleSchema()
    return jsonify({
        'data': role_schema.dump(role)
    })


