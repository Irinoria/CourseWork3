import json

from src.dto import Operation


def get_operations(filename):
    operations = []
    with open(filename, encoding='utf-8') as f:
        for data in json.load(f):
            if data:
                op = Operation.init_from_dict(data)
                operations.append(op)

    return operations

#Фильтр операции по статусу
def filter_operation_by_state(*operations: Operation, state: str) -> list[Operation]:
    filtered_operations: list[Operation] = []
    for op in operations:
        if op.state == state:
            filtered_operations.append(op)
    return filtered_operations

#Сортировка операции по дате
def sort_operation_by_date(*operations: Operation) -> list[Operation]:
    return sorted(operations, key=lambda op: op.date, reverse=True)
