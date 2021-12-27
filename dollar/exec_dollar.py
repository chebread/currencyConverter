# 간단 환율계산 (달러)
from datetime import *

clock = datetime.now()
ymd = "%s 년 %s 월 %s 일"%(clock.year, clock.month, clock.day)
_usd_ = 1126.97
def Conversion(v, c):
    return v * c # 환율

print("-- 간단 환율 계산 (달러) --")
print("-> 환율: %s 기준 -<"%ymd)
while True:
    value = float(input("달러(0:quit): "))
    if value == 0.0:
        print("=> 종료 <=")
        break
    _won_ = Conversion(value, _usd_)
    print(f"-- Dollar {value} = won {_won_} --")
