# დავალება 1
# -----------------------------------------------------------------------------------------------------


# def find_missing_numbers(lst):
#     min_num = min(lst)
#     max_num = max(lst)
#     missing_numbers = []
#     for i in range(min_num, max_num + 1):
#         if i not in lst:
#             missing_numbers.append(i)
#     return missing_numbers
#
#
# nums = [1, 2, 4, 6, 8, 9, 10, 12, 14, 20]
# missing_numbers = find_missing_numbers(nums)
# print("გამოტოვებული ციფრები არის: ", missing_numbers)
#





# დავალება 2
# -----------------------------------------------------------------------------------------------------


# def binary_search(arr,target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
#
# nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
# target = 9
# result = binary_search(nums, target)
# print("პირველი გამმეორებადი რიცხვი ", target, "_ის", "არის ინდექსად: ", result)

