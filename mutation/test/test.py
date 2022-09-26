import mutation.sample.sample as m
import unittest

class testsample(unittest.TestCase):
    def test_mutations(self):
        result= m.mutate_string('abracadabra',5,'k')
        self.assertEqual(result,'abrackdabra')

if __name__ == '__main__':
    unittest.main()