def testing():
    print("testing...")

# def decorator(func):
#     if type(func).__name__ == "function":  # функция выполнилась, но не напрямую, а через др функцию
#         func()
#
# decorator(testing)

# def decorator():
#     def wrapper():
#         print("testing wrapper function...")
#
#     return wrapper
#
# t = decorator()
# t()


def decorator(func):
    def wrapper():
        print("Before starting...")
        func()
        print("After starting..")

    return wrapper

@decorator
@decorator
@decorator
def testing():
    print("testing...")


# testing = decorator(testing)  #можно заменить на аннотацию @
# testing = decorator(testing)
# testing = decorator(testing)

testing()