import numpy as np
import warnings

def print_hi():
    # 1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
    V1 = 20000
    V0 = 20
    a = V1/V0
    b = 20 * np.log10(a)
    print(b)

    # 2.30分貝的聲壓會是50分貝的幾倍?
    #公式移項過後可以得到 V1 = ?
    G_30 = 10 ** (30/20) * V0
    G_50 = 10 ** (50/20) * V0
    c = G_30/G_50
    print(c)

if __name__ == '__main__':
    print_hi()




