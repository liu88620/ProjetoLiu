# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import json
from usuario import users_service


def get_all_users(_write):
    users = users_service.get_all_users().fetch()
    users_dict = [user.to_dict() for user in users]
    _write(json.dumps(users_dict))


def remove_user(email):
    user = users_service.get_user_by_email(email).get()
    user.key.delete()


def add_user(name, email, google_id):
    user = users_service.add_user(name, email, google_id)
    user.put()

def edit_user(name, email, google_id):
    users_service.edit_user(name, email, google_id)
