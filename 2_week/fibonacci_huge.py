# Uses python3

def calc_fib_fast(n: int) -> int:
    """Получить n-е число фибоначчи - F(n)"""
    if n <= 1:
        return n
    elif n == 2:
        return 1
    l = [0, 1, 1]
    for i in range(2, n):
        next_fibo = l[-1] + l[-2]
        l.append(next_fibo)
    return l[-1]

def get_fib_list(n):
    """Список чисел фибоначчи"""
    if n <= 1:
        return n
    elif n == 2:
        return 1
    l = [0, 1, 1]
    for i in range(2, n):
        next_fibo = l[-1] + l[-2]
        l.append(next_fibo)
    return l

def get_fibonaccihuge(n: int, m: int) -> int:
    """
    Неделя 2, Задача 5 Advanced Problem: Huge Fibonacci Number modulo m
    :param n: номер фибоначчи
    :param m: делитель
    :return: остаток от делегия F(n) на m
    """
    rem_list = find_periodicaly_reminders_list(n, m)
    periodicaly_length = len(rem_list)
    if periodicaly_length < n:
        n = n % periodicaly_length
    return calc_fib_fast(n) % m

def check_if_periodicaly(l: list) -> bool:
    """Проверяем есть ли последние два элемента списка в оставшейся его части в той же последовательности.
    """
    last_two_elements = ''.join([str(i) for i in l[-2:]])
    elements_without_last_two = ''.join([str(i) for i in l[:-2]])
    if last_two_elements in elements_without_last_two:
        return True
    return False

def find_periodicaly_reminders_list(n: int, m: int) -> list:
    """ Находим остатки чисел фибоначчи
    :param n: последний номер
    :param m: делитель
    :return:
    """
    l = [0, 1, 1]
    if n <= 1:
        return [1]
    for i in range(2, n):
        l.append((l[-1] + l[-2]) % m)
        if check_if_periodicaly(l):
            return l[:-2]
    return l

if __name__ == '__main__':
    print(get_fibonaccihuge(281621358815590,30524))