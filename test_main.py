import unittest
from main import add


class TestMain(unittest.TestCase):

    def test_add(self):
        result = main.add(4, 5)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
