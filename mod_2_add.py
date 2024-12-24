given_number = int(input('Введите выпавшее число: '))
print(given_number)
def get_all_divisors_brute(n):
    for i in range(3, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
divisors = list(get_all_divisors_brute(given_number))
#print('Делители исходного числа: ',*divisors)
answer = []
def get_digits_from_divisors(list_div):
    if given_number % 2 == 0:
        counter_i = given_number // 2
    else:
        counter_i = given_number // 2 + 1
    for i in range(1, counter_i):
        for j in divisors:
            if j > i and (j-i) > i:
                answer.extend([str(i), str(j - i)])
    print(''.join(answer))
get_digits_from_divisors(divisors)