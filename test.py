import unittest

import do

class TestDo(unittest.TestCase):
    def test_something_return(self):
        output = do.do_something()
        self.assertEqual("hello world", output)

if __name__ == "__main__":
    unittest.main()
