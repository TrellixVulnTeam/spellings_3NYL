import unittest

class SimpleTest(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(1,1)

if __name__ =='__main__':
    unittest.main()
