from Flower import dict_of_flowers, Flower


def create_new_flower():
    """
    Функция помогает создать новый вид цветка и вносит его в словарь цветов
    """
    specifications = []
    parameters = ['Название: ', 'Цвет: ', 'Цена: ', 'Количество: ']
    for i in parameters:
        specifications.append(input(i))
    if check_for_new_flower(specifications):
        specifications[2] = int(specifications[2])
        specifications[3] = int(specifications[3])
        new_flower = Flower(*specifications)
        change_dict_of_flowers(new_flower)
        return new_flower
    else:
        print('Вы ввели неверный значения, команда провалена, вид цветка не создан')


def check_for_new_flower(specifications):
    """
    Проверяет верны ли типы введенных характеристик
    Вспомогательная функция для create_new_flower

    :param specifications: характеристики нового цветка
    :return:
    """
    if specifications[0].isalpha() and specifications[1].isalpha() and \
            specifications[2].isdigit() and specifications[3].isdigit():
        return True
    else:
        return False


def change_dict_of_flowers(flower):
    """
    Вносит в словарь новый тип цветка
    Вспомогательная функция для create_new_flower

    :param flower: новый тип цветка, объект класса Flower
    :return:
    """
    dict_of_flowers[flower.name] = {'Название: ': flower.name,
                                    'Цвет: ': flower.color,
                                    'Цена: ': flower.cost,
                                    'Количество: ': flower.count}
    return dict_of_flowers


def make_new_bouquet():
    """
    Функция позволяет составить букет и возвращает его стоимость
    Также она вычитает потраченные цветы из количества цветов в словаре

    :return: цена составленного букета
    """
    order = {}
    print('Введите количество цветов, из которых хотите составить букет')
    for i in dict_of_flowers.keys():
        while not (quantity := (input(f'{i} - '))).isdigit():
            print("Пожалуйста, введите число")
        order[i] = int(quantity)
    for type_fl, characteristic_fl in dict_of_flowers.items():
        if characteristic_fl['Количество: '] < order[type_fl]:
            print(f'У вас недостаточно цветов типа: {type_fl}')
            return 0
    cost = cost_calculation(order) * 1.5
    print(f'Букет составлен, его цена - {cost}')
    recalculating_count_of_flowers_bouquet(order)
    return cost


def cost_calculation(order):
    """
    Высчитывает сумму себестоимости цвтеов
    :param order: заказ цветов
    :return:
    """
    summa = 0
    for k, v in dict_of_flowers.items():
        summa = summa + v['Цена: '] * order[k]
    return summa


def recalculating_count_of_flowers_bouquet(order):
    """
    Уменьшение количества цветов в словаре при создании букета
    :param order: заказ цветов
    :return:
    """
    for k, v in dict_of_flowers.items():
        dict_of_flowers[k]['Количество: '] = v['Количество: '] - order[k]


def buy_in_addition_flowers():
    """
    Функция позволяет увеличить количество уже существующих видов цветов
    Она изменяет их количество в словаре цветов

    :return: затраченные на покупку цветов деньги
    """
    order = {}
    print('Сколько и каких цветов вы желаете докупить?')
    for i in dict_of_flowers.keys():
        while not (quantity := (input(f'{i} - '))).isdigit():
            print("Пожалуйста, введите число")
        order[i] = int(quantity)
    cost = cost_calculation(order)
    print(f'Вы потратили - {cost}')
    recalculating_count_of_flowers_buy_in_addition(order)
    return cost


def recalculating_count_of_flowers_buy_in_addition(order):
    """
    Увеличение количества цветов в словаре при докупки
    :param order: заказ цветов
    :return:
    """
    for k, v in dict_of_flowers.items():
        dict_of_flowers[k]['Количество: '] = v['Количество: '] + order[k]


def main():
    profit = 0
    menu = {
        "1": 'составить и продать букет',
        "2": 'докупить цветы',
        "3": 'узнать информацию о всех цветах',
        "4": 'купить новый вид цветка',
        "5": 'посчитать доход',
        "0": 'Выход',
    }
    for key, value in menu.items():
        print(f'{key} - {value}')

    while (command := input('Введите команду: ')) != '0':
        if command in menu:
            if command == '1':
                cost = make_new_bouquet()
                profit = profit + cost
            if command == '2':
                cost = buy_in_addition_flowers()
                profit = profit - cost
            if command == '3':
                for key, value in dict_of_flowers.items():
                    print(f'{key} - {value}')
            if command == '4':
                create_new_flower()
            if command == '5':
                print(f'Доход {profit}')


if __name__ == '__main__':
    main()
