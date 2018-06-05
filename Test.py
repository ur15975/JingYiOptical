import requests,json
from HttpRequest import getResponse,turnResponseToJsonlist
from DayOfMonthSales import getYuePayload


zongdianYueRespone = getResponse(getYuePayload("dalian", 2018, 5))
print(turnResponseToJsonlist(zongdianYueRespone.text))

