import numpy as np
import warnings

def print_hi():
    english_score = np.array([55, 89, 76, 65, 48, 70])
    math_score = np.array([60, 85, 60, 68, np.nan, 60])
    chinese_score = np.array([65, 90, 82, 72, 66, 77])
    # 1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
    # 平均數
    print("平均數")
    eng_mean = np.nanmean(english_score)
    print(eng_mean)
    math_mean = np.nanmean(math_score)
    print(math_mean)
    chi_mean = np.nanmean(chinese_score)
    print(chi_mean)

    # 最大值
    print("最大值")
    eng_max = np.nanmax(english_score)
    print(eng_max)
    math_max = np.nanmax(math_score)
    print(math_max)
    chi_max = np.nanmax(chinese_score)
    print(chi_max)

    # 最小值
    print("最小值")
    eng_min = np.nanmin(english_score)
    print(eng_min)
    math_min = np.nanmin(math_score)
    print(math_min)
    chi_min = np.nanmin(chinese_score)
    print(chi_min)

    # 標準差
    print("標準差")
    eng_std = np.nanstd(english_score)
    print(eng_std)
    math_std = np.nanstd(math_score)
    print(math_std)
    chi_std = np.nanstd(chinese_score)
    print(chi_std)

    # 2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
    math_score[4] = 55
    # 平均數
    print("補考後平均數")
    eng_mean = np.nanmean(english_score)
    print(eng_mean)
    math_mean = np.nanmean(math_score)
    print(math_mean)
    chi_mean = np.nanmean(chinese_score)
    print(chi_mean)

    # 最大值
    print("補考後最大值")
    eng_max = np.nanmax(english_score)
    print(eng_max)
    math_max = np.nanmax(math_score)
    print(math_max)
    chi_max = np.nanmax(chinese_score)
    print(chi_max)

    # 最小值
    print("補考後最小值")
    eng_min = np.nanmin(english_score)
    print(eng_min)
    math_min = np.nanmin(math_score)
    print(math_min)
    chi_min = np.nanmin(chinese_score)
    print(chi_min)

    # 標準差
    print("補考後標準差")
    eng_std = np.nanstd(english_score)
    print(eng_std)
    math_std = np.nanstd(math_score)
    print(math_std)
    chi_std = np.nanstd(chinese_score)
    print(chi_std)

    # 3. 用補考後資料找出與國文成績相關係數最高的學科?
    print("與國文相關係數最高的考科")
    coef_chi_eng = np.corrcoef(chinese_score,english_score)
    print("國文與英文相關係數:",coef_chi_eng)
    coef_chi_math = np.corrcoef(chinese_score, math_score)
    print("國文與數學相關係數:",coef_chi_math)

if __name__ == '__main__':
    print_hi()




