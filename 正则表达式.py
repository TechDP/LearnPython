#!/usr/bin/python
 
import re
# 从第一个字节开始进行匹配，如果失败返回 None
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('www', 'www.haha.com').group())
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")



# 查找整个字符串的数据
print(re.search('bw', 'aw,bw,cw,dw'))
print(re.search('bw', 'aw,bw,cw,dw').group())
print(re.search('bw', 'aw,bw,cw,dw').start())
print(re.search('bw', 'aw,bw,cw,dw').end())

# 分割字符串
# re.split(pattern, string, maxsplit=0, flags=0)
# 按照能够匹配的字符串以列表的形式分隔返回不能匹配到的字串，maxsplit用于指定最大分割次数，不指定将全部分割。
print(re.split('[0-9]', 'a1b2c3df45sdf'))
print(re.split('[0-9]', 'a1b2c3df45sdf', 2))

# 搜索string，以列表的形式返回全部能匹配到的字串。
print(re.findall('[0-9]', 'a1b2c3df45sdf'))
print(re.findall('\d+', 'a1b2c3df45sdf')) #以列表的形式返回所有匹配的子串，\d+为匹配1到多个数字

# 搜索string，返回访问每一个匹配结果的match对象的迭代器
print(re.finditer('[0-9]', 'a1b2c3df45sdf'))
for i in re.finditer('[0-9]', 'a1b2c3df45sdf'):
    print(i.group())

# re.sub(pattern, repl, string, count=0, flags=0)
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。count用于指定最多替换的次数，不知道时全部替换。
pat = re.sub('\d+', '@@@', 'aaa1bbb22ccc33333')
print(pat)
pat = re.sub('\d+', '@@@', 'aaa1bbb22ccc33333', count = 2)
print(pat)

# re.subn(pattern, repl, string, count=0, flags=0)
# 返回一个元组包含（新的替换字串，数量）
pat = re.subn('\d+', '@@@', 'aaa1bbb22ccc33333')
print(pat)
pat = re.subn('\d+', '@@@', 'aaa1bbb22ccc33333', count = 2)
print(pat)
