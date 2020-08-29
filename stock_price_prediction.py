import json # import json module

# with statement
with open('Kospi-200.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

index = json_data["Stock"].index("SK케미칼")
stock_num = json_data["Code"][index]
stock_num = str(stock_num)

with open('naver_institute_foreign/{}.json'.format(stock_num), 'r', encoding='utf-8-sig') as json_file:
    foreign_data = json.load(json_file)
with open('naver_stockprice/{}.json'.format(stock_num), 'r', encoding='utf-8-sig') as json_file:
    stock_data = json.load(json_file)

# 외국인/기관: 기관 / 외국인 / 외국인 보유주 수 / 외국인 보유 비율
# 주      식: 시가 / 종가 / 매매량
date = "2020.08.28"
foreign_info = foreign_data[date]
stock_info = stock_data[date]
print(foreign_info, stock_info)

stock_condition = 1
foreign_condition = 1
insitute_conditoin = 1

# 주식 등락 계산
stock_price = int(stock_info[1]) - int(stock_info[0])
if stock_price < 0:
    stock_condition = 0

# 외국인 및 기관 정보
if list(foreign_info[0])[0] == '-':
    foreign_condition = 0
if list(foreign_info[1])[0] == '-':
    institute_condition = 0

result = stock_price + foreign_condition + insitute_conditoin
if result < 2:
    print("주가에 부정적인 영향을 미쳤습니다.")
else:
    print("주가에 긍정적인 영향을 미쳤습니다.")



