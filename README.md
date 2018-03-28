# alfred workflow tools

一个工作中用到的快速查询alfred小工具，以后需要什么就添加什么. :smile:

## bd

使用[百度翻译](http://api.fanyi.baidu.com/api/trans/product/index). 默认翻译是从auto到en, 也可以自定义翻译语言。

语法为:

<center>bd [[fromLang=auto]>toLang=zh] word</center>

默认fromLang为auto, 注意toLang不能设置为auto。

i.e: 

![](https://github.com/FatShen3/alfred-workflows/blob/master/markdown-images/1.jpg)

![](https://github.com/FatShen3/alfred-workflows/blob/master/markdown-images/2.jpg)

![](https://github.com/FatShen3/alfred-workflows/blob/master/markdown-images/4.jpg)

### 其它操作

* 按回车打开百度翻译对应页面.
* 按cmd+回车发音(使用macos say命令)


### 支持语言

|简写|语言|
|auto|自动识别|
|zh|中文|
|en	|英语|
|yue|	粤语|
|wyw|	文言文|
|jp	|日语|
|kor	|韩语|
|fra	|法语|
|spa|	西班牙语|
|th	|泰语|
|ara	|阿拉伯语|
|ru	|俄语|
|pt	|葡萄牙语|
|de	|德语|
|it	|意大利语|
|el	|希腊语|
|nl	|荷兰语|
|pl	|波兰语|
|bul	|保加利亚语|
|est|	爱沙尼亚语|
|dan|	丹麦语|
|fin|	芬兰语|
|cs	|捷克语|
|rom|	罗马尼亚语|
|slo|	斯洛文尼亚语|
|swe|	瑞典语|
|hu	|匈牙利语|
|cht|	繁体中文|
|vie|	越南语|



## en

编码工具，按回车将编码结果复制到剪切板.

语法为:

**en codetype str**

目前codetype支持如下命令:

* md5
* atob 
  * decode base64 (just as javascript function name)
* btoa
  * encode base64
* sha1

i.e: 

![](https://github.com/FatShen3/alfred-workflows/blob/master/markdown-images/3.jpg)