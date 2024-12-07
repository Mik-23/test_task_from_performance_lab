def read_numbers_from_file(filepath):
    # Преобразуем данные файла в список
    with open(filepath, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


def min_moves_to_equal(nums):
    # Округляем до ближайшего целого числа среднее значение
    target = round(sum(nums) / len(nums))
    # Возвращаем минимальное чило ходов
    return sum(abs(num - target) for num in nums)


nums = read_numbers_from_file('numbers.txt')
moves = min_moves_to_equal(nums)

print(moves)
