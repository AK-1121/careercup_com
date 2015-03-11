# http://www.careercup.com/question?id=5684278553739264
import unittest
from max_substr_without_dupls import max_length

class ProblemTestCase(unittest.TestCase):

    def test01(self): 
        self.assertEqual(max_length('abcdefghijklmnopqrstuvwxyz'), 26)

    def test02(self):
        self.assertEqual(max_length('a'*500), 1)
    
    def test03(self):
        self.assertEqual(max_length('a'), 1)

    def test04(self):
        self.assertEqual(max_length('aaaaaabcdeaaaaa'), 5)

    def test05(self):
        self.assertEqual(max_length('abcdabcdabcdabcdeabcdabcdabcd'), 5)

    def test06(self):
        # Error code: -1 (in case of empty string):
        self.assertEqual(max_length(''), -1)

    def test07(self):
        self.assertEqual(max_length('abcdefabcdefabcdef'), 6)


if __name__ == '__main__':
    unittest.main()
