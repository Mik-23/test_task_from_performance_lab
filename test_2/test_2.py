from math import sqrt


def read_circle(file_path):
    # Функция, возвращающая из файла координаты центра и радиус окружеости
    with open(file_path, 'r') as file:
        data = file.readlines()
        center = list(map(float, data[0].split()))
        radius = float(data[1])
        return center, radius


def read_dot(file_path):
    # Функция возвращающая из файла координаты точек
    with open(file_path, 'r') as file:
        data = tuple(tuple(float(i) for i in data.split())
                     for data in file.readlines())
        return data


def calculate_positions(circle_file, dot_file):
    # Координаты центра x, y центра окружности
    x_center, y_center = read_circle(circle_file)[0]
    # Радиус окуржности
    radius = read_circle(circle_file)[1]
    # Координаты точек окружности
    points = read_dot(dot_file)
    result = []
    for x, y in points:
        # Если точка находится внутри окружности, то добавляем в result 1
        if sqrt((x_center - x) ** 2 + (y_center - y) ** 2) < radius:
            result.append(1)
        # Если точка находится на окружности, то добавляем в result 0
        elif sqrt((x_center - x) ** 2 + (y_center - y) ** 2) == radius:
            result.append(0)
        # Если точка находится за пределами окружности, то добавляем в result 2
        else:
            result.append(2)
    return result


result = calculate_positions('circle.txt', 'dot.txt')
for res in result:
    print(res)
