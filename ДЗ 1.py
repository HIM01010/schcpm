def count_divisors(num):
    divisors = 0
    list_of_divisors = []
    sqrt_num = int(num**0.5)
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            divisors += 2
            list_of_divisors.append(i)
            if i != num // i:
                list_of_divisors.append(num // i)
    if sqrt_num * sqrt_num == num:
        divisors -= 1
    list_of_divisors.sort(reverse=True)
    return divisors, list_of_divisors

def find_numbers_with_4_divisors(a, b):
    result = []
    for num in range(a, b + 1):
        divisors, list_of_divisors = count_divisors(num)
        if divisors == 4:
            result.append(num)
            result.append(list_of_divisors)
    return result

while True:
    try:
        a = int(input("Введите начало интервала (a): "))
        b = int(input("Введите конец интервала (b): "))
        
        numbers = find_numbers_with_4_divisors(a, b)
        
        if len(numbers) == 0:
            print("В указанном интервале нет чисел с 4 делителями.")
        else:
            print(f"Числа с 4 делителями в интервале от {a} до {b}:")
            for i in range(0, len(numbers), 4):
                print(f"Число {numbers[i]} имеет 4 делителя:", numbers[i+1][0], numbers[i+1][1], numbers[i+1][2], numbers[i+1][3], sep = " ")
        
        break
        
    except ValueError:
        print("Ошибка: Введите целые числа для начала и конца интервала.")
