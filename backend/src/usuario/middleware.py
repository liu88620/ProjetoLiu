# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl
from google.appengine.api import users
from usuario.model import Usuario


def execute(next_process, handler, dependencies, **kwargs):
    user = users.get_current_user()
    if user:
        google_id = user.user_id()
        query = Usuario.query_by_google(google_id)
        usuario_logado = query.get()
        if not usuario_logado:
            usuario_logado = Usuario(nome=user.nickname(),
                                     email=user.email(),
                                     google_id=google_id)
            usuario_logado.put()
        logout_url=users.create_logout_url('/')
        dependencies['usuario_logado']= usuario_logado
        dependencies['logout_url']= logout_url
    else:
        dependencies['usuario_logado']= False
        dependencies['login_url'] = users.create_login_url('/')


    next_process(dependencies, **kwargs)
