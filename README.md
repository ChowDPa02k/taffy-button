# 语音按钮模板

### 需要修改的部分

#### package.json

- **name**字段

#### setting 文件夹

- **color.styl** 颜色配置

```styl
<!-- 主颜色 -->
$main-color = #F5C1BB
<!-- 夜间模式主颜色 -->
$main-color-dark = rgba(245,193,187,0.9)
<!-- 副颜色 -->
$sub-color = #F5F0F2
<!-- 夜间模式副颜色 -->
$sub-color-dark = rgba(245, 240, 242,0.9)
<!-- 按钮文字颜色 -->
$btn-text-color = #5F505F
<!-- 控制栏文字颜色 -->
$title-color = #5F505F
<!-- 夜间模式控制栏文字颜色 -->
$title-color-dark = #999999
<!-- 按钮hover颜色 -->
$hover-color = #bbc5cf
<!-- 按钮active颜色 -->
$active-color = #93a3b3
```

- **setting.json**项目配置

```jsonc
{
  "name": {
    "CN": {
      // Header和网站名
      "title": "语音按钮",
      // MediaSession歌手
      "fullName": ""
    },
    "EN": {
      "title": "Voives Button",
      "fullName": ""
    }
  },
  // Readme组件显示文字，支持HTML
  "readme": "",
  "header": {
    // Header图标URL
    "icon": "img/logo.svg",
    // 外链按钮地址
    "youtube": "",
    "twitter": "",
    "bilibili": ""
  },
  // 友链列表
  "link": [
    {
      // 友链按钮名
      "name": "Hiiro按钮",
      // 友链地址
      "url": "https: //hiiro.club/",
      // 友链按钮颜色
      "background": "#F5C1BB",
      // 友链按钮文字颜色
      "color": "#5F505F"
    }
  ],
  "footer": {
    // 作者列表
    "author": [
      {
        // 作者名
        "name": "Blacktunes",
        // 作者URL，可选
        "url": "https://github.com/blacktunes"
      }
    ],
    // 页脚说明列表，支持HTML
    "info": [""],
    // 项目Github图标地址
    "githubUrl": "https://github.com/blacktunes/voices-button"
  },
  // 控制台输出
  "console": {
    // 控制台输出文字
    "text": "https://github.com/blacktunes/voices-button",
    // 字号，默认16px
    "size": "",
    // 文字颜色
    "color": "",
    // 控制台输出图片名，请放到public/img文件夹
    "img": "",
    // 图片宽度，默认100%
    "imgWidth": "",
    // 图片高度，默认100%
    "imgHeight": ""
  },
  // MediaSession专辑图片名，请放到public/img文件夹
  "mediaSession": "",
  // 语音CDN地址
  "CDN": ""
}
```

#### setting/translate 文件夹

`category.json`和`locales.json`为固定命名，请勿修改

- **category.json** 分类列表

```jsonc
[
  {
    // 分类命名
    "name": "名言",
    // 是否隐藏
    "hide": true,
    "translate": {
      // 分类中文翻译
      "zh-CN": "猫猫名言~",
      // 分类英文翻译
      "en-US": "witticism~"
    }
  }
]
```

- 语音列表文件可任意命名

```jsonc
[
  {
    // 语音命名
    "name": "baba",
    // 语音文件名
    "path": "baba.mp3",
    // 是否隐藏
    "hide": true,
    "translate": {
      // 语音中文翻译
      "zh-CN": "米娜我是你爸爸",
      // 语音英语翻译
      "en-US": "I'm your Baba"
    },
    // 语音所属分类(对应category的name)
    "category": "名言",
    // 以下属性为可选
    // hover时显示图片，请放到public/voices/img目录
    "usePicture": {
      "zh-CN": "",
      "en-US": ""
    },
    // 添加时间
    "date": "2020-11-11",
    // 语音出处
    "mark": {
      "title": "【Hiiro】读评论 学中文 DD们的评论都是什么东西啊？",
      "time": "0:01~0:03",
      "url": "https://www.bilibili.com/video/BV1ET4y177A8"
    }
  }
]
```

#### public 文件夹

- **index.html**的**title**标签
- **favicon.ico**(网站图标)

### 说明

- 点击标题可显示**隐藏**
- 可以的话，请不要删除默认友链

---

## 贡献指南

由于cfm的语音太多，靠我一人的人力必然无法完成足够全面的语音覆盖，因此我在搭建该站点期间，不仅摸透并且搞明白了这套网站的源码，修改了一些部署时会产生的bug，并且捋出了一套从0开始的语音贡献流程，仅需要一点点计算机基础就能够完成。

本项目静态托管在OSS上，已经做到push源码后全自动编译并将数据更新到线上网站中。

### 下载视频

我们推荐使用Python的yt-dlp包进行下载，你需要安装好：

1. Python环境
2. yt-dlp (via pip or conda)
3. ffmpeg build (Optional)

以直播回放举例，直接右键拷贝URL，然后使用

```bash
$ yt-dlp -F [url]
```

查看视频格式，能够获得直播回放的格式表：

![image-20220331173235230](https://geelao-oss.oss-cn-hangzhou.aliyuncs.com/db/202203311732355.png)

我们可以得知，最佳的视频质量为31+2，则使用

```bash
$ yt-dlp -f 31+2 [url]
```

能够将视频下载到本地。

*其中视频非必选项，但是可以在切片的过程中辅助你进行定位。*

如果你未安装FFMPEG，则视频流和音频流不会被合并。

### 切片

使用任何你熟悉的工具进行音频的切片，这部分不在本教程范畴内，但可以展示我本人的工作流：

本人使用Audition，切片先保存为WAV无损格式，然后再使用小丸工具箱转码为128K QAAC。

cfm的直播间音频Dynamic控制尽显专业水准，在这里我建议先把整条音轨+6dB再进行切片处理

**确保你的音频切片码率低于128K以节省网络资源，因为服务器流量消耗花的是我的钱**

![](https://geelao-oss.oss-cn-hangzhou.aliyuncs.com/db/202203311739217.png)

然后，**！必须严格按照以下路径规范保存你的音频切片！**：

每一集单独开设一个文件夹，命名格式为：

```
{{视频标题}}-{{BV号}}

e.g.
起床聊天 2022年3月27日17点场-BV1y44y1A7tF
聊 2022年3月29日19点场-BV1mT4y1i73W
```

文件夹内的切片命名格式为：

```
{{中文名}}-{{英文名}}-{{分类}}-{{日期(%Y%m%d)}}{{-或_}}{{任意内容}}.m4a/mp3/ogg等

e.g.
Cherry就是狗变的-Cherry is a dog-攻击性-20220329_AAC.m4a
锵锵-Clang-可爱-20220329_AAC.m4a
呜呜呜-555-哭泣-20220329_AAC.m4a
开什么玩笑要吐了-What a joke I'm going to throw up-经典名言-20220329_AAC.m4a
```

### 生成配置文件

如果你按照上述规范整理好文件后，在项目文件夹的

```
./public/voices/work
```

中，有一个`voicesListGenerator.py`脚本，用于**根据文件路径名**自动生成配置文件。

将该脚本放在你的工作文件夹中，然后运行：

```
python voicesListGenerator.py
```

将会自动生成名为`voices.json`的配置文件：

![image-20220331175211496](https://geelao-oss.oss-cn-hangzhou.aliyuncs.com/db/202203311752622.png)

TODO：期望能够有开发者实现在npm build时通过node脚本自动根据规则生成并追加内容，使用python只是因为我的惯用编程语言为Py，因此会有些复杂。



### 部署新内容

将生成的`voices.json`放入以下目录，可任意重命名：

```
./setting/translate/
```

将音频文件**不带文件夹地**直接移动到以下目录中：

```
./public/voices
```

如果操作流程正确，使用

```
npm run serve
```

在本地调试，应当能够直接看见新增的语音按钮。

确认无误后，commit并向该repo提交pr。

### 分类

如果你有新的分类，务必在提交PR时告知开发者。

分类的配置文件在：

```
./setting/translate/category.json
```

中，如无特殊情况请遵守该配置文件的分类规则。

当前内置的分类有：

- 经典名言
- 怪话
- 海鸥
- 攻击性
- 可爱
- 怪叫
- 尿频
- 哭泣
- 尖叫

---

### LICENSE

- 使用[voices-button-cli](https://github.com/blacktunes/voices-button-cli)创建的语音按钮
- 所用模板为[Hiiro 按钮](https://github.com/blacktunes/hiiro-button)
