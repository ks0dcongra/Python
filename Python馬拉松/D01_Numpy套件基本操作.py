import numpy as np
from random import randint

def print_hi():
    # 1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
    a = np.arange(0,21,1)
    print(a)
    # 2.呈上題，將以上數列取出偶數。
    b = np.arange(0,21,2)
    print(b)
    # 3.呈1題，將數列取出3的倍數。
    c = np.linspace(0,21,num=8,endpoint=True,retstep=False)
    print(c)

    #===========自己補充======================
    # import取亂數
    d = randint(1, 10)
    print(d)
    # np取亂數
    e = np.random.choice(100, 10)
    print(e)

if __name__ == '__main__':
    print_hi()




