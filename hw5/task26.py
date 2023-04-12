# #### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя

#     Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16


def power_recurs(numbA, numbB):
    if numbB == 0: return 1
    return power_recurs(numbA, numbB - 1) * numbA

print(power_recurs(2,0))
print(power_recurs(2,1))
print(power_recurs(2,3))
print(power_recurs(2,4))
