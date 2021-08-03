import os
import json
import xlwt
from urllib.parse import urlparse, parse_qs
import requests
import sys
import urllib
import time
import datetime

configs = [{"config_type":"301","config_name":"角色活动祈愿"},{"config_type":"302","config_name":"武器活动祈愿"},{"config_type":"200","config_name":"常驻祈愿"}]


def avgRank(rankArray,configName,currentCount) :
    length = len(rankArray)
    escape = "\n"
    total_count = 0   
    log = "============================================"+escape
    # if length == 0:
    #     return configName+"没有数据"
    for rankJSON in rankArray :
        count = rankJSON["count"]
        name = rankJSON["name"]        
        total_count += count
        log += "    "+name+" "+str(count)+" 抽"+escape
    if length != 0:
        log += "    "+configName+"平均5星:"+" "+str(total_count/length)+" 抽"+escape
    log += "    "+configName+"已累计:"+" "+str(currentCount)+" 抽未出5星"+escape
    log += "============================================"+escape
    return log
    


def main() :
    if len(sys.argv) != 2:
        print("请放入抓包后的接口后执行，如 python3 gacha.py 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?xxxxx'")
        return
    URL = sys.argv[1]
    parsed_url = urlparse(URL)
    params = parse_qs(parsed_url.query)
    authkey = params['authkey'][0]
    
         
    print_str = ""
    reuqest_param = {'size':20,
    'authkey':authkey,
    'authkey_ver':1,
    'sign_type':2,
    'auth_appid':"webview_gacha",
    'init_type':301,
    'timestamp':int(time.time()),
    'lang':"zh-cn",
    'device_type':"mobile",
    'game_biz':"hk4e_cn"
    }
    for key in params:
        reuqest_param[key] = params[key][0]
    for config in configs : 
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet(config["config_name"])
        titles = ["抽卡时间","名称","类别","星级"]
        for col,column in enumerate(titles):
            sheet.write(0, col, column)

        gacha_type = config['config_type']
        endId = 0
        row = 0
        rankCount = 0
        rankArray = []
        allData = []
        
        for page in range(1, 9999):        
            config_name = config['config_name']
            url = "https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?"                                    
            reuqest_param["gacha_type"] = gacha_type
            reuqest_param["page"] = page
            reuqest_param["end_id"] = endId        
                      
            url += urllib.parse.urlencode(reuqest_param)
            print("正在查询"+config_name+":"+str(page))
            request = requests.get(url)
            formatJSON = request.json()        
            if formatJSON["retcode"] != 0:
                print("发生错误："+formatJSON["message"])
                return
            if len(formatJSON["data"]["list"]) == 0:
                break
            for  data in formatJSON["data"]["list"]:
                allData.append(data)        
                endId=data["id"]        
                sheet.write(row+1, 0, data["time"])
                sheet.write(row+1, 1, data["name"])
                sheet.write(row+1, 2, data["item_type"])
                sheet.write(row+1, 3, data["rank_type"])
                row += 1
        workbook.save("./genshin_"+config_name+".xls")
        allData.reverse()
        currentCount = 0
        for  data in allData:
            rankCount += 1
            currentCount += 1
            rank_type = data["rank_type"]
            name = data["name"]
            if rank_type == "5":            
                rankJSON = {}
                rankJSON["count"] = rankCount
                rankJSON["name"] = name
                rankArray.append(rankJSON)
                currentCount = 0
                rankCount = 0        
        print_str += avgRank(rankArray,config['config_name'],currentCount)+"\n"
    print(print_str)

main()