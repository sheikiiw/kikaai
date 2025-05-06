import json
from src.re_file_reader import filter_by_description, count_by_category

VALID_STATUSES = {"executed", "canceled", "pending"}
CATEGORIES = ["Перевод", "Покупка", "Снятие", "Пополнение"]  # Пример категорий


def load_data_from_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка загрузки файла: {e}")
        return []


def get_valid_status():
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if status in VALID_STATUSES:
            return status.upper()
        print(f"Статус операции \"{status}\" недоступен.")


def sort_operations(operations, ascending):
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_rub_only(operations):
    return [op for op in operations if op.get("currency", "").lower() == "rub"]


def print_operations(operations):
    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print(f"\nВсего банковских операций в выборке: {len(operations)}")
    for op in operations:
        print(f"\n{op['date']} {op['description']}")
        print(op.get("from", "") + " -> " + op.get("to", ""))
        print(f"Сумма: {op['amount']} {op['currency']}")


def main():
    while True:
        print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите источник данных:\n1. JSON\n2. CSV\n3. XLSX\n4. Выход")

        choice = input("Введите номер: ").strip()
        if choice == "4":
            print("До свидания!")
            break
        if choice != "1":
            print("Пока реализована только работа с JSON.")
            continue

        operations = load_data_from_json("data/operations.json")
        if not operations:
            continue
        print("Выбран JSON-файл.")

        # Фильтрация по статусу
        status = get_valid_status()
        filtered_ops = [op for op in operations if op.get("status", "").lower() == status.lower()]

        # Сортировка по дате
        if input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
            asc = input("По возрастанию или по убыванию? ").strip().lower() == "по возрастанию"
            filtered_ops = sort_operations(filtered_ops, asc)

        # Фильтрация по валюте
        if input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower() == "да":
            filtered_ops = filter_rub_only(filtered_ops)

        # Фильтрация по описанию
        if input("Фильтровать по слову в описании? Да/Нет: ").strip().lower() == "да":
            search = input("Введите слово для фильтрации: ")
            filtered_ops = filter_by_description(filtered_ops, search)

        # Подсчет по категориям
        if input("Показать статистику по категориям? Да/Нет: ").strip().lower() == "да":
            category_counts = count_by_category(filtered_ops, CATEGORIES)
            print("\nСтатистика по категориям:")
            for category, count in category_counts.items():
                print(f"{category}: {count} операций")
        # Вывод операций
        print("\nРаспечатываю итоговый список транзакций...")
        print_operations(filtered_ops)


if __name__ == "__main__":
    main()
