__all__= ["A", "test_a"]   #список или тьюпл # инкапсуляция на уровне модуля

__a = 10
__b = 20

def test_a():
    print("test_a from module some")

def test_b():
    print("test_b")


class A:
    pass

class B:
    pass