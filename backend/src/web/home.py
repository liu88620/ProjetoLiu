# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from google.appengine.api import users


def index(_write_tmpl):
    user = users.get_current_user()
    print user
    if user:
        user_data = {'nickname': user.nickname(), "logout_url":users.create_logout_url('/')}
        _write_tmpl('templates/home.html', user_data)
    else:
        user_data = {'login_url': users.create_login_url('/')}
        _write_tmpl('templates/home.html', user_data)

def mangas(_write_tmpl, name):
    path = 'templates/mangas-' + name + '.html'
    _write_tmpl(path)

def episodio(_write_tmpl, ep):
    data = {'episodio': ep}
    _write_tmpl('templates/episodio.html', data)

def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)