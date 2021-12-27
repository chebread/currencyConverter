# 1달러 환율
import requests

_usd_ = 1126.97
def Conversion(v, c):
    return v * c # 환율
print("-- $ 1 환율 --")
value = Conversion(1, _usd_)
print("%s 기준 %f 원"%("21/5/20", value))
print("=> POWER BY GOOGLE <=")
