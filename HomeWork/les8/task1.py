"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
 должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
 @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
"""

from datetime import date

class Date:
  @classmethod
  def extract_date(cls, input_date):
    return date(*map(int, reversed((input_date).split("-"))))

  @staticmethod
  def check_date(input_date):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_list = list(map(int, input_date.split('-')))
    assert 1 <= date_list[1] <= 12, 'Month does not exist'
    assert 1 <= date_list[0] <= month[date_list[1]-1], 'Day does not exist'

a = Date()

print(Date.extract_date('08-08-2020'))
print(a.extract_date('07-08-2020'))
print(Date.check_date('31-11-2020'))