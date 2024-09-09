from PublicDataReader import TransactionPrice

SERVICE_KEY = "XTY%2FDi5zO80vkWgVSpIhICfgcVA53HVxOxuMleCVw1VVY8m400i6mBJNzNRA%2Bl607SlLhxMmuORruHXJQbUdRQ%3D%3D"
api = TransactionPrice(SERVICE_KEY)

# 단일 월 조회
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

print(df)