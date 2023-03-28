import unittest
import re


class Solution:
    def reverse_words(self, sentence):
        sentence = re.sub(' +', ' ', sentence.strip())
        sentence = list(sentence)
        str_len = len(sentence)

        str_rev(sentence, 0, str_len - 1)

        start = 0
        end = 0

        while start < str_len:

            while end < str_len and sentence[end] != ' ':
                end += 1
            str_rev(sentence, start, end - 1)
            start = end + 1
            end += 1

        return ''.join(sentence)

def str_rev(_str, start_rev, end_rev):
    while start_rev < end_rev:
        temp_var = _str[start_rev]
        _str[start_rev] = _str[end_rev]
        _str[end_rev] = temp_var

        start_rev += 1
        end_rev -= 1




class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.reverse_words("We love Python")
        self.assertEqual("Python love We", res)

