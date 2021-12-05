from unittest import TestCase, main
from first import nums


class NumsTest(TestCase):
    def test_plus(self):
        self.assertEqual(nums.plus(2, 3), 5)

    def test_div(self):
        self.assertEqual(nums.div(12, 4), 3)
        with self.assertRaises(ValueError) as e:
            nums.div(15, 0)
        self.assertEqual("Делитель равен 0", e.exception.args[0])


if __name__ == '__main__':
    main()
