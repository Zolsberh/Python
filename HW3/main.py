class Acount:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счет №{self.__num} принадлежащий {self.__surname} открыт')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'счет #{self.__num} принадлежащий {self.__surname} был закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    # Получаем данные через get и set
    #################################
    def get_num(self):
        return self.__num

    def get_surname(self):
        return self.__surname

    def get_percent(self):
        return self.__percent

    def get_value(self):
        return self.__value

    def set_num(self, value):
        self.__num = value

    def set_surname(self, value):
        self.__surname = value

    def set_percent(self, value):
        self.__percent = value

    def set_value(self, value):
        self.__value = value
    #################################

    # Получаем данные через свойства
    #################################
    @property
    def num(self):
        return self.__num

    @property
    def surname(self):
        return self.__surname

    @property
    def percent(self):
        return self.__percent

    @property
    def value(self):
        return self.__value

    @num.setter
    def num(self, value):
        self.__num = value

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @percent.setter
    def percent(self, value):
        self.__percent = value

    @value.setter
    def value(self, value):
        self.__value = value
    #################################

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Acount.suffix}')
        else:
            self.__value - val
            print(f'{val} {Acount.suffix} было успешно снято!')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Acount.suffix} было успешно добавлено!')
        self.print_balance()

    def convert_to_usd(self):
        val_usd = Acount.convert(self.__value, Acount.rate_usd)
        print(f'Состояние счета: {val_usd} {Acount.suffix_usd}')

    def convert_to_eur(self):
        val_eur = Acount.convert(self.__value, Acount.rate_eur)
        print(f'Состояние счета: {val_eur} {Acount.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {self.suffix}')

    def print_info(self):
        print(f'#{self.__num}')
        print('-' * 20)
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Процент: {self.__percent: .0%}')
        print('-' * 20)


acc = Acount('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Acount.set_usd_rate(2)
acc.convert_to_usd()
acc.value = 15000
acc.print_info()

