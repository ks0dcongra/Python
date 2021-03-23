import numpy as np
import warnings

def print_hi():
    english_score = np.array([55, 89, 76, 65, 48, 70])
    math_score = np.array([60, 85, 60, 68, 55, 60])
    chinese_score = np.array([65, 90, 82, 72, 66, 77])
    #上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，運用上列數據回答下列問題。

    #1.有多少學生英文成績比數學成績高？
    en_greater_ma = np.greater(english_score,math_score)
    print(en_greater_ma)
    en_greater_ma_sum = np.sum(en_greater_ma)
    print(en_greater_ma_sum)
    #2.是否全班同學最高分都是國文？
    e = np.not_equal(chinese_score, [english_score, math_score])
    f = np.all(e)
    print(f)





if __name__ == '__main__':
    print_hi()




