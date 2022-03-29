import requests
import re
print('''
此爬虫针对bilibili新品种——音频视频不分家的视频！！！
如果遇到正确操作“bilibili爬虫完全版”仍然报错的现象，可以使用此爬虫试一试
如有需要爬取音频视频分家视频请前往”bilibili爬虫完全版“！！！
ps：bilibili上的视频大多都是音频视频分家的。
''')
print()

url = input("请输入url:")
print('爬取的视频网页url为：'+url)

headers = {
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'cookie': "rpdid=|(u))ku)kk~Y0J'uYRR~YRmkY; b_nut=1644765205; buvid3=6016E56A-31D4-740E-E663-68766866F99B95789infoc; buvid4=97AA56BB-BDEA-732D-DE39-83F5B961A49195789-022021323-kQX+zlqLtJMg72J5eWc2Yg%3D%3D; _uuid=8CBD1061C-D1410-E7B7-7C96-7BB222DA5CCE56675infoc; blackside_state=1; buvid_fp_plain=undefined; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO5916452764178826; b_ut=5; fingerprint=a7e8cac5673c057781c866b795f68f1d; buvid_fp=581ab9f28ad1d3f40722df336ef13218; SESSDATA=0469625a%2C1661435386%2Cb433f%2A21; bili_jct=262adaf4a3d0dc76081d8c8e6b3aa252; DedeUserID=363847475; DedeUserID__ckMd5=10fb51d003f11b1c; sid=avlzu0na; nostalgia_conf=-1; PVID=1; CURRENT_QUALITY=64; innersign=1; CURRENT_FNVAL=4048; b_lsid=9E56BEB6_17FAB8CDFF2; bp_video_offset_363847475=640003732673658900"
}
print()
print('··············正在获取网页源代码··············')
response_url = requests.get(url=url,headers=headers)

print(response_url.text)

print('——————————————成功获取网页源码——————————————')
print()

print('··············正在获取视频标题··············')
title = re.findall('"title":"(.*?)","',response_url.text)[0]
title = title.replace(' ',"_")
title = title.replace('&',"_and_")
print('标题为：'+title)
print("——————————————成功获取视频标题——————————————")
print()

print('··············正在获取视频播放地址··············')
url_1 = re.findall('"url":"(.*?)",',response_url.text)[0]   # 跟完全版一样，这里可以改视频清晰度
print(url_1)
print('——————————————成功获取视频播放地址——————————————')
print()

print('··············正在保存视频··············')
response_1 = requests.get(url=url_1,headers=headers).content
with open(title+'.mp4',mode='wb') as f:
    f.write(response_1)
f.close()
print('——————————————视频保存完毕——————————————')

print('保存视频标题为：'+title+'.mp4')


