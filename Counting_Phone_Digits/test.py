# Phone Number

# Write a program that cleans up user-entered phone numbers so that they can be sent SMS messages.

# The rules are as follows:

#     If the phone number is less than 10 digits assume that it is bad number
#     If the phone number is 10 digits assume that it is good
#     If the phone number is 11 digits and the first number is 1, trim the 1 and use the last 10 digits
#     If the phone number is 11 digits and the first number is not 1, then it is a bad number
#     If the phone number is more than 11 digits assume that it is a bad number

# We've provided tests, now make them pass.

# Hint: Only make one test pass at a time. Disable the others, then flip each on in turn after you get the current failing one to pass.
# Source
# Event Manager by JumpstartLab http://tutorials.jumpstartlab.com/projects/eventmanager.html


import unittest

from phone_number import Phone


class PhoneTest(unittest.TestCase):
    def test_cleans_number(self):
        number = Phone("(123) 456-7890").number
        self.assertEqual("1234567890", number)

    def test_cleans_number_with_dots(self):
        number = Phone("123.456.7890").number
        self.assertEqual("1234567890", number)

    def test_valid_when_11_digits_and_first_is_1(self):
        number = Phone("11234567890").number
        self.assertEqual("1234567890", number)

    def test_invalid_when_11_digits(self):
        number = Phone("21234567890").number
        self.assertEqual("0000000000", number)

    def test_invalid_when_9_digits(self):
        number = Phone("123456789").number
        self.assertEqual("0000000000", number)

    def test_area_code(self):
        number = Phone("1234567890")
        self.assertEqual("123", number.area_code())

    def test_pretty_print(self):
        number = Phone("1234567890")
        self.assertEqual("(123) 456-7890", number.pretty())

    def test_pretty_print_with_full_us_phone_number(self):
        number = Phone("11234567890")
        self.assertEqual("(123) 456-7890", number.pretty())

if __name__ == '__main__':
    unittest.main()
