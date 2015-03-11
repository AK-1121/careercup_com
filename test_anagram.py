import unittest
from anagram import a_is_anagram_in_b

class AnagrammaTestCase(unittest.TestCase):

    def test01(self):
        self.assertTrue(a_is_anagram_in_b("xyz", "faasfasfasxzyzasd"))

    def test02(self):
        self.assertFalse(a_is_anagram_in_b("a", "lgkdslkgj"))

    def test03(self):
        self.assertFalse(a_is_anagram_in_b("aa", "lgkdslkgja"))

    def test04(self):
        self.assertFalse(a_is_anagram_in_b("aabb", "labagkdslkgaabjbba"))

    def test05(self):
        self.assertTrue(a_is_anagram_in_b("xxyyzz", "xyzzyxlgkdslkgj"))

    def test06(self):
        self.assertFalse(a_is_anagram_in_b("aaabbbccc", "ccbbbaaa"))

    def test07(self):
        self.assertFalse(a_is_anagram_in_b("abc", "ab"*500))

    def test08(self):
        self.assertTrue(a_is_anagram_in_b("abcabc", "cbaacb"))


if __name__ == '__main__':
    unittest.main()
