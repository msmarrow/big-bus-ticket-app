import unittest
import cmd
import big_bus as bus
import buy_action as buy


class BigBusTest(unittest.TestCase):
    '''unit testing for big bus ticket purchase software'''
    def test_bought_valid_number_of_tickets(self):
        self.assertEqual(buy.is_valid_number_of_tickets(5), False)
        self.assertEqual(buy.is_valid_number_of_tickets(4), True)

    def test_did_input_valid_route(self):
        blue_string = "blue"
        red_string = "RED"
        green_string = "greEn"
        purple_string = "purple"

        self.assertEqual(is_valid_route(blue_string), True)
        self.assertEqual(is_valid_route(red_string), True)
        self.assertEqual(is_valid_route(green_string), True)
        self.assertEqual(is_valid_route(purple_string), False)

unittest.main()
