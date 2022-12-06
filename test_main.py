import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        result = main.add(4, 5)
        self.asserEqual(result, 9)
