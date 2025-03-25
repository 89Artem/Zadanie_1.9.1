def binary_search(arr, x):
    """Функция для выполнения двоичного поиска."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def sort_list(arr):
    """Функция для сортировки списка по возрастанию."""
    return sorted(arr)


def main():
    # Запрос ввода последовательности чисел
    input_sequence = input("Введите последовательность чисел через пробел: ")

    # Преобразование введённой последовательности в список
    try:
        numbers = list(map(float, input_sequence.split()))
    except ValueError:
        print("Ошибка: Введите только числа.")
        return

    # Сортировка списка
    sorted_numbers = sort_list(numbers)

    # Запрос числа у пользователя
    try:
        user_number = float(input("Введите число: "))
    except ValueError:
        print("Ошибка: Введите корректное число.")
        return

    # Поиск позиции с помощью двоичного поиска
    position = binary_search(sorted_numbers, user_number)

    if position == 0:
        print(f"Все элементы в списке больше или равны {user_number}.")
    elif position == len(sorted_numbers):
        print(f"Все элементы в списке меньше {user_number}.")
    else:
        print(f"Элемент меньше {user_number} находится на позиции {position - 1}, "
              f"а элемент больше или равный {user_number} находится на позиции {position}.")


if __name__ == "__main__":
    main()