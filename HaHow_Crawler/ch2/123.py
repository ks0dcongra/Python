from datetime import date

def main():
    daysOfMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    def myCalendar(year, month):
        start = date(year,month,1).timetuple().tm_wday
        print(start)
        print('{0}年{1}月日歷'.format(year,month).center(57))
        print('\t'.join('日 一 二'.split()))
        day = daysOfMonth[month-1]
        result = [''*8 for i in range(start+1)]
        result += list(map(lambda d: str(d).ljust(8),range(1,day+1)))
        print(result)
        # for i, day in enumerate(result):
        #     if i!=0 and i%7 ==0:
        #         print()
        #     print(day,end='')
        # print()
    myCalendar(1000,10)
if __name__ == '__main__':
    main()
