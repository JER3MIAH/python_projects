import unittest
import fuction


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = fuction.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'jojooo'
        result = fuction.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = fuction.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()
