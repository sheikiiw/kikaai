import json
from src.re_file_reader import filter_by_description, count_by_category

VALID_STATUSES = {"executed", "canceled", "pending"}

def load_data_from_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

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
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print("Выберите источник данных:\n1. JSON\n2. CSV\n3. XLSX")

    choice = input("Введите номер: ").strip()
    if choice == "1":
        operations = load_data_from_json("data/operations.json")
        print("Выбран JSON-файл.")
    else:
        print("Пока реализована только работа с JSON.")
        return

    status = get_valid_status()
    filtered_ops = [op for op in operations if op.get("status", "").lower() == status.lower()]

    if input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
        asc = input("По возрастанию или по убыванию? ").strip().lower() == "по возрастанию"
        filtered_ops = sort_operations(filtered_ops, asc)

    if input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower() == "да":
        filtered_ops = filter_rub_only(filtered_ops)

    if input("Фильтровать по слову в описании? Да/Нет: ").strip().lower() == "да":
        search = input("Введите слово для фильтрации: ")
        filtered_ops = filter_by_description(filtered_ops, search)

    print("Распечатываю итоговый список транзакций...")
    print_operations(filtered_ops)