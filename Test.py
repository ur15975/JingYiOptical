import requests,json
from HttpRequest import getResponse,turnResponseToJsonlist
from DayOfMonthSales import getYuePayload,getYueXiYanYe,getYeHuangSu,getContactLens

# dalianYueRespone = getResponse(getYuePayload("dalian", 2018, 6))
# print(turnResponseToJsonlist(dalianYueRespone.text))

zongdianYueRespone = getResponse(getYuePayload("zongdian", 2018, 6))
print(turnResponseToJsonlist(zongdianYueRespone.text))

zongdianXiYanYeRespone = getResponse(getYueXiYanYe("zongdian", 2018, 6))
print(turnResponseToJsonlist(zongdianXiYanYeRespone.text))

zongdianYeHuangSuRespone = getResponse(getYeHuangSu("zongdian", 2018, 6))
print(turnResponseToJsonlist(zongdianYeHuangSuRespone.text))

zongdianContactLensRespone = getResponse(getContactLens("zongdian", 2018, 6))
print(turnResponseToJsonlist(zongdianContactLensRespone.text))

qijianDianRespone = getResponse(getYuePayload("qijian", 2018, 6))
print(turnResponseToJsonlist(qijianDianRespone.text))

huataiDianRespone = getResponse(getYuePayload("huatai", 2018, 6))
print(turnResponseToJsonlist(huataiDianRespone.text))

xinmateDianRespone = getResponse(getYuePayload("dashang", 2018, 6))
print(turnResponseToJsonlist(xinmateDianRespone.text))


