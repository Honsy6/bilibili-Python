import requests
import pprint
import re
import json
import os
import time
"""请输入想要的清晰度，数字越高清晰度越低，0为最高清晰度"""
quality = 0      #根据需要直接改数字就好了


html = input('请输入其中一个视频的url地址：')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com'
}

print('······正在解析列表······')
response_html = requests.get(html,headers)
list_all = json.loads(re.findall('"episodes":(.*?),"isActive":',response_html.text)[0])
list_title, list_id = [], []
for i in range(len(list_all)):
    list_title_1, list_id_1 = list_all[i]['title'], list_all[i]['bvid']
    list_title.append(list_title_1)
    list_id.append(list_id_1)
print('————————————————————————————————————————————————————————————————————————————')
if len(list_id) >= 5:
    print(f"————————————列表过长，显示爬取的列表前五视频名称与ID————————————")
    for i in range(5):
        print(f'|— {list_id[i]} —+— {list_title[i]} —|')
elif len(list_id) < 5:
    print(f"————————————————显示要爬取的列表视频名称与ID————————————————")
    for i in range(len(list_id)):
        print(f"|— {list_id[i]} —+— {list_title[i]} —|")
print('————————————————————————————————————————————————————————————————————————————')
print(f"将爬取的视频一共{len(list_id)}个\n——————列表解析完毕——————\n")
time.sleep(5)

def ToRequestsVideo(url_id,title):
    url = f'https://www.bilibili.com/video/{url_id}'

    print('······获取网页源代码中······')
    response_url = requests.get(url,headers=headers)
    print('——————成功获取网页源代码——————\n')

    print('······正在解析视频、音频地址······')
    all_1 = re.findall('<script>window.__playinfo__=(.*?)</script>',response_url.text)[0]
    all_2 = json.loads(all_1)
    oopp = all_2['data']['dash']['audio']     #判断是否有音频地址
    if oopp == '' or oopp == 'rull' or oopp == None:
        opp = 1
    else:
        opp = 0
        url_2 = all_2['data']['dash']['audio'][0]['baseUrl']
    url_1 = all_2['data']['dash']['video'][quality]['backupUrl'][0]
    print('——————成功解析视频、音频地址——————\n')

    print('······正在保存视频、音频文件······')
    response_url_1 = requests.get(url_1,headers=headers).content
    with open('_2_.mp4',mode='wb') as f:
        f.write(response_url_1)
        f.close()
    if opp == 0:              #有音频地址
        response_url_2 = requests.get(url=url_2,headers=headers).content
        with open('_2_.mp3',mode='wb') as f:
            f.write(response_url_2)
            f.close()

    print('——————成功保存视频、音频文件——————\n')

    print('······正在合成视频······')   # 视频的合成，使用第三方工具 ffmpeg
    if opp == 0:       #有音频与视频合成
        os.system(f'ffmpeg.exe -i _2_.mp4 -i _2_.mp3 -c copy "{title}.mp4"')
    elif opp == 1:     #无音频与视频合成
        os.system(f'ffmpeg.exe -i _2_.mp4 "{title}.mp4"')
        print('————无音频————')
    print('——————成功合成视频——————\n')
    time.sleep(2)

for i in range(len(list_all)):
    print(f'————————正在爬取{i+1}/{len(list_all)}   视频ID为:{list_id[i]}  视频标题为:{list_title[i]}\n')
    ToRequestsVideo(list_id[i], list_title[i])

os.remove('_2_.mp4')
os.remove('_2_.mp3')
print('——————程序已结束——————')
print('————ps: _2_.mp4 、与 _2_.mp3 为程序运行时的临时文件，运行结束后可手动删除————')

