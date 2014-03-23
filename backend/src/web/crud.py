# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from rest import Curso, salvar


# -Curso.gender,
def index(_write_tmpl, _resp):
    '''
    query = Curso.query().order(-Curso.firstname, -Curso.lastname, -Curso.country, -Curso.state,
                                -Curso.city,-Curso.address,-Curso.zipcode,-Curso.phone,-Curso.email)
    dct = {'lista_cursos': query.fetch()}
    '''
    _resp.write('teste')


# gender,
# gender=gender,
def salvar(_handler, firstname, lastname, country, state, city, address, zipcode, phone, email):
    #salvar(firstname, lastname, country, state, city, address, zipcode, phone, email)
    path = router.to_path(index)
    _handler.redirect(path)


def cadastrar(_write_tmpl):
    '''
    path = router.to_path(salvar)
    dct = {'salvar_curso': path, 'req': _req}
    '''
    _write_tmpl('/templates/curso_form.html')