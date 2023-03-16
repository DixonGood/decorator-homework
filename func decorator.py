from datetime import datetime

def func(time):
    def wrapper(*args):
        star_time_func = datetime.now()
        result = time(*args)
        end_func = datetime.now()
        print(f'Время работы функции: {end_func - star_time_func}')
        return result
    return wrapper


print("---" * 80)

@func
def func1(work):
    if work % 2 == 0:
        return work

list1 = [1, 5, 10, 12, 6, 33, 40, 51]

new_list = [i for i in list1 if func1(i)]

print(new_list)


print("---" * 80)

@func
def func3(name):
    return "".join(reversed(name.upper()))

work_1 = input("Введите строку: ")
result = func3(work_1)
print(result)

print("---" * 80)