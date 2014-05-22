# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from web import users_rest, home
from mock import Mock
from usuario.model import Usuario
from make_test import prepare_to_test


class IntegrationTests(unittest.TestCase):

    def setUp(self):
        prepare_to_test()
        Usuario(nome="liu", email="liu@liu.com").put()

    def test_get_all_users_rest(self):
        write = Mock()
        users_rest.get_all_users(write)
        write.assert_called_once_with('[{"email": "liu@liu.com", "google_id": null, "nome": "liu"}]')

    def test_handler_listar(self):
        write = Mock()
        home.listar(write)
        write.assert_called_once_with(u'templates/listar.html', {u'lista': [{u'indice': 0, 'email': u'liu@liu.com', 'google_id': None, 'nome': u'liu'}]})

    def test_handler_mangas(self):
        write = Mock()
        home.mangas(write, "naruto")
        write.assert_called_once_with(u'templates/mangas-naruto.html')

    def test_handler_episodio(self):    
        write = Mock()
        home.episodio(write, "2", "10")
        write.assert_called_once_with(u'templates/episodio.html', {u'episodio': u'2', u'length': u'10'})