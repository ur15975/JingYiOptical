def getYuePayload(dianming, year, month):
    dianmingstr = ""
    if   dianming == 'qijian'    : dianmingstr = "0021"
    elif dianming == 'zongdian'  : dianmingstr = "0022"
    elif dianming == 'dashang'   : dianmingstr = "0023"
    elif dianming == 'huatai'    : dianmingstr = "0024"
    elif dianming == 'dalian'    : dianmingstr = "0031"
    return "deptcode=" + dianmingstr + "&breedcode=&startdate=" + str(year) + "-01-01&enddate=" + str(year + 1) + "-01-01&datetype=1&pricetype=1&mode=" + str(month)
