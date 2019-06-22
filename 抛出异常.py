# try:
#     s = input('please enter two numbers separated by comma: ')
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
# except (ValueError, IndexError) as err:
#     print('Value Error: {}'.format(err))


# print('continue')

## 自定义异常处理
class MyInputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise MyInputError(1)
except (MyInputError, Exception) as err:
    print('error: {}'.format(err))


