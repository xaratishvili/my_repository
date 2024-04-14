# 1 ლექცია
# ------------------------------------------------------------------------------------------------------

# სინტაქსი
# print("Hello World")


# 2 ტიპის კომენტარი
# ესეთი
"""
და ესეთიც
"""


# დარეზერვებული ცვლადის სახელები
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 2 ტიპის ცვლადი: Mutable(ცვალებადი) და Immutable(უცვლელი)
# Mutable - list, dictionary, set
# Immutable - Bool, int, string, float, tuple



# 2 ლექცია
# ------------------------------------------------------------------------------------------------------

# ოპერატორები
# ოპერატორები არის სიმბოლოთა შეთანხმება,
# რომლებიც გამოიყენება ცვლადებზე და მათ მნიშვნელობებზე
# სხვადასხვა ოპერაციების შესასრულებლად.
# პითონში გვაქვს ოპერატორების რამდენიმე ჯგუფი.

# > არითმეტიკული ოპერატორები              --------

# 5 + 3 = 8   შეკრება
# 5 - 3 = 2   გამოკლება
# 5 * 3 = 15  გამრავლება
# 6 / 3 = 2.0 გაყოფა
# 6 // 3 = 1  გაყოფა მთელი
# 5 % 2 = 1   ნაშთი
# 5 ** 2 = 25 ხარისხში აყვანა



# > მინიჭების ოპერატორები                   --------

# a = 5   ==   a = 5
# a += 5  ==   a = a + 5
# a -= 5  ==   a = a - 5
# a *= 5  ==   a = a * 5
# a /= 5  ==   a = a / 5
# a //= 5 ==   a = a // 5
# a %= 5  ==   a = a % 5
# a ** 5  ==   a = a ** 5



# > ლოგიკური ოპერატორები                   --------

# and აბრუნებს True თუ ორივე სწორია
# x = 6
# x > 5 and x < 10
#
# or აბრუნებს True თუ ერთ-ერთი სწორია
# x = 5
# x < 10 or x > 10
#
# not აბრუნებს შებრუნებულს , თუ პირობა True არის დაგვიბრუნებს False
# x = 5
# not(x < 5 or x < 10)



# > წევრობის ოპერატორები                    --------

# in აბრუნებს True თუ ობიექტი ასრულებს პირობას
# y = [1,2,3]
# x = 1
# x in y
#
# not in აბრუნებს True თუ ობიექტი არ ასრულებს პირობას
# y = [1,2,3]
# x = 4
# x in y



# > იდენტურობის ოპერატორი                   --------

# is აბრუნებს True თუ ორიექტები ერთი და იგივეა
# x = 1
# y = 1
# x is y
#
# is not აბრუნებს True თუ ობიექტები სხვადასხვაა
# x = 1
# y = 2
# x is not y



# > შედარების ოპერატორები                    --------

# a > b          a მეტია b_ზე
# a < b          a ნაკლებია b_ზე
# a == b         a და b ერთმანეთის ტოლია
# a != b         a და b ერთმანეთის ტოლი არ არის
# a >= b         a მეტია ან ტოლია b_ზე
# a <= b         a ნაკლებია ან ტოლია b_ზე



# Python-ში შეგვიძლია if-elif-else კონსტრუქციები ჩავდგათ ერთმანეთში,
# რაც ნიშნავს, რომ if-ში ჩადგმული if ამოქმედდება მხოლოდ პირველი
# if პირობის შესრულების შემთხვევაში, ჩადგმულ if-ს კი ისევ ინდენტაციის
# დაცვის გზით ვუწერთ თავის ბლოკს



# 3 ლექცია
# ------------------------------------------------------------------------------------------------------

# > range() ფუნქცია აბრუნებს რიცხვების თანმიმდევრობას.
# > მხოლოდ საბოლოო მნიშვნელობა -   range(10)
# > საწყისი და საბოლოო მნიშვნელობა - range(5, 10)
# > საწყისი,  საბოლოო მნიშვნელობა და ბიჯი  -  range(5, 10, 2)
# > len() აბრუნებს ობიექტების რაოდენობას
# > random - Random მოდული წარმოქმნის შემთხვევით რიცხვებს Python-ში.

# iter_ით ამოაგდებს ჯერ  numb1_ს მერე numb2_ს და ბოლოს numb3_ს და next კიდევ შემდეგს აგდებს

# name = iter(["numb1","numb2","numb3","numb4","numb5"])
# print(next(name))
# print(next(name))
# print(next(name))



# while არის ციკლი რომელიც მუშაობს სანამ პირობა არის True

# text = int(input("ჩაწერეთ რიცხვი: "))
# while text < 10:
#     text += 1
#     print(text)
#     if text == 10:
#         break
# else:
#     print("Number is higher than 10")
#
# ვწერთ რიცხვს 10_მდე და ის გვიგდებს ყველას 10_მდე ხოლო თუ 10_ზე მეტია მაშინ else პირობას აკეთებს



# range ფუნქციაში რა ციფრიც გვიწერია იმდენჯერ ატრიალებს for ციკლს

# text = "hello itstep"
#
# for i in range(10):
#     print(i)



# text = "hello world"
# length = len(text)
# a = 0
#
# for i in range(length):
#     a += 1
#     print(a)
#
# დაპრინტავს text_ში რამდენი ასოც არის



# import random
#
# print("random: ",random.randint(1,30))
# print("random: ",random.choice([1,2,3,4,5,6,7,8,9,0]))
#
# random ფუნქცია გარტყმით იღებს ციფრს 0_დან 30_მდე და მეორეში 10_მდე



# 4 ლექცია
# ------------------------------------------------------------------------------------------------------

# String-ზე მოქმედებები
a = "hello "
b = "world"

# print(a + b)          hello world
# print(a * 2)          hello hello
# print(a[0])           h
# print(a[0:2])         he
# print("h" in a)       true
# print("j" not in a)   true



# > capitalize() - პირველი სიმბოლოს  მაღალ რეგისტრში გადასაყვანად
# > upper() - ყველა სიმბოლოს მაღალ რეგისტრში გადასაყვანად
# > lower() - ყველა სიმბოლოს დაბალ რეგისტრში გადასაყვანად
# > count() - მოცემული სიმბოლოს რაოდენობის დათვლას დასათვლელად ობიექტში
# > index() - მოცემული სიმბოლოს ინდექსის გასაგებად
# > split() - ყოფს ობიექტს შესაბამისი გამყოფით
# > strip() - აშორებს ობიექტს ზედმეტ სიმბოლოებს
# > format() - გვეხმარება სტრინგში მნიშვნელობის შესაცვლელად
# > find()  - გვეხმარება ინდექსის საპოვნელად
# > join() - იღებს ყველა ელემენტს iterable-ში და აერთიანებს მათ ერთ სტრიქონში.

# name = "david"
# print(name.capitalize())           David



# name = "david"
# text = f"my name is {name}"
# print(text)                        my name is david



# name = "my name is \t david"
# print(name)                          my name is     david

# name = "my name is \n david"
# print(name)                          my name is
#                                       david

# a = "a"
# print(ord(a))            97
# print(chr(98))           b



# 5 ლექცია
# ------------------------------------------------------------------------------------------------------

# ლისტის შექმნა და მასზე მოქმედება

# > append(): ამატებს ელემენტს სიის ბოლოს.
# > extend(): დაამატე სხვა სიას ელემენტების ბოლოს.
# > insert(): ელემენტის ჩასმა კონკრეტულ ინდექსზე.
# > remove(): წაშლის მითითებულ ელემენტს პირველივე შემთხვევისას.
# > pop(): ამოაქვს და აბრუნებს ელემენტს კონკრეტულ ინდექსზე.
# > index(): დააბრუნებს მნიშვნელობის პირველივე შემთხვევისას.
# > count(): დააბრუნებს მოცემული ობიქეტის რაოდენობას.
# > sort(): დაალაგებს სიის ელემენტებს ზრდადი თანმიმდევრობით.
# > reverse(): შეცვლის ელემენტების თანმიმდევრობას სიაში.


# lst = [x for x in range(1,10)]
# print(lst)
#                      # === the same
# lst = []
# for i in range(1,10):
#     lst.append(i)
# print(lst)



# numbers = [1,2,3,4,5,6,7,8,9]
# lst = ["even" if num % 2 == 0 else "odd" for num in numbers]
# print(lst)



# list = [5,6,7,8,9]
# list.insert(1, "str")
# print(list)                               #ამატებს 1 ინდექსის მერე str_ს



# numbers = [1,2,3,4,5,6,7,8,9]
# target = 3
#
# for number in range(len(numbers)):
#     if numbers[number] == target:
#          print(number)                       #ძებნის სისტემა

# 6 ლექცია
# ------------------------------------------------------------------------------------------------------

# ფუნქციები და მეთოდები

# numbers = [1,2,3,4,5,11,6,7,13,9,10]
# print(max(numbers))                          # max ფუნქცია იღებს list_დან ყველაზე მაღალს

# list = [1,10,12,16,21]
# print(sum(list))                             # sum ითვლის ჯამს



# import math
#
# sqr = math.sqrt(16)     # 4.0
# sqr_2 = math.pow(5,2)   # 25.0
# x = math.ceil(2.4)      # 3
# y = math.floor(2.4)     # 2
# z = math.fabs(-10)      # 10.0
# y = math.gcd(-10,20,30) # ყველაზე დიდი საერთო გამყოფი = 10
# a = math.factorial(5)   # 1 * 2 * 3 * 4 * 5 = 120
# print(sqr, sqr_2, x, y, z, y, a)    # python math module



# def func_1():
#     result = 2 + 3
#     return result
#
# def func_2(a):
#     return a
#
# print(func_2(func_1()))     # 5

# from main import func_1   #სხვა ფაილის შექმნის დროს ესე უნდა გაწერა



# def function(a, b):
#     result = a + b
#     return result
#
# print(function(5,2))       # 7



# def func_1(arg):
#     return arg
# def func_2(*args):
#     return args
# print(func_1(5))         # 5
# print(func_2(1,2,3))     # (1,2,3)


# 7 ლექცია
# ------------------------------------------------------------------------------------------------------

# ფუნქციები

# def main(name , surname):
#     return "hello " + name + " " + surname
#
# print(main(name="itstep",surname="georgia"))        # hello itstep georgia



# def main(*args):                     # hello
#     for i in args:                   # 1
#         print(i)                     # 2
#                                      # 3
# main("hello","1","2","3")



# def main(*args,main):
#     return args,main

# print(main("test","test2",main="test5"))      # (('test', 'test2'), 'test5')

# def main(**kwargs):
#     return kwargs

# print(main(name="1",age="3"))               # {'name': '1', 'age': '3'}



# def main(name,age):
#     return (name,age)
#
# lst = ['it',15]
# print(main(*lst))                     # unpacking    ('it', 15)



# def main(*args):
#     total = sum(args)
#     return total
#
# print(main(10,20,30,40,50,60))         # packiging      210



# def calc(*args):
#     total = sum(args)
#     average = total / len(args)
#     return total, average
#
# new_total, new_average = calc(1,2,3,4,5,6,7,8)
#
# print(new_total)          # 36
# print(new_average)        # 4.5



# global_var = 'test'
# def main():
#     global local_var
#     local_var = 'new_test'
#     print(global_var)
#     print(local_var)
#
# main()        #ფუნქციაში ცვლადი რომ გადავაგქიოთ გლობალურად მას უნდა გაეწეროს Global რომ ყველგან გამოვიყენოთ



# def new_main(num):
#     if num <= 1:
#         return 1
#     else:
#         print(num)
#         return num * new_main(num - 1)
#
# print(new_main(6))



# def nums(n):
#     if n > 0:
#         print(n)
#         return nums (n - 1)
# print(nums(7))



# def func(n):
#     if n <= 1:
#         return 1
#     else:
#         print(n)
#         return func(n-1)
# print(func(5))
#

#
# def print_pattern(n):
#     b = '1'
#     print(b)
#     i = 1
#     while i < n:
#         i += 1
#         b = b + str(i)
#         print(b)
# print_pattern(5)



# def print_pattern(n):
#     if n <= 1:
#         print(1)
#     else:
#         result = print_pattern(n - 1)
#         for i in range(1, n + 1):
#             print(i, end="")
#         print()
#         return result
#
# print_pattern(10)




# 8 ლექცია
# ------------------------------------------------------------------------------------------------------













# 9 ლექცია
# ------------------------------------------------------------------------------------------------------

# 10 ლექცია
# ------------------------------------------------------------------------------------------------------

# 11 ლექცია
# ------------------------------------------------------------------------------------------------------