# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from usuario import users_service
from usuario.model import Usuario
from make_test import prepare_to_test

class UsersTests(unittest.TestCase):

    def setUp(self):
        prepare_to_test()
        Usuario(nome="liu", email="liu@liu.com").put()


    def test_get_one_user(self):
        users = users_service.get_all_users().fetch()
        self.assertNotEqual(users, [])

    def test_get_email(self):
        user = users_service.get_user_by_email("liu@liu.com").get()
        self.assertEqual(user.email, "liu@liu.com")

    def test_add_user_with_google_id(self):
        users_service.add_user("iury", "iury@gmail.com", google_id="122132").put()

        user = Usuario.query(Usuario.nome=="iury", Usuario.google_id=="122132").get()
        self.assertIsNotNone(user)

    def test_add_user(self):
        users_service.add_user("iury", "iury@gmail.com").put()

        user = Usuario.query(Usuario.nome=="iury", Usuario.email=="iury@gmail.com").get()
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
