# Strings: ordered, immutable, text representation

str1 = 'Hello World'
substring1 = str1[0:5]
print(substring1)

str2 = '    hi hello     '
strStrip = str2.strip()
print(strStrip)

str3 = 'hello world'
print(str3.capitalize())
print(str3.replace('hello', 'hi'))

# bad join
list1 = ['a'] * 6
strA1 = ''
for i in list1:
    strA1 += i
print(strA1)

# good join
strA2 = ''.join(list1)
print(strA2)

# %
var = 3.141952
var2 = 7
print('the variable is %d' % var)
print('the variable is %f' % var)
print('the variable is %.2f' % var)

# format
print('the variable is {} and {}'.format(var, var2))

# f-strings
print(f'the variable is {var} and {var2 * 2}')
