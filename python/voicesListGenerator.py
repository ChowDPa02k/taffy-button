import os
import re
from datetime import datetime
import json

voices = []
count = {}

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
            # 分割文件名，获取信息
            fileInfo = re.split('-|_', fn)
            # vue中按钮渲染的key与name绑定，如果出现key重复会导致页面显示的时候出现错位问题
            if fileInfo[0] in count:
                resourceName = fileInfo[0] + str(count[fileInfo[0]])
                count[fileInfo[0]] = count[fileInfo[0]] + 1
            else:
                resourceName = fileInfo[0]
                count[fileInfo[0]] = 1
            # 生成字典
            voices.append({
                'name':
                resourceName,
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
with open('voices_3c.json', 'w', encoding='utf-8') as f:
    json.dump(voices, f, ensure_ascii=False)