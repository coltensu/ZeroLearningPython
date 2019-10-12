"""
Q: patton中的字符串为什么要前置r？
A: re会自动解析字符串中的内容并转义，所以无需自己转义。
"""

import re

while True:
    username = input('Pls input your name:')
    result = re.match(r'\w*su\w*', username)
    print(result)
    if result:
        print('su')
    else:
        print('not su')