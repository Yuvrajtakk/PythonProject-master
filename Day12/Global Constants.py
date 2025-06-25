def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
# print(a_variable)  // throw name error

i = 50


def foo():
    i = 100
    return i


foo()
print(i)# 50


def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16#black scope

    print(my_variable)


bar()