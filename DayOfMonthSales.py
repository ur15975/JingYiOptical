from JingYiStr import judgeStore

# 总业绩每月代码
def getYuePayload(dianming, year, month):
    dianmingstr = judgeStore(dianming)
    return "deptcode=" + dianmingstr + "&breedcode=&startdate=" + str(year) + "-01-01&enddate=" + str(
        year + 1) + "-01-01&datetype=1&pricetype=1&mode=" + str(month)

# 隐形眼镜每月代码
# startdate=2018-01-01&enddate=2019-01-01&mode=06&deptcode=0022&typecode=04&pricetype=1%2C5
def getContactLens(dianming, year, month):
    dianmingstr = judgeStore(dianming)
    return "startdate=" + str(year) + "-01-01&enddate=" + str(year + 1) + "-01-01&mode=" + str(
        month) + "&deptcode=" + str(dianmingstr) + "&typecode=04&pricetype=1%2C5"

# 洗眼液每月代码
# startdate=2018-01-01&enddate=2019-01-01&mode=06&deptcode=0022&pricetype=1%2C5&select=%E6%B4%97%E7%9C%BC
def getYueXiYanYe(dianming, year, month):
    dianmingstr = judgeStore(dianming)
    return "startdate=" + str(year) + "-01-01&enddate=" + str(year + 1) + "-01-01&mode=" + str(
        month) + "&deptcode=" + str(dianmingstr) + "&pricetype=1%2C5&select=%E6%B4%97%E7%9C%BC"


# 叶黄素每月代码
# startdate=2018-01-01&enddate=2019-01-01&mode=06&deptcode=0022&pricetype=1%2C5&select=%E5%8F%B6%E9%BB%84
def getYeHuangSu(dianming, year, month):
    dianmingstr = judgeStore(dianming)
    return "startdate=" + str(year) + "-01-01&enddate=" + str(year + 1) + "-01-01&mode=" + str(
        month) + "&deptcode=" + str(dianmingstr) + "&pricetype=1%2C5&select=%E5%8F%B6%E9%BB%84"

# 润眼液每月代码
# startdate=2018-01-01&enddate=2019-01-01&mode=06&deptcode=0022&pricetype=1%2C5&select=%E6%B6%A6%E7%9C%BC
def getYeHuangSu(dianming, year, month):
    dianmingstr = judgeStore(dianming)
    return "startdate=" + str(year) + "-01-01&enddate=" + str(year + 1) + "-01-01&mode=" + str(
        month) + "&deptcode=" + str(dianmingstr) + "&pricetype=1%2C5&select=%E6%B6%A6%E7%9C%BC"


