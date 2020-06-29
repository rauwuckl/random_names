import unittest
from RandomNames import generator as gen
import random


class MyTestCase(unittest.TestCase):
    def test_generator(self):

        t_name = gen.random_name('#43?')
        n1 = random.randint(0, 100)

        t2_name = gen.random_name('#42?')

        t4_name = gen.random_name('#43?')
        n2 = random.randint(0, 100)

        self.assertEqual(t_name, t4_name)
        self.assertNotEqual(t_name, t2_name)
        self.assertNotEqual(n1, n2)


        for i in range(10):
            r_name = gen.random_name()
            pass

    def test_two(self):
        import RandomNames
        n = RandomNames.random_name()
        pass



if __name__ == '__main__':
    unittest.main()
