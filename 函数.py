# 函数内部定义函数

GLOBAL_VALUE = 5
def func1():
    # global必须声明在所有调用该参数的前面
    global GLOBAL_VALUE
    print("GLOBAL_VALUE is {}".format(GLOBAL_VALUE))
    GLOBAL_VALUE += 1
    print("GLOBAL_VALUE is {}".format(GLOBAL_VALUE))
    value = 5
    def func1_Inter():
        print("Func Inter")
        print("GLOBAL_VALUE is {}".format(GLOBAL_VALUE))
        nonlocal value
        print("value is {}".format(value))
    func1_Inter()

func1()


# 闭包
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2)
cube = nth_power(3)

print(square(2))
print(cube(2))



# 匿名函数
'''
lambda argument1, argument2,... argumentN : expression
匿名函数的关键字是lambda，之后是一系列的参数，然后用冒号隔开，最后则是由这些参数组成的表达式
'''

