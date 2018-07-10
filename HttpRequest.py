import requests,json

url = "http://erp.ztjoin.com/bb/dbfx"
querystring = {"action":"search"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    'Cookie': "ASP.NET_SessionId=0g251pxor3p1peqiolv5zbwj; comck=id=dljy&emp=admin&dept=0001&g=0",
    'Content-Type': "application/x-www-form-urlencoded",
    'Host': "erp.ztjoin.com",
    'Origin': "http://erp.ztjoin.com",
    'Referer': "http://erp.ztjoin.com/bb/dbfx",
    'X-Requested-With': "XMLHttpRequest",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    'Postman-Token': "08df90e3-6f6c-412a-b4bd-02145eef6929"
}

def turnResponseToJsonlist(responseText):
    encode_json = json.loads(responseText)
    return encode_json

def getResponse(playload):
    return requests.request("POST", url, data=playload, headers=headers, params=querystring)
