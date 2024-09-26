from PublicDataReader import TransactionPrice
import pandas
import json

class PublicData:
    def __init__(self) -> None:
        with open("./config.json", "r") as config_file:
            config = json.load(config_file).get("PUBLIC_DATA")
            self.serviceKey = config.get("SERVICE_KEY")
            self.legalDistrictFile = config.get("LEGAL_DISTRICT_FILE") 
            self.legalDistrictSchema = config.get("LEGAL_DISTRICT_SCHEMA") 
            self.legalDistrictGuFile = config.get("LEGAL_DISTRICT_GU_FILE") 
            
            self.apiTP = TransactionPrice(self.serviceKey)

            self.initLegalDistictData()

    def initLegalDistictData(self) -> None:
        data = pandas.read_csv(self.legalDistrictFile, sep='\t', engine="python", encoding="utf-8", dtype=self.legalDistrictSchema)
        
        # 법정동코드 = 시코드(2자리) + 구코드(3자리)
        # 구코드가 000인 경우 = 시코드로 볼 수 있음
        # 시코드 제거 
        print(data)
        data = data.where(data["Exist"] == "존재")                                        \
                   .where(data["LegalDistictCode"].str.slice(start=2, stop=5) != '000')  \

        # 남겨야할 구코드를 생성 = 동코드를 제거하기 위함
        data["LegalDistictCode_slice"] = data["LegalDistictCode"].str.slice(start=0, stop=5) + "00000"

        data = data.where(data["LegalDistictCode"] == data["LegalDistictCode_slice"])   \
                .rename(columns={"LegalDistictCode"       : "LegalDistictCode_delete"}) \
                .rename(columns={"LegalDistictCode_slice" : "LegalDistictCode"       }) \
                .drop(columns=["LegalDistictCode_delete"])                              \
                .dropna()                                                               \
                .reset_index(drop=True)

        data.to_csv(self.legalDistrictGuFile, index=False)

    def printLegalDistrictGu(self):
        #return pandas.read_csv(self.legalDistrictGuFile, sep='\t', engine="python", encoding="utf-8", dtype=self.legalDistrictSchema)
        data = pandas.read_csv(self.legalDistrictGuFile, sep='\t', engine="python", encoding="utf-8", dtype=self.legalDistrictSchema)
        print(data)
        print(data.values.tolist())

        



pd = PublicData()
pd.printLegalDistrictGu()

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


# 단일 월 조회
# 시 기준 코드를 넣어봐야 아무것도 안나옴
# 구 기준 코드(5자리)를 넣어야 데이터가 나옴
#df = api.get_data(
#    property_type="아파트",
#    trade_type="매매",
#    sigungu_code="11110",
#    year_month="202212",
#)

#print(df.head)
