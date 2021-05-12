# 환율 계산 프로그램

# 21/5/12 기준 세계 환율
usd = 1129.01 # 1 Dollar
eur = 1361.21 # 1 Eur
gbp = 1592.47 # 1 Found
cny = 175.03 # 1 Wian

# 21/5/12 평균 기준 가상화패 환율
bc = 64244338 # 1 BitCoin

def CoinCurrency(coin, _type_, coin_name):
    if coin == "q":
        print("== (종료) ==")
        exit()
    if coin == "w":
        type_coin = float(input("코인: "))
        won = type_coin * _type_
        print("-- %f 원 = %f %s --\n"%(won, type_coin, coin_name))
    elif coin == "c":
        won = float(input("원화: "))
        type_coin = won / _type_
        print("-- %f %s == %f 원 --\n"%(type_coin, coin_name, won))
    else:
        print("== (Error) ==")

# 원-환율 계산법:
# 미국) (코인) * (환율) = 원화, 원화 / 환율 = 달러
# 유럽) (코인) * 환율 = 원화, 원화 / 환율 = 유로
# 중국) = 위안
# 영국) 파운드
while True:
    print("-- 환율 계산 프로그램 --")
    # 환율의 종류 선택
    print("-- 가상화패: v / 나라: c (q:quit) --")
    type_coin = str(input())
    if type_coin == "q":
        print("== (종료) ==")
        exit()
    # Virtual currency
    if type_coin == "v":
        print("-- 가상화패 환율 계산 --")
        type_virtual = int(input(("1. 비트코인\n(0:quit)\n")))
        if type_virtual == 0:
            print("== (종료) ==")
            exit()
        if type_virtual == 1:
            print("-- 비트코인 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            bitcoin_currency = str(input())
            CoinCurrency(bitcoin_currency, bc, "BC")
        elif type_virtual == 1:
            print("-- 비트코인 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            bitcoin_currency = str(input())
            CoinCurrency(bitcoin_currency, bc, "BC")
        elif type_virtual == 1:
            print("-- 비트코인 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            bitcoin_currency = str(input())
            CoinCurrency(bitcoin_currency, bc, "BC")
        else:
            print("== (Error) ==")
    # 나라
    elif type_coin == "c":
        print("-- 환율 계산 --")
        type_currency = int(input("1. 달러\n2. 유로\n3. 파운드\n4. 위안\n(0: quit)\n"))
        # 달라
        if type_currency == 0:
            print("== (종료) ==")
            exit()
        if type_currency == 1:
            print("-- 달러 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            dollar_currency = str(input())
            CoinCurrency(dollar_currency, usd, "USD")
        elif type_currency == 2:
            print("-- 유로 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            eur_currency = str(input())
            CoinCurrency(eur_currency, eur, "EUR")
        elif type_currency == 3:
            print("-- 파운드 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            found_currency = str(input())
            CoinCurrency(found_currency, gbp, "GBP")
        elif type_currency == 4:
            print("-- 위안 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            wian_currency = str(input())
            CoinCurrency(wian_currency, cny, "CNY")
        else:
            print("== (Error) ==")
