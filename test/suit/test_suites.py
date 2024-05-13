import unittest
import sys
sys.path.append("../..")
from test.case.user.test_user_reg import TestUserReg
from test.case.user.test_user_login import TestUserLogin

smoke_suit=unittest.TestSuite()
smoke_suit.addTests([TestUserLogin("test_login_success"),TestUserReg("test_user_reg")])

def get_suit(suit_name):
    smoke_suit = unittest.TestSuite()
    smoke_suit.addTests([TestUserLogin("test_login_success"), TestUserReg("test_user_reg")])
    return suit_name

unittest.TextTestRunner(verbosity=2).run(smoke_suit)

