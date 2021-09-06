# Mac端原神抽卡记录导出
由于看了好几个repository都没看到支持Mac，所以决定自己动手写一个脚本，有一定门槛，需要懂抓包&基础的终端命令才会用。  
如果有什么问题，可以到[Issues](https://github.com/Fidetro/genshin-impact-gachalog/issues)上提

# 功能  
- 导出最近6个月抽卡记录  
- 显示抽出对应五星抽了多少抽
- 显示平均一个5星需要多少抽
- 显示已累计多少抽未抽出5星
# 使用方式  

1. 打开游戏->反馈->账号问题->历史设备临时处理->通行证账号管理->复制链接 或者 自行抓包拿到祈愿记录的接口`https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog`,图中用的是`Charles`  
![](https://github.com/Fidetro/genshin-impact-gachalog/blob/master/ad8aa7045d0457d582071fd321d49553.png?raw=true)  



2. 复制对应的接口url后，执行脚本  
```shell
python3 gacha.py 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?xxxxx'
```
3、 预期会出现：
```
============================================
    魈 75 抽
    魈 76 抽
    温迪 68 抽
    刻晴 30 抽
    钟离 55 抽
    角色活动祈愿平均5星: 60.8 抽
    角色活动祈愿已累计: 52 抽未出5星
============================================

============================================
    和璞鸢 55 抽
    风鹰剑 46 抽
    雾切之回光 70 抽
    武器活动祈愿平均5星: 57.0 抽
    武器活动祈愿已累计: 5 抽未出5星
============================================

============================================
    刻晴 26 抽
    阿莫斯之弓 75 抽
    常驻祈愿平均5星: 50.5 抽
    常驻祈愿已累计: 21 抽未出5星
============================================

```  
同时目录下会生成`genshin_常驻祈愿.xls`、`genshin_角色活动祈愿.xls`、`genshin_武器活动祈愿.xls`。  
