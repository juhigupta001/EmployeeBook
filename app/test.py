import logging
from flask import url_for
from flask.ext.login import current_user

from app.bases import BaseTestCase
from app.users.models import User


class UserViewsTests(BaseTestCase):
    def test_users_can_login(self):
        User.create(name="Juhi", email="juhi@gmail.com",password="12345")

        with self.client:
            response = self.client.post("/login/", data={"name": "Juhi ",password": "12345"})

            self.assert_redirects(response, url_for("index"))
            self.assertTrue(current_user.name == "Juhi")
            self.assertFalse(current_user.is_anonymous())
            logging.info('TestCase 1 Passed')                                                      
                                                         

    def test_users_can_logout(self):
        User.create(name="Juhi",email=" juhi@gmail.com", password="12345")

        with self.client:
            self.client.post("/login/", data={"name": "juhi", "password": "12345"})
            self.client.get("/logout/")
            logging.info('TestCase 2 Passed')
            self.assertTrue(current_user.is_anonymous())

    def test_invalid_password_is_rejected(self):
        User.create(name="juhi",email="juhi@gmail.com", password="12345")

        with self.client:
            self.client.post("/login/", data={"name": "juhi", "password": "****"})
            logging.info('TestCase 3 Passed')
            self.assertTrue(current_user.is_anonymous())
