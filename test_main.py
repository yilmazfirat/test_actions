import unittest
from main import add as main_add


class TestMain(unittest.TestCase):

    def test_add(self):
        result = main_add(4, 6)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
