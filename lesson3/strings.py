userInput = input('Type a number or phrase\n'
                  '>>>')  # строка пользователя

test = userInput.lower().replace(' ', '').replace(',', '').replace('.', '').replace(':', '').replace(';', '') \
    .replace('!', '').replace('?', '').replace('-', '').replace('\t', '').replace("'", '').replace('"', '')
# перенос в нижний регистр,замена знаков препинания,переносов и пробелов для создания сплошной строки

# проверка сравниванием, являеться ли данная строка палиндромом
if test[::-1] == test:  # test[::-1] - строка наоборот
    print('Palindrome')
else:
    print('Not a palindrome')
