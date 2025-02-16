# # string1 = input.txt("введите первую строку: ")
# # string2 = input.txt("введите вторую строку: ")
# # result = string1 < string2
# # print(result)
#
#
#
# # string = input.txt("Введите строку: ")
# # words_count = len(string.split())
# # print(words_count)
#
#
# # a=int(input.txt("возраст"))
# # if a>=18:
# #     print("да ")
# # else:
# #     print("возможно но потом ")
#
#
# # temperature=float(input.txt("термература: "))
# #
# # if temperature<0:
# #     print("холодно,лучше сидеть дома ")
# # elif temperature<10:
# #     print("холодно но не очень но лучше сидеть дома ")
# # elif temperature<15:
# #     print("можно идти гулять в шапке ")
# # elif temperature<25:
# #     print("можно идти гулять без шапки ")
# # else:
# #     print("тепло")
#
# # a=int(input.txt("число "))
# # if a%2==0:
# #     print("парное")
# # else:
# #     print("непарное")
#
#
# # a=30
# # b=10
# # c=60
# # min=a
# # if b<min:
# #     min=b
# # if c<min:
# #     min=c
# # print(min)
#
#
# # a=100
# # b=50
# # c=70
# # mid=a
# # if a>b:
# #     mid=b
# # if b>c:
# #     mid=c
# # else:
# #     mid=a
# # print(mid)
#
# # Арифметичні дії над числами пронумеровані таким чином:
# # 1 — додавання, 2 — віднімання, 3 — множення, 4 — ділення.
# # Дано номер дії N (ціле число в діапазоні 1–4) та дійсні числа A та B (B не дорівнює 0).
# # Виконати над числами вказану дію та вивести результат.
# # a=2
# # b=5
# # dog=int(input.txt("номер "))
# # while True:
# #     if dog==1:
# #         print(a+b)
# #     elif dog==2:
# #         print(a-b)
# #     elif dog==3:
# #         print(a*b)
# #     elif dog==4:
# #         print(a/b)
# #     else:
# #         print("неправильное число ")
# #
#
# # num = int(input.txt("Введіть ціле число (1-999): "))
# #
# # if 1 <= num <= 999:
# #     parity = "парне" if num % 2 == 0 else "непарне"
# #     if num < 10:
# #         digits = "однозначне"
# #     elif num < 100:
# #         digits = "двозначне"
# #     else:
# #         digits = "тризначне"
# #     print(f"{parity} {digits} число")
# # else:
# #     print("Число не в діапазоні 1-999.")
#
# # 1. Дано три числа. Знайти середнє з них
# # (тобто число, розташоване між найменшим та найбільшим).
#
# # a=5
# # b=10
# # c=15
# # min=a
# # max=a
# # mid=a
# # if a<min:
# #     min=a
# # if b<min:
# #     min=b
# # if c<min:
# #     min=c
# #
# # if a>max:
# #     max=a
# # if b>max:
# #     max=b
# # if c>max:
# #     max=c
# #
# # if max!=a:
# #     if min!=a:
# #         mid=a
# # if max!=b:
# #     if min!=b:
# #         mid=b
# # if max!=c:
# #     if min!=c:
# #         mid=c
# # print("среднее",mid,"минимальное",min,"максимальное",max)
#
# # Завдання 1: Перевірте, чи є введене число додатним, від'ємним або нулем:
#
# # a=int(input.txt("num "))
# # if a>0:
# #     print("+")
# # elif a<0:
# #     print("-")
# # else:
# #     print("0")
#
# # Завдання 2: Обчисліть оцінки студента залежно від його заробітку,
# # наприклад оцінка 1 - заробіток 1000, оцінка 2 заробіток 2000 і так далі.
#
# # a=int(input.txt("сколько заработал??? "))
# # b=a//1000
# # print(b)
# # Використати блок “else”
# # щоб вивести повідомлення
# # “Завершено” після успішного виходу з циклу (довільний)
# # a=[12,10,8,6,4,2,0]
# # for i in a:
# #     print(i)
# # else:
# #     print("конец.")
# # Дано діапазон чисел
# # (Користувач обирає сам (input.txt)).
# # Вивести на екран лише непарні числа і 0 (в кінці)
# # a=int(input.txt("start"))
# # b=int(input.txt("finish"))
# # for i in range(a,b):
# #     if i%2!=0:
# #         print(i)
# # else:
# #     print(0)
# # Написати програму, яка зчитає 3 числа
# # (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”
# # a=1
# # b=14
# # c=4
# # d=0
# # for i in range(a,b):
# #     if i%c==0:
# #         d=d+1
# # print(d)
# # Знайдіть суму перших a натуральних чисел(число A вводить користувач)
# # a=int(input.txt("число "))
# # b=0
# # for i in range(0,a):
# #     b+=i
# # print(b)
# # Користувач вводить N, програма обчислює суму перших N чисел послідовності Фібоначчі.
# # a=int(input.txt("число "))
# # b=0
# # c=1
# # d=0
# # print(b,c)
# # for i in range(0,a):
# #     d=b+c
# #     b=c
# #     c=d
# #     print(d)
#
# # Написати програму, яка рахує суму всіх елементів у списку.
# # a=[145,279,333,5]
# # b=1
# # for i in a:
# #     b*=i
# # print(b)
# # Написати програму, яка рахує добуток усіх елементів у списку.
# # Написати програму, що перевірити порожній список чи ні.
# # a=[]
# # if not a:
# #     print("пусто ")
# # else:
# #     print("не пусто ")
# # Піднести кожен із елементів списку до куба
# # a=[10,30,50]
# # b=[]
# # for i in a:
# #     b=i**3
# # print(b)
# # a=[1,10,5,20]
# # b=a[1]
# # for i in a:
# #     if a[0] < b:
# #         b = a[0]
# #     if a[1] < b:
# #         b = a[1]
# #     if c < :
# #          = c
# #
# #
# #
# # import random
# # while True:
# #     number1=random.randint(1,100)
# #     number2=random.randint(1,100)
# #     # result=number1+number2
# #
# #     da=["+","-","*","/"]
# #     net=random.choice(da)
# #     result=eval(f"{number1}{net}{number2}")
# #     a=f"{number1}{net}{number2}="
# #     b=int(input.txt(a))
# #     if b==result:
# #         print("молодец ")
# #         print()
# #     else:
# #         print("!молодец")
# #         print()
#
# # 1.Написати програму, яка отримує мінімальне число зі списку.
# # a=[10,20,30,40,10,5]
# # b=a[0]
# # for i in a:
# #     if i<b:
# #         b=i
# # print(b)
#
# # 2.Написати програму, що порахує кількість додатніх елементів та кількість від'ємних у списку
# # a=[3,10,15,-10,-40]
# # minus=0
# # plus=0
# # for i in a:
# #     if i>0:
# #         plus+=1
# #     elif i<0:
# #         minus+=1
# # print(minus,plus)
#
# # 3. Піднести кожен із елементів списку до куба
# # a=[3,5,10,12]
# # for i in a:
# #     print(i*i*i)
#
# # Написати to-do програму, що дає можливість користувачеві
# # вводити нові завдання на сьогодні, допоки користувач не введе “q”.
# # Після виходу з циклу — виводяться всі завдання у форматі:
# # 1 Помити посуд
# # 2 Сходити в магазин.
# # 3 Відвідати урок Osvitech.
# # b=[]
# # c=1
# # while True:
# #     a=input.txt()
# #     if a=="1":
# #         b.append(input.txt())
# #         print(b)
# #     if a=="2":
# #         print("сходить в магазин ")
# #     if a=="3":
# #         for i in b:
# #             print(str(c),i)
# #             c+=1
# #     if a=="q":
# #         break
# # first_list=[]
# # second_list=[]
# # while True:
# #     a=input.txt("число:")
# #     if a=="stop":
# #         break
# #     first_list.append(int(a))
# # print(first_list)
# # for i in first_list:
# #     if i%2==0:
# #         second_list.append(i)
# # print(first_list,second_list)
# # import random
# # print("число сиди между 1-100,угадываю :)")
# # a=random.randint(1,100)
# # while True:
# #     b=int(input.txt("число: "))
# #     if a==b:
# #         print("молодец ")
# #         a=random.randint(1,100)
# #     else:
# #         if a<b:
# #             print("меньше \n!молодец ")
# #         if a>b:
# #             print("больше \n!молодец ")
# # import random
# # a=["кот","кит","пёс","змея"]
# # b=random.choice(a)
# # c="_"*len(b)
# # print("слово загадано твоя миссия его отгадать!!!!!!!!!!!!!!! ")
# # print(c)
# # result=[]
# # while True:
# #     d=input.txt("буква: ")
# #     if d in b and not result:
# #
# #         for i in b:
# #             if d==i:
# #                 result.append(d)
# #             else:
# #                 result.append("_")
# #     if d in b:
# #         j=0
# #         for i in b:
# #             if d==i:
# #                 result[j]=d
# #             j+=1
# #     print(*result)
# # Створіть програму, яка приймає від користувача дві строки та перетворює їх у список,
# # де перший елемент — це перша літера першої строки, другий елемент
# # — друга літера першої строки, третій елемент — перша літера другої строки, четвертий
# # — друга літера другої строки і т.д. Виведіть цей список.
# # a=input.txt()
# # b=input.txt()
# # c=[]
# # while
# # c.append(a[0])
# # c.append(a[1])
# # c.append(b[0])
# # c.append(b[1])
# # print(c)
#
#
#
# # Створіть програму, яка приймає від користувача дві строки
# # та знаходить найбільший загальний підрядок у цих строках.
# # Виведіть цей підрядок.
# # a="собака сьела птицу"
# # # b=input.txt()
# # c=""
# # d=0
# # e=""
# # for i in a:
# #     if i!=" ":
# #         c+=i
# #     else:
# #         print(c)
# #         if len(c)>d:
# #             d=len(c)
# #             e=c
# #
# #
# #         c=""
# # print(c,d,e)
#
#
#
#
#
#
#
#
#
#
#
#
# # Створіть рядок та використайте зрізи для виводу перших трьох та останніх трьох символів.
# # a="собака сьела птицу"
# # print(a[0:3])
# # print(a[-3:])
# # Створіть множину, яка містить у собі числа від 1 до 20. Використовуючи методи множин,
# # створіть дві нові множини - одну з парними числами, іншу з непарними числами.
# # a=set(range(1,21))
# # b=set()
# # c=set()
# # for i in a:
# #     if i%2==0:
# #         b.add(i)
# #     else:
# #         c.add(i)
# # print(a,b,c)
#
#
#
# # Дано рядок, який містить довільне речення, слова в якому розділені пробілами.
# # З використанням зрізів знайти і вивести слово, як має найбільшу довжину.
# # a=""
#
#
# # Створіть список зі стрічок та використайте зрізи для виводу останніх трьох
# # символів з кожної стрічки.
#
# # a=["собака","сыр","вода","hello"]
# # for i in a:
# #     print(i[-3:])
#
# # Створіть список зі стрічок
# # та використайте зрізи для виводу символів з кожної стрічки у зворотньому порядку.
# # a=["собака","сыр","вода","hello"]
# # for i in a:
# #     print(i[::-1])
#
# # Створіть список, який містить у собі 10 стрічок, які складаються з двох слів,
# # розділених пробілом. Використовуючи зрізи,
# # виведіть на екран кожне слово з кожної стрічки у зворотньому порядку.
# # a=["сыр молоко","вода вода","собака мясо","кошка кот","мороженок холодильник",
# #    "карандаш ручка","листок запись","врач дежурство","сериал попкорн","англиский язык"]
# # b=[]
# # c=[]
# # for i in a:
# #     c=i.split()
# #     b.extend(c)
# #
# # for y in b:
# #     print(y[::-1])
#
#
# # Задано список чисел.Потрібно визначити,
# # які числа з цього списку є паліндромами
# # (тобто, їх можна прочитати однаково зліва направо і справа наліво).
#
# # a=[121,100,101,209,5]
# # for i in a:
# #     str(i)
# #     if str(i)==str(i)[::-1]:
# #         print(i)
#
# # Написати програму генератор пароля,
# # яка просить користувача надати довжину бажаного пароля.
# # import random
# # a=int(input.txt("сколько цифр:"))
# # b="123456789abcdefghijklmnopqrstuvwxyz"
# # d=""
# # for i in range(a):
# #     c = random.choice(b)
# #     d=c+d
# # print(d)
#
#
#
# # Користувач вводить рядок тексту,
# # програма знаходить унікальні символи у цьому рядку та виводить їх.
# # a=input.txt()
# # b=""
# # for i in a:
# #     if i not in b:
# #         b+=i
# # print(b)
# # Користувач вводить рядок тексту, програма знаходить всі слова,
# # які зустрічаються у рядку більше одного разу, та виводить їх.
# # a=input.txt()
# # b=a.split()
# # for i in b:
# #     if b.count(i)>1:
# #         print(b.count(i))
# #         print(i)
# # print(b)
# # Користувач вводить рядок тексту та символ-роздільник.
# # Програма розбиває рядок на підслова за
# # допомогою введеного символу-роздільника та виводить отримані підслова
# # a=input.txt()
# # b=input.txt()
# # c=a.split(b)
# # print(c)
#
#
# # import random
# # b=["камень","ножницы","бумага"]
# # while True:
# #     a=input.txt("камень,ножницы или бумага? ")
# #     c=random.choice(b)
# #     if a==c:
# #         print("!молодец")
# #         print(a, c)
# #     if a=="камень" and c=="ножницы":
# #         print("молодец")
# #         print(a,c)
# #     if a=="ножницы" and c=="бумага":
# #         print("молодец")
# #         print(a, c)
# #     if a == "бумага" and c == "камень":
# #         print("молодец")
# #         print(a, c)
# #     if a == "ножницы" and c == "камень":
# #         print("!молодец")
# #         print(a,c)
# #     if a == "бумага" and c == "ножницы":
# #         print("!молодец")
# #         print(a,c)
# #     if a == "камень" and c == "бумага":
# #         print("!молодец")
# #         print(a,c)
#
# # def a(b):
# #     c=["а","и","е","у","о","ы","ё","ю","я","э"]
# #     e=0
# #     for i in b:
# #         if i in c:
# #             e+=1
# #     print(e)
# # b=input.txt()
# # a(b)
#
# # def count(a,b):
# #     print(a+b)
# #
# # a=int(input.txt())
# # b=int(input.txt())
# # count(a,b)
#
# # def a(b):
# #     c=b[0]
# #     for i in b:
# #         if i>c:
# #             c=i
# #     print(c)
# # b=[10,20,40,9]
# # a(b)
#
# # def a(b):
# #     # c=[]
# #     d=0
# #     for i in b:
# #         # c.append(i**2)
# #         d+=i**2
# #     print(d)
# # b=[10,30,50]
# # a(b)
#
# # import random
# # a=["сколько весит килограм асфальта??","почему солнце желтое??"]
# # b=["килограм","потому сто"]
# # d=random.choice(a)
# # print(d)
# # c=input.txt("ваш ответ: ")
# # e=a.index(d)
# # f=b[e]
# # if c==f:
# #     print("молодец")
# # else:
# #     print("!молодец")
#
# # def a(b,c):
# #     c=b[::-1]
# #     print(c)
# # b=input.txt()
# # c=""
# # a(b,c)
#
# # def a(b):
# #     for i in range(b):
# #         print("*"*i)
# # b=int(input.txt())
# # a(b)
#
# # def a(b):
# #     c=b[0]
# #     for i in b:
# #         if i>c:
# #             c=i
# #     return c
# # b=[10,20,40,9]
# # d=a(b)
# # print(d)
#
# def plus(a,b):
#     p=a+b
#     return p
# def minus(a,b):
#     m=a-b
#     return m
# def dl(a,b):
#     d=a//b
#     return d
# def um(a,b):
#     u=a*b
#     return u
# a=int(input.txt("первое число: "))
# b=int(input.txt("второе число: "))
# c=input.txt("символ: ")
# if c=="+":
#     print(plus(a, b))
# elif c=="-":
#     print(minus(a, b))
# elif c=="/":
#     print(dl(a, b))
# elif c=="*":
#     print(um(a, b))
# else:
#     print("!правильно")
#
# delete=[]
# fridge=["молоко","сыр","мороженое"]
#
# cat=int(input.txt())
#
# if cat==1:
#     print(fridge)
# elif cat==2:
#     fridge.append(input.txt())
#     print(fridge)
# elif cat==3:
#     delete.append(fridge.pop(int(input.txt())))
#     print(fridge,delete)
# elif cat==4:
#     fridge.insert(int(input.txt()),input.txt())
#     print(fridge)
# elif cat==5:
#     print(delete)
# elif cat==6:
#     delete.reverse()
#     print(delete)
#
# def s(a):
#     b=0
#     c=[]
#     for i in a:
#         b+=i
#         c=b/len(a)
#     return c
# a=[20,30,50,100]
# d=s(a)
# print(d)
# import random
# c=5
# b=random.randint(0,c)
# d=random.randint(0,c)
# e=10
# print("найти сокровище,10 попыток чтобы найти ")
# while e>0:
#     a=int(input.txt())
#     f=int(input.txt())
#     if a>c or a<0 or f>c or f<0:
#         print("!молодец")
#     if b==a and d==f:
#         print("big молодец")
#         break
#     else:
#
#         if a>b:
#             print("выше")
#
#         if a<b:
#             print("ниже")
#         if f>d:
#             print("левее")
#         if f<d:
#             print("правее")
#         e-=1
# if e==0:
#     print("тупой не понимаешь ничего,попытки закончились")

# def a():
#     print("что то ")
# a()

# def a():
# #     b=1
# #     return b
# # c=a()
# # print(a())

# Написати функцію, яка приймає список і
# повертає кількість елементів у цьому списку,
# що більші за середнє значення списку.

# def a(b):
#     c=0
#     for i in b:
#         c+=i
#     d=c/len(b)
#     e=0
#     for i in b:
#         if i>d:
#             e+=1
#     return e
#
# b=[10,20,40,50]
# f=a(b)
# print(f)

# Написати функцію, яка приймає список рядків та повертає новий список,
# який містить тільки ті рядки,
# що складаються тільки з літер або цифр.

# def a(b):
#     c=0
#     d=0
#     for i in b:
#         for q in i:
#             if 'a' <= q <= 'z':
#             # if 'a' <= q <= 'z' and not ('0' <= q <= '9'):
#                 c += 1
#             if "0" <= q <= "9":
#             # if "0" <= q <= "9" and not ('a' <= q <= 'z'):
#                 d += 1
#         if c == len(i):
#             print(i)
#         if d == len(i):
#             print(i)
#         c=0
#         d=0
# b=["abcd","a1b2c3d4","1234"]
# a(b)

# def a(b,c):
#     d=0
#     for i in b:
#         d+=i
#     for q in c:
#         d+=q
#     return d
# b=[103,234,987]
# c=[40,213,456]
# e=a(b,c)
# print(e)

# def a(b):
#     c=0
#     d=0
#     for i in b:
#         for q in i:
#             if 'a' <= q <= 'z':
#             # if 'a' <= q <= 'z' and not ('0' <= q <= '9'):
#                 c += 1
#             if "0" <= q <= "9":
#             # if "0" <= q <= "9" and not ('a' <= q <= 'z'):
#                 d += 1
#         if c == len(i):
#             print(i)
#         if d == len(i):
#             print(i)
#         c=0
#         d=0
# b=["abcd","a1b2c3d4","1234"]
# a(b)



# def p(a,c):
#     e=a+c
#     return e
# def m(a,c):
#     f=a-c
#     return f
# def u(a,c):
#     g=a*c
#     return g
# def d(a,c):
#     h=a/c
#     return h
# def s(a,c):
#     i=a**c
#     return i
# def k(a):
#     j=a**0.5
#     return j
# def r(a):
#     l=str(a)[::-1]
#     return l
# while True:
#     print("выберите действие для кукулятора ")
#     b=input.txt()
#
#     if b == "+":
#         a=int(input.txt())
#         c=int(input.txt())
#         print(p(a,c))
#     elif b == "-":
#         a=int(input.txt())
#         c=int(input.txt())
#         print(m(a,c))
#     elif b == "*":
#         a=int(input.txt())
#         c=int(input.txt())
#         print(u(a,c))
#     elif b == "/":
#         a=int(input.txt())
#         c=int(input.txt())
#         print(d(a,c))
#     elif b == "**":
#         a=int(input.txt())
#         c=int(input.txt())
#         print(s(a,c))
#     elif b == "1/2":
#         a=int(input.txt())
#         print(k(a))
#     elif b == "r":
#         a=int(input.txt())
#         print(r(a))
#     else:
#         print("!правильное действие")

# def p(a):
#     if a==a[::-1]:
#         print("палендром")
#     else:
#         print("не палендром")
#
#
# a=input.txt()
# p(a)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
#
# plt.show()

# Напишіть програму, яка зчитує вміст файлу
# "input.txt.txt" і записує його у файл
# "output.txt" з виключенням повторюваних рядків.

# with open("input.txt","r",encoding="utf-8") as file:
#     a=file.readlines()
#
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#         if i in b:
#             pass
# with open("output.txt","w",encoding="utf-8") as file:
#     file.writelines(b)
#     print(b)

# Выписать из первого файла все цифры во второй
with open("input.txt","r",encoding="utf-8") as file:
    a=file.readlines()
    b=[]
    c=["0","1","2","3","4","5","6","7","8","9"]
    for i in a:
        for y in i:
            if y in c:
                b.append(y)
    print(b)
with open("output.txt","w",encoding="utf-8") as file:
    file.writelines(b)


