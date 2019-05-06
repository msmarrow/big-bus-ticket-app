import unittest
import cmd
import big_bus as bus
import buy_action as buy


class BigBusTest(unittest.TestCase):
    '''unit testing for big bus ticket purchase software'''
    def test_buought_valid_number_of_tickets(self):

        self.assertEqual(buy.is_valid_number_of_tickets(5),False)
        self.assertEqual(buy.is_valid_number_of_tickets(4),True)

unittest.main()
