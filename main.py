
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


# set require version
kivy.require("1.9.0")

# словарь rus
data_num_rus = {
    '0': '',
    '1': 'Один',
    'odna': 'Одна',
    '2': 'Два',
    'dve': 'Две',
    '3': 'Три',
    '4': 'Четыре',
    '5': 'Пять',
    '6': 'Шесть',
    '7': 'Семь',
    '8': 'Восемь',
    '9': 'Девять',
    '10': 'Десять',
    '11': 'Одиннадцать',
    '12': 'Двенадцать',
    '13': 'Тринадцать',
    '14': 'Четырнадцать',
    '15': 'Пятнадцать',
    '16': 'Шестнадцать',
    '17': 'Семнадцать',
    '18': 'Восемнадцать',
    '19': 'Девятнадцать',
    '20': 'Двадцать',
    '30': 'Тридцать',
    '40': 'Сорок',
    '50': 'Пятьдесят',
    '60': 'Шестьдесят',
    '70': 'Семьдесят',
    '80': 'Восемьдесят',
    '90': 'Девяносто',
    '100': 'Сто',
    '200': 'Двести',
    '300': 'Триста',
    '400': 'Четыреста',
    '500': 'Пятьсот',
    '600': 'Шестьсот',
    '700': 'Семьсот',
    '800': 'Восемьсот',
    '900': 'Девятьсот',
    '1000': 'Одна тысяча',
    '2000': "Две тысячи",
    '3000': "Три тысячи",
    '4000': "Четыре тысячи",
    'qRk': "тысячь",
    'qQk': "тысяча",
    'qTk': "тысячи"

}
# dictionary ukr
data_num_ukr = {
    '0': '',
    '1': 'Один',
    'odna': 'Одна',
    '2': 'Два',
    'dve': 'Дві',
    '3': 'Три',
    '4': 'Чотири',
    '5': 'П\'ять',
    '6': 'Шість',
    '7': 'Сім',
    '8': 'Вісім',
    '9': 'Дев\'ять',
    '10': 'Десят',
    '11': 'Одинадцять',
    '12': 'Дванадцять',
    '13': 'Тринадцять',
    '14': 'Чотирнадцять',
    '15': 'П\'ятнадцять',
    '16': 'Шістнадцять',
    '17': 'Сімнадцять',
    '18': 'Вісімнадцять',
    '19': 'Дев\'ятнадцять',
    '20': 'Двадцять',
    '30': 'Тридцять',
    '40': 'Сорок',
    '50': 'П\'ятдесят',
    '60': 'Шістдесят',
    '70': 'Сімдесят',
    '80': 'Вісімдесят',
    '90': 'Дев\'яносто',
    '100': 'Сто',
    '200': 'Двісті',
    '300': 'Триста',
    '400': 'Чотириста',
    '500': 'П\'ятсот',
    '600': 'Шістсот',
    '700': 'Сімсот',
    '800': 'Вісімсот',
    '900': 'Дев\'ятсот',
    '1000': 'Одна тисяча',
    '2000': 'Дві тисячі',
    '3000': 'Три тисячі',
    '4000': 'Чотири тисячі',
    'qRk': "тисяч",
    'qQk': "тисяча",
    'qTk': "тисячі"

}
# English
data_num_eng = {
    '0': '',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
    '20': 'Twenty',
    '30': 'Thirty',
    '40': 'Forty',
    '50': 'Fifty',
    '60': 'Sixty',
    '70': 'Seventy',
    '80': 'Eighty',
    '90': 'Ninety',
    '100': 'One hundred',
    '200': 'Two hundred',
    '300': 'Three hundred',
    '400': 'Four hundred',
    '500': 'Five hundred',
    '600': 'Six hundred',
    '700': 'Seven hundred',
    '800': 'Eight hundred',
    '900': 'Nine hundred',
    '1000': 'One thousand',
    'qRk': "thousand"
}
# класс поиска числа в библиотека и ретурн его прописью


class ChekNum():

    def getChekNum(self, num, numDict):  # числа надо получить строка

        self.num = str(num)
        self.numDict = numDict

        # --- chek num in numDict
        for i in self.num:
            # если ввод содержит символы буквы
            if not i.isdigit():
                z = 'Ввод только число!!!'
                return z
            if int(self.num[0]) == 0:
                txt_not_null = "Not start 0 !!!"
                return txt_not_null

        # если число в базе возврат числа из базы и окно зеленое
        if self.num in numDict:
            return str(numDict[self.num])

        # если нет в базе - проверяем на длину число - если десятичное (22,55,99)
        if self.num not in numDict:
            if len(self.num) == 2:
                self.num1 = num[0]+'0'
                self.num2 = num[1]
                return self.numDict[self.num1] + ' ' + self.numDict[self.num2]

            # если число сотни 100.101.111.150.199.999
            if len(self.num) == 3:
                # выделяем разряд сотен из 560 = 500
                self.num1 = num[0] + '00'  # сотни
                # если десятки из сотни (550) есть в базе 20,30,40,50....90
                if (num[1] + num[2]) in numDict:
                    # получаем из словаря значение и присваиваем переменной Z
                    z = self.numDict.get(self.num1)  # #единицы
                    return z + ' ' + self.numDict[(num[1] + num[2])]
                # если десяток нет в базе и десятки не начинаются с 0 = 21,23, и НЕ 01,03
                if (num[1] + num[2]) not in numDict and int(num[1]) != 0:
                    # выделяем десяток из числа (551 = десяток 50)
                    self.num2 = num[1] + '0'
                    # выделяем единицы из числа 557 = единицы 7
                    self.num3 = num[2]  # единицы
                    return self.numDict[self.num1] + ' ' + self.numDict[self.num2] + ' ' + self.numDict[self.num3]
                # если в сотне - десятки начинаются с 0..... 101,201,909
                if int(num[1]) == 0:
                    # выделяем единицы из числа 707 = единицы 7.....self.num1 = num[0] + '00' выше сделали
                    self.num3 = num[2]  # единицы
                    return self.numDict[self.num1] + ' ' + self.numDict[self.num3]
# # ---- тысячи

            if len(self.num) == 4:
                # [9]811 тысячи
                if (self.num[0] + '000') not in numDict:
                    self.zNum1 = self.numDict[num[0]] + \
                        ' ' + self.numDict['qRk']
                if (self.num[0] + '000') in numDict:
                    self.zNum1 = self.numDict[(self.num[0] + '000')]

                # 9[811] сотни
                if (self.num[1] + '00') in numDict:
                    self.zNum2 = self.numDict[(self.num[1] + '00')]
                if int(self.num[1]) == 0:
                    self.zNum2 = self.numDict[self.num[1]]

                # 98[11] десятки/единицы
                # если срез num[2:]) <= 19:
                if int(self.num[2:]) <= 19:
                    # если num[2]) = 0 то просто выбор из базы по последнему знаку:
                    if int(self.num[2]) == 0:
                        self.zNum3 = self.numDict[self.num[3]]
                    # если срез num[2:]) НЕ = 0 берем из базы:
                    else:
                        self.zNum3 = self.numDict[self.num[2:]]
                # если срез num[2:] >= 20:
                if int(self.num[2:]) >= 20:
                    # если срез num[2:] есть в базе - берем из базы:
                    if self.num[2:] in self.numDict:
                        self.zNum3 = self.numDict[self.num[2:]]
                    # если срез num[2:] НЕТ в базе - состовляем из базы число 2х значное:
                    else:
                        self.zNum3 = self.numDict[(self.num[2] + '0')] + ' ' + \
                            self.numDict[self.num[3]]
                # возврат числа прописью
                return self.zNum1 + ' ' + self.zNum2 + ' ' + self.zNum3
# ---- десятки тысяч
            if len(self.num) == 5:
                # [21]000 тысячи ровные
                if (self.num[0:2]) in numDict:
                    self.zNum1 = self.numDict[num[0:2]] + \
                        ' ' + self.numDict['qRk']

                if (self.num[0:2]) not in numDict and self.numDict == data_num_rus or (self.num[0:2]) not in numDict and self.numDict == data_num_ukr:
                    # if self.num[0:2] not in numDict and self.numDict == data_num_rus or self.numDict == data_num_ukr:
                    if self.num[1] == '1':
                        self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                            self.numDict['odna'] + \
                            ' ' + self.numDict['qQk']
                    if self.num[1] == '2':
                        self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                            self.numDict['dve'] + \
                            ' ' + self.numDict['qTk']
                    if self.num[1] == '3':
                        self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                            self.numDict['3'] + \
                            ' ' + self.numDict['qTk']
                    if self.num[1] == '4':
                        self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                            self.numDict['4'] + \
                            ' ' + self.numDict['qTk']
                    if int(self.num[1]) >= 5:
                        self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                            self.numDict[self.num[1]] + \
                            ' ' + self.numDict['qRk']

                if self.num[0:2] not in numDict and self.numDict == data_num_eng:
                    self.zNum1 = self.numDict[self.num[0]+'0'] + ' ' + \
                        self.numDict[self.num[1]] + \
                        ' ' + self.numDict['qRk']

                if int(self.num[2:]) != 000:
                    self.zNum1 = "Нет числа в базе!!!"

                return self.zNum1

            if len(self.num) > 5:
                self.zNum1 = "Нет числа в базе!!!"
                return self.zNum1

        # если не нашел число в базе - проверив все верхние методы
        if self.num not in numDict:
            self.zNum1 = "Нет числа в базе!!!"
            return self.zNum1


class myNumsApp(App):
    icon = 'free-icon-origami-4582876.png'
    # self.num_from_key - храним в этой переменной число с клавиш
    # очищает все вводные

    def update_exitlabel(self, instance):
        if instance.text == 'Clear':
            self.root.ids.input.text = ""
        else:
            # получаем число  на ввод
            self.num_from_key += str(instance.text)
            self.root.ids.input.text = self.num_from_key

        print(self.num_from_key)

    def update_num_str(self):
        # получаем число  на ввод
        self.num = str(self.num_from_key)
        # получаем число прописью из словаря
        self.txt_num_from_dict = str(self.x.getChekNum(
            self.num, self.lang_dict))
        print('self.txt_num_from_dict', self.txt_num_from_dict)

        if len(self.num) == 0:
            self.root.ids.exitlabel.color = .83, 0, 0, 1
            if self.lang_dict == data_num_rus:
                self.root.ids.exitlabel.text = "Введите число"
                # self.clear_num()
                self.clear()
                return self.root.ids.exitlabel.text
            if self.lang_dict == data_num_ukr:
                self.root.ids.exitlabel.text = "Введіть число"
                # self.clear_num()
                self.clear()
                return self.root.ids.exitlabel.text
            if self.lang_dict == data_num_eng:
                self.root.ids.exitlabel.text = "ENTER NUMBER"
                # self.clear_num()
                self.clear()
                return self.root.ids.exitlabel.text

        if self.txt_num_from_dict == "Not start 0 !!!":
            self.root.ids.exitlabel.color = .83, 0, 0, 1
            if self.lang_dict == data_num_eng:
                self.root.ids.exitlabel.text = "Not start 0 !!!"
                # self.root.ids.input.text = ""
                # self.num_from_key = ''
                # self.clear()
                return self.root.ids.exitlabel.text
            if self.lang_dict == data_num_rus or self.lang_dict == data_num_ukr:
                self.root.ids.exitlabel.text = "Не с Нуля !"
                # self.clear()
                return self.root.ids.exitlabel.text

        if self.txt_num_from_dict == "Ввод только число!!!":
            self.root.ids.exitlabel.color = .83, 0, 0, 1
            self.root.ids.exitlabel.text = str(self.x.getChekNum(
                self.num, self.lang_dict))

        if self.txt_num_from_dict == "Нет числа в базе!!!":
            self.root.ids.exitlabel.color = .83, 0, 0, 1
            if self.lang_dict == data_num_eng:
                self.root.ids.exitlabel.text = 'Not Number In Base !!!'
                return self.root.ids.exitlabel.text
            if self.lang_dict == data_num_ukr:
                self.root.ids.exitlabel.text = 'Немає числа в базі !!!'
                return self.root.ids.exitlabel.text

            self.root.ids.exitlabel.text = str(self.x.getChekNum(
                self.num, self.lang_dict))

        else:
            self.root.ids.exitlabel.text = str(self.x.getChekNum(
                self.num, self.lang_dict))

    # def clear_txt_input(self):
    #     # self.num_from_key = ''
    #     # self.num = ''
    #     self.root.ids.input.text = ''
    #     self.root.ids.russl.active = False
    #     self.root.ids.ukrl.active = False
    #     self.root.ids.engl.active = False
    #     self.root.ids.langlabel.text = ''
    #     self.root.ids.exitlabel.text = ''
    #     self.root.ids.exitlabel.color = .0, .75, .69, 1

    # clear self.num = ''
    # def clear_num(self):
    #     self.num = ''

    def clear(self):
        self.num_from_key = ''
        self.num = ''
        self.root.ids.input.text = ''
        self.root.ids.russl.active = False
        self.root.ids.ukrl.active = False
        self.root.ids.engl.active = False
        self.root.ids.langlabel.text = ''
        # self.root.ids.exitlabel.text = ''
        # self.root.ids.exitlabel.color = .0, .75, .69, 1

    def clear_all(self, instance):
        self.num_from_key = ''
        self.num = ''
        self.root.ids.input.text = ''
        self.root.ids.russl.active = False
        self.root.ids.ukrl.active = False
        self.root.ids.engl.active = False
        self.root.ids.langlabel.text = ''
        self.root.ids.exitlabel.text = ''
        self.root.ids.exitlabel.color = .0, .75, .69, 1

    def checkbox_click(self, value):

        if value == 1:
            self.root.ids.langlabel.text = 'Русский Язык'
            self.lang_dict = data_num_rus
            self.update_num_str()

        if value == 2:
            self.root.ids.langlabel.text = 'Українська Мова'
            self.lang_dict = data_num_ukr
            self.update_num_str()

        if value == 3:
            self.root.ids.langlabel.text = 'English'
            self.lang_dict = data_num_eng
            self.update_num_str()

    def build(self):
        self.title = "Num-->Txt"
        self.x = ChekNum()
        self.num_from_key = ''
        self.num = ''
        return MyMainBoxLayout()


class MyMainBoxLayout(BoxLayout):
    pass


# Rum the app
root = myNumsApp()
root.run()
