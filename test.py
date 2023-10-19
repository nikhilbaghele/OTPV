import unittest
import pytest
import validate_email, generate_otp, send_email

class TestProgramFunctions(unittest.TestCase):

    def test_validate_email(self):
        # Valid email addresses
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user123@domain.co"))

        # Invalid email addresses
        self.assertFalse(validate_email("invalid-email"))
        self.assertFalse(validate_email("user@.com"))
        self.assertFalse(validate_email("user@domain"))

    def test_generate_otp(self):
        # Generate OTP and check length
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

    def test_send_email(self):
        # Replace these with your own test email and SMTP server details
        test_email = "test@example.com"
        test_otp = "123456"

        # Test sending an email
        self.assertTrue(send_email(test_email, test_otp))

if _name_ == '_main_':
    unittest.main()