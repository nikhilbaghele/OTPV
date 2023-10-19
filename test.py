import otpv3 as otp
import pytest
import unittest
from otpv3 import validate_email, generate_otp


class TestProgramFunctions(unittest.TestCase):

    def test_validate_email(self):

        result = validate_email("nikhilbaghele11@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = validate_email("nikhilbaghele11@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generate_otp(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())


if __name__ == '_main_':
    pytest.main()