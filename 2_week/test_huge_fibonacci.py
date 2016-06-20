from unittest import TestCase
import fibonacci_huge

def get_fib_list(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    l = [0, 1, 1]
    for i in range(2, n):
        next_fibo = l[-1] + l[-2]
        l.append(next_fibo)
    return l


class TestHugeFibo(TestCase):
    def test_main(self):
        fl = get_fib_list(30)
        for divider in (2, 3, 4, 5, 6, 7, 8, 9):
            res_list = [(i, n, n % divider) for i, n in enumerate(fl)]
            for test_tuple in res_list:
                fibo_index, fibo_value, reminder_correct = test_tuple
                reminder_with_huge = fibonacci_huge.get_fibonaccihuge(fibo_index, divider)
                self.assertEqual(reminder_with_huge, reminder_correct)
                print('check ',reminder_with_huge,reminder_correct)