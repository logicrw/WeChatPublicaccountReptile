# 微信公众号爬虫： 四川大学锦江学院

# 1. 找到完整的URL请求地址（通过Fiddler抓包实现）
# 2. 找到完整的请求头信息,Headers里面包括了cookie User-agent Host等信息
import requests

def headers_to_dict(headers):
    """
    将字符串转换为字典对象
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k.strip()] = v.strip()
    print(d_headers)
    return d_headers

# 如果获取失败，检查Headers中的Cookie是否过期了，及时Fiddler抓包重新更换
def crawl():
    url = "https://mp.weixin.qq.com/mp/profile_ext" \
          "?action=home" \
          "&__biz=MzA3NTY3NjUzMg==" \
          "&scene=124" \
          "&uin=MzAzMDI4NDA4OQ%3D%3D" \
          "&key=9853f5dfd5cd58d682ccb1292ad7c8d45402a6845d83be0088b9e9a69a2dde8bb5a6bcec6f3934d527319eeb9172c4f77d02e47167ec0c650128c9b6cb6af0efa3f9d443a0a3ea220e2799d6f9b6ec8d" \
          "&devicetype=Windows+10+x64" \
          "&version=62090529" \
          "&lang=zh_CN" \
          "&a8scene=7" \
          "&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr" \
          "&winzoom=1"
    headers = """Host: mp.weixin.qq.com
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4
        Cookie: rewardsn=; wxtokenkey=777; wxuin=3030284089; devicetype=Windows10x64; version=62090529; lang=zh_CN; pass_ticket=ZaU5UjhVDMVvsOzkK4i3B/jZubj7dI36zAoLaLuE52eYyRmdeP68+Ffs6uiXclfr; wap_sid2=CLnu+aQLElxsWi1BWHpDMlFoS1A0UjY2ak5TQTJYTUppcGxHX2lvS21teE00M1U2TERKN0FNdy16RmJHUThCc3VDekpOejN1VFdOUU5GYV9URjFuTHdYTk5vekxTakFFQUFBfjC9qqX5BTgNQJVO"""
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    with open("weixin_jinjiang_history.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    # 然后打开保存好的源代码，可以发现文章历史标题封装在 var msgList数组里, 里面是json格式数据

def extract_data(html_content):
    """
    提取历史文章数据：
    1。 正则体术数据内容
    2. html转义处理得到一个列表对象
    3. 返回最近发布的10篇文章
    :param html_content:
    :return:
    """
    import re
    import html
    import json
    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data) # html转义，比如  var msgList = '{&quot;list&quot;:[{&quot;comm_msg_info&quot;:
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles



if __name__ == '__main__':
    # crawl()
    with open("weixin_jinjiang_history.html", "r", encoding="utf-8") as f:
        articles_last_10 = extract_data(f.read())
        print(articles_last_10)
        """
        返回的数据类似这样：
        {'comm_msg_info': {'id': 1000001026, 'type': 49, 'datetime': 1596362856, 'fakeid': '3075676532', 'status': 2, 'content': ''}, 'app_msg_ext_info': {'title': '来看剧吧！', 'digest': '', 'content': '', 'fileid': 0, 'content_url': 'http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652567815&amp;idx=1&amp;sn=1e46e36f588b24fae80582953ca4aaba&amp;chksm=8482b71cb3f53e0a82e3016e5dfca6e1b30acdc27cea810a4e7cbf00d22da64fcded14191637&amp;scene=27#wechat_redirect', 'source_url': '', 'cover': '', 'subtype': 9, 'is_multi': 0, 'multi_app_msg_item_list': [], 'author': '', 'copyright_stat': 100, 'duration': 59, 'del_flag': 1, 'item_show_type': 7, 'audio_fileid': 2652567814, 'play_url': 'https://res.wx.qq.com/voice/getvoice?mediaid=MzA3NTY3NjUzMl8yNjUyNTY3ODE0', 'malicious_title_reason_id': 0, 'malicious_content_type': 0}}
        comm_msg_info: 发送时间
        app_msg_ext_info: 文章的具体信息
        """
