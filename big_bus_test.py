import unittest
import cmd
import big_bus as bus


class BigBusTest(unittest.TestCase):
    '''unit testing for big bus ticket purchase software'''
    def test_buy_too_many_tickets(self):
        buying_interface = bus.Shell(cmd.Cmd)

        self.assertEqual(buying_interface.do_buy(3),"Sorry, maximum ticket purchase is 4!\n")

        #will need to refactor ticket purchase check to separate function
        #in order to properly test this


unittest.main()
