import json
from datetime import datetime
with open('../operations.json', 'r') as file:
    data = json.load(file)


def executed_operations(operations):
    """Возвращает переменную в которой содержаться только выполненные операции"""
    executed_operations_list = []
    for operation in operations:
        if "state" in operation:
            if operation["state"] == "EXECUTED":
                executed_operations_list.append(operation)
    return executed_operations_list


def convert_date(operations):
    """берет дату операций и со str конвертирует в datetime"""
    convert_operations = []
    for operation in operations:
        operation_time = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
        formatted_operation_time = operation_time.strftime("%d.%m.%Y")
        operation["date"] = formatted_operation_time
        convert_operations.append(operation)
    return convert_operations


def print_last_5_operations(operations):
    """Сортируем операции по дате в обратном порядке, а потом возвращает последние 5 операций"""
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def mask_card_number(card):
    """берет значение по ключу from и оставляет только номер карты, потом маскирует номер """
    digits_only = ''.join(c for c in card if c.isdigit())
    card_name = ''.join(c for c in card if not c.isdigit())
    if card_name[-1] == ' ':
        card_name = card_name[:-1]
    if card_name != 'Счет':
        blocks = [digits_only[i:i+4] for i in range(0, len(digits_only), 4)]
        masked_number = blocks[0] + ' ' + blocks[1][:2] + '**' + ' ' + '****' + ' ' + blocks[-1]
    else:
        masked_number = "**" + digits_only[2:6]
    return masked_number


def get_card_name(card):
    """берет значение по ключу from и to и возвращает метод платежа"""
    card_name = ''.join(c for c in card if not c.isdigit())
    return card_name.strip()


def main(dict):
    """выводит последних 5 выполненных операций и соединяет все функции воедино в заданном формате"""
    for i in range(len(dict)):
        print(dict[i]['date'], dict[i]['description'])
        print(get_card_name(dict[i]['from']), mask_card_number(dict[i]['from']), '->', get_card_name(dict[i]['to']),
              mask_card_number(dict[i]['to']))
        print(dict[i]['operationAmount']['amount'], dict[i]['operationAmount']['currency']['name'], '\n')

d1 = executed_operations(data)
d1 = convert_date(d1)
d1 = print_last_5_operations(d1)
main(d1)