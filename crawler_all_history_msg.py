
# 微信公众号爬虫：
# 获取“四川大学锦江学院”公众号历史消息【全部】
# 下拉刷新后返回的getmsg更多消息的json数据：
import logging
import utils
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SCUJinjiangCollege:
    def crawl(self):
        """
        更多历史消息文章
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA3NTY3NjUzMg==&f=json&offset=21&count=10&is_ok=1&scene=124&uin=MzAzMDI4NDA4OQ%3D%3D&key=1682b2315ca9ee490093bfa995607ed42db8b3e564d9c1d195dd1a11cfc8ac85e7083817ff8d8d8b13e283c015b191b6bcb2021562c8964a270bc4dce67ed2e9e56d0f35c5bbfa349ef7b63451602810&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&wxtoken=&appmsg_token=1072_IS8epv81t7o7rdJHPiOknOLxKrEuyI3U5AmwbQ~~&x5=0&f=json"
        headers = """Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat
X-Requested-With: XMLHttpRequest
Accept: */*
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA3NTY3NjUzMg==&scene=124&uin=MzAzMDI4NDA4OQ%3D%3D&key=1682b2315ca9ee490093bfa995607ed42db8b3e564d9c1d195dd1a11cfc8ac85e7083817ff8d8d8b13e283c015b191b6bcb2021562c8964a270bc4dce67ed2e9e56d0f35c5bbfa349ef7b63451602810&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&a8scene=7&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&winzoom=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4
Cookie: rewardsn=; wxtokenkey=777; wxuin=3030284089; devicetype=android-27; version=27000f8d; lang=zh_CN; pass_ticket=ZaU5UjhVDMVvsOzkK4i3B/jZubj7dI36zAoLaLuE52eYyRmdeP68Ffs6uiXclfr; wap_sid2=CLnu+aQLElwtRHdCMlZsbmdPMXl3bER5Z3pxbEIyMFpGc0tIMk9nVmkzZkNCOW1FZGQ5WHFXZU0zblBpT1FiajFGOU1WWllpcGVZcGhaWVJLcEpPOER3eGxyaE1pREFFQUFBfjCX0aX5BTgNQJVO"""
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据: offset=%s, data=%s" % (21, msg_list))
        else:
            # 错误消息
            logger.error("错误消息，请检查请求头")
            exit()

if __name__ == '__main__':
    crawler = SCUJinjiangCollege()
    crawler.crawl()