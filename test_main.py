import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        result = main.add(4, 5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
