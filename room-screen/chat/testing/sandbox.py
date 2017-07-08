<<<<<<< HEAD
from multiprocessing import Process
from time import sleep


def one():
    while True:
        print("this is thread one")
        sleep(2)

def two():
    while True:
        print("this is thread two")
        sleep(5)



if __name__ == '__main__':
  p1 = Process(target=one)
  p1.start()
  p2 = Process(target=two)
  p2.start()
  p1.join()
  p2.join()
=======
from multiprocessing import Process
from time import sleep


def one():
    while True:
        print("this is thread one")
        sleep(2)

def two():
    while True:
        print("this is thread two")
        sleep(5)



if __name__ == '__main__':
  p1 = Process(target=one)
  p1.start()
  p2 = Process(target=two)
  p2.start()
  p1.join()
  p2.join()
>>>>>>> ba00ef1077f809dd7ebea03a214d112bf8826bb6
