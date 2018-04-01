"""
auth

Simple extension for authentication
"""

from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth

USERNAME = 'admin'
PASSWORD = 'python'

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == USERNAME:
        return PASSWORD
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
