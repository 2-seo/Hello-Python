def palindrome(data):
    if len(data) <= 1:
        return True
    if data[0] == data[-1]:
        return palindrome(data[1:-1])
    return False

print(palindrome('가나가'))

