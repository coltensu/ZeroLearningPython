"""
r+可读可写，不会创建不存在的文件。
如果直接写文件，则从顶部开始写，覆盖之前此位置的内容；
如果先读后写，则会在文件最后追加内容。
"""


def main():
    with open('test.txt', 'r+', encoding='utf-8') as f:
        print(f.read())
        f.write('read: 2019/10/10\n')


def read_file():
    with open('test.txt', 'r', encoding='utf-8') as f:
        one_line = f.readlines()
        print(':', one_line)


if __name__ == '__main__':
    main()
    read_file()
