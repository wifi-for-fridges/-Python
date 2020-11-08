"""
Выполнить циклический сдвиг в списке целых чисел на указанное число шагов. Сдвиг также должен быть кольцевым,
 то есть элемент, вышедший за пределы списка, должен появляться с другого его конца.
"""

def move(list_numbers : list, step: int) -> list:
    """
    Выполняет циключеский кольцевой сдвиг списка чисел вправо либо влево на уканное число шагов
    :param list_numbers (list): список чисел, для которого необходимо осуществить сдвиг
    :param step (int): величина сдвига, > 0 - двигаем вправо, < 0 - влево, = 0 - оставляем список без изменений,
    знак данного числа (+ или -) означает лишь направление сдвига
    :return (list): новый список после осуществления сдвига
    """
    if step == 0:
        return numbers

    if step > 0:
        # в случае слишком большого значения величины сдвига,
        # результирующая величина сдвига равна real_step = input_step (mod len_of_list)
        if len(list_numbers) < step:
            step %= len(list_numbers)

        new_numbers = list_numbers[len(list_numbers) - step:]
        new_numbers.extend(list_numbers[:len(list_numbers) - step])
        return new_numbers

    if step < 0:
        # аналогично, в случае слишком большого значения величины сдвига,
        # результирующая величина сдвига равна real_step = input_step (mod len_of_list)
        step = abs(step)
        if len(list_numbers) < step:
            step %= len(list_numbers)

        new_numbers = list_numbers[step:]
        new_numbers.extend(list_numbers[:step])
        return new_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, -1, -2, 3, 8]

print(move(numbers, 55))    # оба случая равносильны сдвигу на 0 вправо и влево соответственно
print(move(numbers, -55))

print(move(numbers, 4))
print(move(numbers, -3), '\n')

numbers = [1, 2, 3, 4]
print(move(numbers, 55))    # оба случая равносильны сдвигу на 3 вправо и влево соответственно
print(move(numbers, -55))

print(move(numbers, 2))
print(move(numbers, -1))