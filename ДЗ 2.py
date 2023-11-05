def get_permutations(input_str, k):
    if not isinstance(input_str, str) or not isinstance(k, int):
        print("Ошибка: Неверный тип данных")
        return []

    if k < 0 or k > len(input_str):
        print("Ошибка: Недопустимое значение k")
        return []

    def generate_permutations(input_str, k):
        if k == 0:
            return [""]
        if not input_str:
            return []

        permutations = []

        for i in range(len(input_str)):
            first_char = input_str[i]
            remaining_str = input_str[:i] + input_str[i+1:]
            
            smaller_permutations = generate_permutations(remaining_str, k - 1)
            
            for perm in smaller_permutations:
                permutations.append(first_char + perm)

        return permutations
      
    return generate_permutations(input_str, k)

while True:
    input_str = input("Введите строку: ")
    k_str = input("Введите число k: ")

    try:
        k = int(k_str)
    except ValueError:
        print("Ошибка: Неверный тип данных для k. Пожалуйста, введите данные заново.")
        continue

    result = get_permutations(input_str, k)
    for perm in result:
        print(perm)
    break
