import numpy as np


def print_hi():
    # 1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
    a = np.array(range(30))
    b = a.reshape(5,6)
    c = b.ravel(order='F')
    d = c.reshape(5,6)
    print(d)

    # 2.呈上題的array，找出被6除餘1的數的索引
    e = np.where(d%6==1)
    print(e)






if __name__ == '__main__':
    print_hi()




