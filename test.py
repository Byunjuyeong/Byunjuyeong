import pyupbit

access = "CCSlQsEwwstKC43UFZyy1kmepweKJdfokREZzz8u"          # 본인 값으로 변경
secret = "jG5BbqbgNsaBqf8GjRhm0MKtS7xXY18plVV54BMt"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회