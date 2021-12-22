import unittest
from main import operation, num_input


true_operation = [3.5, 20_000]  # 140 рублей в долларах при курсе 0.025 и операции 'Перевести'
                                # стоимость электрогитары при курсе 0.025

true_input = ['CURRENT_STATE', 'CURRENT_STATE', 'STATE_COURSE']


class MyTestCase(unittest.TestCase):

    def test_operation(self):
        self.assertEqual(true_operation,\
                         [operation(140, 0.025, 'Перевести'),\
                          operation(20, 0.025, 'Cтоимость электрогитары Gibson SG в рублях')])

    def test_input(self):
        self.assertEqual(true_input, [num_input('-10'), num_input('abc23'), num_input('140.2')])


if __name__ == '__main__':
    unittest.main()
