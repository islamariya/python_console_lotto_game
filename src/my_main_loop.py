import datetime


class Order(object):
    """represents each paid order, 2 dishes max """
    id: int
    dish_1: object.__class__Dish
    dish_2: object.__class__Dish

    cooking_time: datetime
    # как сделать? или str где оно используется и для чего нужно

    # результат функции строка 25
    is_ready: bool
    liquidation_time_oven: datetime
    liquidation_time_pick_point: datetime
    is_received: bool
    is_order_thrown_out: bool
    is_order_closed: bool

    #выдача
    pick_point = id
    delivery_time: datetime

    def is_order_ready(self):
        """Boolean. Если оба блюда готовы, то готово, можно выдавать. ? Как проставляется. След шаг: отправь на
        телевизор, запусти таймеер"""
        pass

    def inform_tv_order_is_ready(self):
        """отправляет сигнал о готовности блюда на телевизор, после этого запускает таймер отчета времени на
        забор заказа"""
        pass

    def set_oven_timer_for_liquidation(self):
        """запускает таймер на ликвидацию зазака. 30 минут с момента. 30 минут хранится в переменной settings.py
        Таймер делаем отдельным воркером (потоком)? """
        pass

    def barcode_alarm_handler(self):
        """ Блок функций, позволяющийЖ
         - идентифицировать баркод и выполненный заказ;
         - присвоить заказу номер ячейки;
         - обнулить датчик
         - сформировать джижение манипулятра от последней точки до пункта упаковки
         - упаковка товара
         - погружение в ячейку выдачи
         - сингалы ячейки
         - запуск таймера на ликвидацию ячейк выдачи
          :return self.pick_point
        """
        pass

    def notification_tv(self):
        """Фнукция уведоммлений о том, что заказ еще не получен, повторное объявление на TV."""
        pass

    def order_delivered(self):
        """Меняет статус заказа доставлен, обнуляет счетчики"""
        pass

    def pickup_point_checking(self):
        """Проверяет забран ли заказ, вне блока
        должно посылать сигнал о том, что заказ забрали (изменить статус)"""
        pass

    def order_closing(self):
        """функция обрабатывает закрытие заказа после получения покупателем. Что тут делаем? Как записываем в бд,
        удаляем сами объект или ждем сборщика мусора?"""
        pass


class Dish(object):
    """Класс описывает каждое изготавливаемое блюдо"""
    id: int

    dough: object
    sauce: object
    filling: object
    additive: object

    oven_reserved: object
    pass

class Dough(object):
    """Класс описывает конкретное тесто в определенном блюде заказа"""

