import requests
import re
import os
import json
"""请输入想要的清晰度，数字越高清晰度越低，0为最高清晰度"""
quality = 0

url = input('请输入url地址：')
print(f'url地址为:{url}')
print()

print('······获取网页源代码中······')
headers = {
    'Referer': "https://www.bilibili.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    "Cookie": "buvid3=43CAB701-090F-87DB-249E-34CBC6D16F0C81045infoc; i-wanna-go-back=-1; b_lsid=B10C4310AF_17E9A45F3D9; _uuid=E145C5FF-1079C-16ED-8EBF-6FC68FAE42BC82758infoc; buvid4=AA587054-A73F-D521-D6C6-AE0A1DD7157C83625-022012714-kQX+zlqLtJOPCa19J7/+Hw%3D%3D; CURRENT_BLACKGAP=0; fingerprint=a7e8cac5673c057781c866b795f68f1d; buvid_fp_plain=undefined; buvid_fp=581ab9f28ad1d3f40722df336ef13218; SESSDATA=1d6a85a8%2C1658817818%2C3bb73%2A11; bili_jct=e984ce29a16df280701c8935ac1bb5bd; DedeUserID=363847475; DedeUserID__ckMd5=10fb51d003f11b1c; sid=6nxasi0u; b_ut=5; LIVE_BUVID=AUTO4416432658293514; CURRENT_FNVAL=4048; blackside_state=1; rpdid=|(u))ku)um~)0J'uYRJkYYRJl; CURRENT_QUALITY=64; bp_video_offset_363847475=620308155041103600; innersign=1; PVID=2"
}

response_url = requests.get(url,headers=headers)
#print(response_url.text)
print('——————成功获取网页源代码——————')
print()

print('······正在获取视频标题······')
title = re.findall('"title":"(.*?)"',response_url.text)[0]
title = title.replace('"',"'")
print(f'标题为:{title}')
print('——————成功获取标题——————')
print()

print('······正在解析视频、音频地址······')
all_1 = re.findall('<script>window.__playinfo__=(.*?)</script>',response_url.text)[0]
all_2 = json.loads(all_1)
url_2 = all_2['data']['dash']['audio'][0]['baseUrl']
url_1 = all_2['data']['dash']['video'][quality]['baseUrl']
print(f'地址_1为:{url_1}')
print(f'地址_2为:{url_2}')
print('——————成功解析视频、音频地址——————')
print()

print('······正在保存视频、音频文件······')
response_url_1 = requests.get(url_1,headers=headers).content
response_url_2 = requests.get(url_2,headers=headers).content
with open('_1_.mp4',mode='wb') as f:
    f.write(response_url_1)
with open('_1_.mp3',mode='wb') as f:
    f.write(response_url_2)
print('——————成功保存视频、音频文件——————')
print()

print('······正在合成视频······')   # 视频的合成，使用第三方工具 ffmpeg
os.system(f'ffmpeg.exe -i _1_mp4 -i _1_.mp3 -c copy "{title}.mp4"')
print('——————成功合成视频——————')
print()

os.remove('_1_.mp4')
os.remove('_1_.mp3')
print(f'合成的视频标题为:{title}.mp4')
print('——————程序已结束——————')
print('————ps: _1_.mp4 与 _2_mp3 为程序运行时的临时文件，可手动删除————')
