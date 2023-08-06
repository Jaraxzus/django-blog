from django.test import TestCase, Client


class AuthUrlsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = "http://localhost:8000/api/v1/auth/register/"
        self.verify_email_url = "http://localhost:8000/api/v1/register/verify-email/"
        self.resend_email_url = "http://localhost:8000/api/v1/register/resend-email/"
        self.account_confirm_email_url = (
            "http://localhost:8000/api/v1/account_confirm_email/123/"
        )
        self.password_reset_url = "http://localhost:8000/api/v1/password/reset/"
        self.password_reset_confirm_url = (
            "http://localhost:8000/api/v1/password/reset/confirm/123/456/"
        )
        self.login_url = "http://localhost:8000/api/v1/login/"
        self.logout_url = "http://localhost:8000/api/v1/logout/"
        self.user_details_url = "http://localhost:8000/api/v1/user/"

    def test_register_url(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "testuser",
                "password1": "1234567sdfh97234jdfk*^",
                "password2": "1234567sdfh97234jdfk*^",
            },
        )
        print(response)
        self.assertEqual(response.status_code, 201)

    def test_verify_email_url(self):
        response = self.client.get(self.verify_email_url)
        self.assertEqual(response.status_code, 200)

    #
    # def test_resend_email_url(self):
    #     response = self.client.get(self.resend_email_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_confirm_email_url(self):
    #     response = self.client.get(self.account_confirm_email_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_password_reset_url(self):
    #     response = self.client.get(self.password_reset_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_password_reset_confirm_url(self):
    #     response = self.client.get(self.password_reset_confirm_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_login_url(self):
    #     response = self.client.get(self.login_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_logout_url(self):
    #     response = self.client.get(self.logout_url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_user_details_url(self):
    #     response = self.client.get(self.user_details_url)
    #     self.assertEqual(response.status_code, 200)
