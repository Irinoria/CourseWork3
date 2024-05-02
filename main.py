from src.utils import get_operations, sort_operation_by_date, filter_operation_by_state


#Берем данные из файла json и выводим последние 5 выполненных (EXECUTED) операций
def main(filename='operations.json'):
    operations = get_operations(filename)
    operations = filter_operation_by_state(*operations, state='EXECUTED')
    operations = sort_operation_by_date(*operations)

    for op in operations[:5]:
        print(op.safe())
        print()


if __name__ == '__main__':
    main()
