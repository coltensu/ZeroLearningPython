from multiprocessing import Process
from time import sleep


def read_task():
    while True:
        print('reading...')
        sleep(1)


def write_task():
    while True:
        print('writing...')
        sleep(3)


if __name__ == '__main__':
    read_thread = Process(target=read_task)
    read_thread.start()
    write_thread = Process(target=write_task)
    write_thread.start()
    read_thread.join()
    write_thread.join()
