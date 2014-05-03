# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from google.appengine.api import users
from usuario import users_service

def index(_write_tmpl):
        _write_tmpl('templates/home.html')

def listar(_write_tmpl):
    users=users_service.get_all_users().fetch()
    lista = []
    i = 0
    for user in users:
        user = user.to_dict()
        if "@" in user['nome']:
            user['nome'], __ = user['nome'].split("@")
        lista.append(user)
        user['indice'] = i
        i+=1
    _write_tmpl('templates/listar.html', {'lista':lista})

def mangas(_write_tmpl, name):
    path = 'templates/mangas-' + name + '.html'
    _write_tmpl(path)

def episodio(_write_tmpl, ep, length):
    data = {'episodio': ep, "length": length}
    _write_tmpl('templates/episodio.html', data)

def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)