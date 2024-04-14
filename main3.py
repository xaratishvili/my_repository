# დავალება 1 და 2
# --------------------------------------------------------------------------------------
# ვერ მივხვდი რატომ უნდა break თავიდან და არა ბოლოში, ვეცადე პირობა და მერე number == text  break ყოფილიყო მაგრამ არ იმუშავა


# total_sum = 0
# text = "sum"
#
# while True:
#     number = input("Write a positive number (write sum or 0 if you want to stop): ")
#     if number == text:
#         break
#     elif int(number) > 0:
#         total_sum += int(number)
#     elif int(number) == 0 or number == text:
#         print("final positive result is: ", total_sum)
#
# print("final positive result is: ", total_sum)


# total_sum = 0
# text = "sum"
#
# while True:
#     number = input("Write a positive number (write sum or 0 if you want to stop): ")
#     if number == text or int(number) == 0:
#         break
#     elif int(number) > 0:
#         total_sum += int(number)
# print("final positive result is: ", total_sum)
#


# პირველ if-ში დავუწეროთ ჯერ number == text და შემდეგ  int(number) == 0
# რაც შესაძლებლობას მოგვცემს რომ შევამოწმოთ სტრინგი ისე რომ ინტეჯერად არ გადავაქციოთ
# ანუ sum რო შემოვა ჯერ მაგას შეამოწმებს და მერე თუ არ იქნება  sum მაგის მერე გადავიდეს 0 იანის შემოწმებაზე
# if number == text or int(number) == 0:
#         break
#     elif int(number) > 0:
#         total_sum += int(number)
#
#
# (თუ გვინდა რომ sum-ის ნაცვლად მომხმარებელმა რაიმე სხვა ჩაწერა და მაგაზე
# ერორი არ ამოაგდოს მაგ შემთხვევაში კიდევ ერთი if დაგვჭირდება.)







# დავალება 3
# -----------------------------------------------------------------------------------------


# import random

# random_number = random.randint(1, 10)
# number_guess = None
# failure = 0

# while number_guess != random_number:
#     number_guess = int(input("Write a number between 1 to 10: "))
#     failure += 1
    
#     if failure == 5:
#         print("try again")
#         break
#     if number_guess < random_number:
#         print("Random number is higher, try typing higher number")
#     elif number_guess > random_number:
#         print("Random number is lower, try typing lower number")
#     else:
#         print("You got the number right, it is: ", random_number)





# text = "this is is itstep"
# text_2 = text.count("is")
# print(text_2)


# text = input("ჩაწერეთ ტექსტი: ")
# text2 = text
# print(text,text2)



# text = input("Enter a text to check if it's a palindrome: ")

# if text == text[::-1]:
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")

# text = input("Enter a text to check if it's a palindrome: ")
#
# if text == text[::-1]:
#     print(text,"Is True Palindrome")
# else:
#     print(text,"Is False Palindrome")
