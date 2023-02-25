import ccxt
upbit = ccxt.upbit()
upbit.load_markets()
symbols =upbit.symbols
my_symbols =["BTC/KRW","XRP/KRW","DOGE/KRW"]
# symbols=["BTC/KRW","XRP/KRW","DOGE/KRW"]


for symbol in symbols:
    if not symbol in my_symbols:
        continue#현재 symbol이 my_symbols 안에 속하지 않다면
    #밑에를 더 이상 진행하지 안고 다음 반복으로 넘어감
    infos=upbit.fetch_ticker(symbol)
    price=infos["close"]
     # print(price)
    if symbol == "DOGE/KRW" and price <200:
        break
    print(f"{symbol}의 가격은{price}원 입니다.")

    print("프로그램 끝!")
    # print(symbol)# 이 symbol은 변수이므로 아무렇게 지어도 된다.
