from PublicDataReader import TransactionPrice
import pandas

# SERVICE_KEY = "XTY%2FDi5zO80vkWgVSpIhICfgcVA53HVxOxuMleCVw1VVY8m400i6mBJNzNRA%2Bl607SlLhxMmuORruHXJQbUdRQ%3D%3D"
# api = TransactionPrice(SERVICE_KEY)

# # 단일 월 조회
# df = api.get_data(
#     property_type="아파트",
#     trade_type="매매",
#     sigungu_code="11650",
#     year_month="202212",
# )

# # 기간 내 조회
# df = api.get_data(
#     property_type="아파트",
#     trade_type="매매",
#     sigungu_code="11650",
#     start_year_month="202201",
#     end_year_month="202212",
# )

# print(df)

legal_district_code_dtype = {"법정동코드":"str"
                             , "법정동명":"str"
                             , "폐지여부":"str"}
data = pandas.read_csv("LegalDistrictCode.txt", sep='\t', engine="python", encoding="utf-8", dtype=legal_district_code_dtype)

ldc = data["법정동코드"].str.slice(start=0, stop=5) \
                     .unique() + "00000"
result = data.where(data["법정동코드"].isin(ldc)) \
                                   .dropna() \
                                   .reset_index(drop=True)

result[["LargeDistrict", "MidleDistrict"]] = result["법정동명"].str.split(expand=True)

print(result)