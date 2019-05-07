import unittest
import cmd
import big_bus as BB
import buy_action as Buy
import date_class as DC
import ticket as Tix
from datetime import date, datetime


class BigBusTest(unittest.TestCase):
    '''unit testing for big bus ticket purchase software'''
    def test_bought_valid_number_of_tickets(self):
        self.assertEqual(Tix.is_valid_number_of_tickets(5), False)
        self.assertEqual(Tix.is_valid_number_of_tickets(4), True)

    def test_did_input_valid_route(self):
        blue_string = "blue"
        red_string = "RED"
        green_string = "greEn"
        purple_string = "purple"

        self.assertEqual(Buy.is_valid_route(blue_string), True)
        self.assertEqual(Buy.is_valid_route(red_string), True)
        self.assertEqual(Buy.is_valid_route(green_string), True)
        self.assertEqual(Buy.is_valid_route(purple_string), False)

    def test_did_input_valid_month(self):
        '''TO DO: need to update test cases periodically'''
        this_month = date.today().month
        input_month_august = "8"
        input_month_may = "5"
        input_month_june = "6"

        self.assertEqual(DC.is_valid_month(input_month_august), False)
        self.assertEqual(DC.is_valid_month(input_month_may), True)
        self.assertEqual(DC.is_valid_month(input_month_june), True)

    def test_did_input_valid_date(self):
        '''TO DO: also need to update test cases periodically'''
        this_month = date.today().month
        good_input = "7"
        bad_input_over_10_days = "30"
        bad_input_in_the_past = "2"

        self.assertEqual(DC.is_valid_date(bad_input_over_10_days, this_month), False)
        self.assertEqual(DC.is_valid_date(bad_input_in_the_past, this_month), False)
        self.assertEqual(DC.is_valid_date(good_input, this_month), True)

    def test_date_formatting(self):
        month = "5"
        date = "1"
        year = 2019

        self.assertEqual(DC.format_date(month,date,year),"05-01-2019")







unittest.main()
