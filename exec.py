# 환율 계산 프로그램

# 21/5/13 기준 세계 환율
usd = 1126.56 # 1 Dollar
eur = 1126.56 # 1 Eur
gbp = 1588.45 # 1 Found
cny = 175.01 # 1 Wian
iry = 15.37 # 1 rupy

# 21/5/12 평균 기준 가상화패 환율
bc = 55345414.36 # 1 BitCoin

def CoinCurrency(coin, _type_, coin_name):
    if coin == "q":
        print("== (종료) ==")
        exit()
    if coin == "w":
        type_coin = float(input("코인: "))
        won = type_coin * _type_
        won = format(won,  ',')
        type_coin = format(type_coin,  ',')
        print("-- %s 원 = %s %s --\n"%(won, type_coin, coin_name))
    elif coin == "c":
        won = float(input("원화: "))
        type_coin = won / _type_
        type_coin = format(type_coin,  ',')
        won = format(won,  ',')
        print("-- %s %s == %s 원 --\n"%(type_coin, coin_name, won))
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
    print("-- 가상화패: v / 나라: c --\n-- (f:setting) (q:quit) --")
    type_coin = str(input())
    # 기능
    if type_coin == "q":
        print("== (종료) ==")
        exit()
    if type_coin == "f":
        print("== (설정) ==")
        type_f = str(input("== (c:currency change) ==\n(q:quit)\n"))
            #설정
        if type_f == "c":
            print("== (환율 값 설정) ==")
            print("== (u:usd) ==\n== (e:eur) ==\n== (g:gdp) ==\n== (c:cny) ==\n==(i:iry) ==\n== (b:bc) ==\n(q:quit)")
            c_short = str(input())
            # 환율 값 설정
            if c_short == "q":
                print("== (종료) ==")
                exit()
            if c_short == "u":
                usd = float(input("== (%s) ==\n"%("USD")))
            elif c_short == "e":
                eur = float(input("== (%s) ==\n"%("EUR")))
            elif c_short == "g":
                gbp = float(input("== (%s) ==\n"%("GBP")))
            elif c_short == "c":
                cny = float(input("== (%s) ==\n"%("CNY")))
            elif c_short == "i":
                iry = float(input("== (%s) ==\n"%("IRY")))
            elif c_short == "b":
                bc = float(input("== (%s) ==\n"%("BC")))
            else:
                print("== (Error) ==")
        if type_f == "q":
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
        else:
            print("== (Error) ==")
    # 나라
    elif type_coin == "c":
        print("-- 환율 계산 --")
        type_currency = int(input("1. 달러\n2. 유로\n3. 파운드\n4. 위안\n5. 루피\n(0: quit)\n"))
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
        elif type_currency == 5:
            print("-- 루피 환율 계산 --")
            print("-- 원화: w / 환율: c (q:quit) --")
            found_currency = str(input())
            CoinCurrency(found_currency, iry, "IRY")
        else:
            print("== (Error) ==")
