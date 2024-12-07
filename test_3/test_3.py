import json


def load_json(file_path):
    # Загружает json файл
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def fill_values(tests, values):
    # Заполняет значения с помощью рекурсии
    if isinstance(tests, dict):
        # Если это словарь, проверяем наличие ключа "id"
        test_id = tests.get("id")
        if test_id in values:
            tests["value"] = values[test_id]
        # Заполняем значения во всех вложенных элементах с помощью рекурсии
        for key, value in tests.items():
            fill_values(value, values)
    elif isinstance(tests, list):
        # Если это список, обрабатываем каждый элемент
        for item in tests:
            fill_values(item, values)


def write_json(tests_file, values_file, report_file):
    # Открывает файл с тестами
    tests = load_json(tests_file)
    # Открывает файл со значениями
    values = load_json(values_file)
    # Заполняет значения
    fill_values(tests, values)
    """Записывет заполненные значения в файл report,
    если файла нет, то он создастся"""
    with open(report_file, 'w') as file:
        json.dump(tests, file)


write_json('tests.json', 'values.json', 'report.json')
