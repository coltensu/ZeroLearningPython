"""
palindrome	英[ˈpælɪndrəʊm]  美[ˈpælɪndroʊm]
             n.	回文(正反读都一样的词语);
"""


def invert(num):
    total = 0
    while num > 0:
        total = total * 10 + num % 10
        num //= 10
    return total


def is_palindrome(num):
    invert_num = invert(num)
    if invert_num == num:
        print(num, 'is a palindrome number.')
    else:
        print(num, 'is not a palindrome number.')


if __name__ == '__main__':
    is_palindrome(123456)
    is_palindrome(12321)
    is_palindrome(11111111111200000)
    #while True:
    #    n = input('Please input a number:')
    #    is_palindrome(int(n))
