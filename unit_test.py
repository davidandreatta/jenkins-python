import unittest

def isNotNull(number):
    if number != 0:
        return True
    else:
        return False

class TestCase(unittest.TestCase):
    def test_isNotNull(self):
        self.assertTrue(isNotNull(0))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))
