alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/'
alfavit_UA = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ1234567890()/'
krok = int(1)
while True:
    message = input("Повідомлення для шифрування:").upper()
    itog = ''
    lang = input('Виберіть мову UA/EN:')
    if lang == 'UA':
       for i in message:
           mesto = alfavit_UA.find(i)
           new_mesto = mesto + krok
           if i in alfavit_UA:
               itog += i
           else:
               itog += i
    else:
        for i in message:
            mesto = alfavit_EN.find(i)
            new_mesto = mesto + krok
            if i in alfavit_EN:
                itog += alfavit_EN[new_mesto]
            else:
                itog += i
    print(itog)