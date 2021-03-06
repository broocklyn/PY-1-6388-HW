
__author__ = 'Учускин Павел Валерьевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits = 0):
    dot = int('1' + '0' * ndigits)
    q = number * dot
    c = int(q)
    lastDigit = int((q - c) * 10)
    if lastDigit >= 5:
        c += 1
    return c/dot  
	
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))




# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	num = str(ticket_number)
	if len(num) == 6:
		sum1 = int(num[0]) + int(num[1]) + int(num[2])
		sum2 = int(num[3]) + int(num[4]) + int(num[5])
		if sum1 == sum2:
			return 'счастливый билетик'
	else: return 'обычный билет'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))