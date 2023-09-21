# 导入模块
import requests
import re # 内置库

# 确定 url
url = 'http://www.weather.com.cn/weather/101010700.shtml'

# 发请求，获取响应
res = requests.get(url)

# 出现乱码，进行编码
res.encoding = 'utf-8'

# 打印响应内容
# print(res.text)

# 做数据解析
# re.match 从头开始找，最开始就没有匹配返回 None
# .匹配任意一个字符，但是 \n 符号不匹配
# re.S 帮助.匹配到换行符
result = re.match('.*(<ul class="t clearfix">.*?</ul>).*', res.text, re.S)

# 获取 ul 标签里面的内容，一个括号分一个组，如果取第一个括号里面的内容，1
ul = result.group(1)

# 贪婪模式与非贪婪模式
# .* 尽可能匹配多的字符
# .*? 尽可能匹配少的字符
lis = re.findall('<li.*?>.*?</li>', ul, re.S)

# 遍历每一个 li 标签，拿到每一组数据 compile() 模板
pattern = re.compile('<li.*?<h1>(.*?)</h1>.*?<p.*?>(.*?)</p>.*?<i>(.*?)</i>.*?<i>(.*?)</i>.*', re.S)
for li in lis:
    # print(li)
    r = pattern.match(li)
    print(r.group(1), r.group(2), r.group(3), r.group(4))
    # break