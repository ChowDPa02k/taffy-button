import os
import re
from datetime import datetime
import json

voices = []

for root, dirs, files in os.walk('.'):
    # 分割目录，获取视频标题和BV号
    source = root[2:].split('-')
    if len(source) < 2:
        continue
    title = source[0]
    vid = source[1]
    for fp in files:
        (fn, ext) = os.path.splitext(fp)
        # 只取AAC，后续可以自行修改成你的格式
        if ext == '.m4a':
            # 分割文件名，获取信息，生成字典
            fileInfo = re.split('-|_', fn)
            voices.append({
                'name':
                fileInfo[0],
                'path':
                fp,
                'date':
                datetime.strptime(fileInfo[3], '%Y%m%d').strftime('%Y-%m-%d'),
                'translate': {
                    "zh-CN": fileInfo[0],
                    "en-US": fileInfo[1]
                },
                "usePicture": {
                    "zh-CN": "",
                    "en-US": ""
                },
                'category':
                fileInfo[2],
                'mark': {
                    'title': title,
                    'time': "",
                    'url': "https://www.bilibili.com/video/" + vid
                }
            })

# 写入Json，拿来即用
with open('voices.json', 'w', encoding='utf-8') as f:
    json.dump(voices, f, ensure_ascii=False)