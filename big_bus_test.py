import unittest
import cmd
import big_bus as BB
import buy_action as Buy
from datetime import date, datetime


class BigBusTest(unittest.TestCase):
    '''unit testing for big bus ticket purchase software'''
    def test_bought_valid_number_of_tickets(self):
        self.assertEqual(Buy._is_valid_number_of_tickets(5), False)
        self.assertEqual(Buy._is_valid_number_of_tickets(4), True)

    def test_did_input_valid_route(self):
        blue_string = "blue"
        red_string = "RED"
        green_string = "greEn"
        purple_string = "purple"

        self.assertEqual(Buy._is_valid_route(blue_string), True)
        self.assertEqual(Buy._is_valid_route(red_string), True)
        self.assertEqual(Buy._is_valid_route(green_string), True)
        self.assertEqual(Buy._is_valid_route(purple_string), False)

    def test_did_input_valid_month(self):
        '''TO DO: need to update test cases periodically'''
        this_month = date.today().month
        input_month_august = "8"
        input_month_may = "5"
        input_month_june = "6"

        self.assertEqual(Buy._is_valid_month(input_month_august), False)
        self.assertEqual(Buy._is_valid_month(input_month_may), True)
        self.assertEqual(Buy._is_valid_month(input_month_june), True)

    def test_did_input_valid_date(self):
        '''TO DO: also need to update test cases periodically'''
        todays_date = date.today().day
        input_invalid = "string"
        input_valid = "5"

        self.assertEqual(Buy._is_valid_date(input_month_invalid), False)
        self.assertEqual(Buy._is_valid_date(input_month_valid), True)








unittest.main()
