# დავალება 1
# ----------------------------------------------------------------------------------------------

# import random
#
#
# def sorting_random_number():
#
#
#     random_number = [random.randint(0, 500) for _ in range(100)]
#     ascending_list = sorted(random_number)
#     descending_list = sorted(random_number, reverse=True)
#     return ascending_list, descending_list
#
#
# ascending_result, descending_result = sorting_random_number()
# print("ascend:  ", ascending_result)
# print("descend: ", descending_result)





# დავალება 2
# ----------------------------------------------------------------------------------------------

# import random
#
#
# def quick_sort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left = [x for x in arr[1:] if x < pivot]
#         middle = [x for x in arr[1:] if x == pivot]
#         right = [x for x in arr[1:] if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
#
# def sorting_random_number():
#
#     random_list = [random.randint(0, 500) for _ in range(100)]
#     ascending_list = quick_sort(random_list)
#     descending_list = selection_sort(random_list)[::-1]
#     return ascending_list, descending_list
#
#
# ascending_result, descending_result = sorting_random_number()
# print("ascend:  ", ascending_result)
# print("descend: ", descending_result)

