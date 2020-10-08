import unittest
class TestingStringMethods(unittest.TestCase):


   def test_is_string_lower(self):
      '''makes sure a string is all lowercase''' 
      corpus = '../../data/txt/corpus.txt'
      self.assertTrue(corpus.islower())
      self.assertFalse(corpus.islower())


def main():
      unittest.main()

if __name__ == '__main__':
  corpus = '../../data/txt/corpus.txt'
  main()
  
  
################################################
# results:

# F
# ======================================================================
# FAIL: test_is_string_lower (__main__.TestingStringMethods)
# makes sure a string is all lowercase
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_strings_are_lowercase.py", line 11, in test_is_string_lower
#     self.assertFalse(corpus.islower())
# AssertionError: True is not false

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)

################################################
