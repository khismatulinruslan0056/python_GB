
# #### 5.2[28]: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3
#     <function_name>(10,34) -> 44

def sum_recurs(numbA, numbB):
    if numbB == 0: return numbA
    return sum_recurs(numbA + 1, numbB - 1)

print(sum_recurs(0,0))
print(sum_recurs(0,2))
print(sum_recurs(3,0))
print(sum_recurs(10,34))