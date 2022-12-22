# userList = []  # Оголошення списку
# while True:  # Початок циклу
#     userNum = (input('Enter num or sum\n'))  # введення користувача
#     try:  # вилов помилок
#         if userNum == 'sum':  # якщо userNum дорівнює 'sum', то цикл закінчується
#             break
#         elif isinstance(float(userNum), float) or isinstance(int(userNum), int):  # якщо введене число є типу float
#             # або int, тоді це число додається до списку і конвертується в тип float
#             userList.append(float(userNum))
#     except ValueError:
#         print('Not a number')  # якщо не є числом або словом 'sum', то помилка і по новому колу
# summary = 0  # оголошення змінної в якій буде сума всіх введених чисел
# for i in userList:  # перебираємо всі числа в userList
#     summary += i  # додаємо в кожній ітерації число
# print(summary)  # вивід на консоль

userList = []  # Оголошення списку
while True:  # Початок циклу
    userNum = input('Enter a number or a word \'sum\'\n')  # введення користувача
    if userNum == 'sum':  # якщо userNum дорівнює 'sum', то цикл закінчується
        break
    elif userNum.replace('.', '', 1).replace('-', '', 1).replace(',', '', 1).isdigit():  # перевірка на число
        # (видаляється лише одна крапка, знак '-' і кома)
        userList.append(float(userNum))  # до списку додається число конвертоване у тип float
        print(userList)
    else:
        print('Error')
summary = 0  # оголошення змінної в якій буде сума всіх введених чисел
for i in userList:  # перебираємо всі числа в userList
    summary += i  # додаємо в кожній ітерації число
print(summary)  # вивід на консоль
