
# 微信公众号爬虫：
# 获取“四川大学锦江学院”公众号历史消息【全部】
# 下拉刷新后返回的getmsg更多消息的json数据：
import logging
from datetime import datetime
import utils
import requests
import time
import json
import html
# requests.packages.urllib3.disable_warnings()
from urllib.parse import urlsplit
from mongodb import Post

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SCUJinjiangCollege:

    def crawl(self, offset=0):
        """
        更多历史消息文章
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA3NTY3NjUzMg==&f=json&offset={offset}&count=10&is_ok=1&scene=124&uin=MzAzMDI4NDA4OQ%3D%3D&key=9701b8bf0b69875af2605bece0b84ac5791a9cc45d7defc08d4f127acdab2c3ae739842f9f0fd569da86b2db1f91f27c9dff5bab9e5116263572442d555a91bb1cb7b502a908e8443a130fcd032293e6&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&wxtoken=&appmsg_token=1072_6j04Jj7bozTq%252FaFAuTDRNbD8bM4iFMuP3Lbb1g~~&x5=0&f=json".format(offset=offset)
        headers = """Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat
X-Requested-With: XMLHttpRequest
Accept: */*
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA3NTY3NjUzMg==&scene=124&uin=MzAzMDI4NDA4OQ%3D%3D&key=9701b8bf0b69875af2605bece0b84ac5791a9cc45d7defc08d4f127acdab2c3ae739842f9f0fd569da86b2db1f91f27c9dff5bab9e5116263572442d555a91bb1cb7b502a908e8443a130fcd032293e6&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&a8scene=7&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&winzoom=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4
Cookie: rewardsn=; wxtokenkey=777; wxuin=3030284089; devicetype=android-27; version=27000f8d; lang=zh_CN; pass_ticket=ZaU5UjhVDMVvsOzkK4i3B/jZubj7dI36zAoLaLuE52eYyRmdeP68Ffs6uiXclfr; wap_sid2=CLnu+aQLElx6WkYxZHVSVFZOWm01YWhJcjdKSWVLVXozSlNIdnlDY1I5bkpGQ1hMcFNSamZNMDVIZDU2TGQ5ek1TQkpjRVVkZ0tncXZXZDVvUXZza0VTcmhwRlUwakFFQUFBfjCp5KX5BTgNQJVO"""
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据: offset=%s, data=%s" % (offset, msg_list))
            self.save(msg_list) # 保存到数据库
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                next_offset = result.get("next_offset")
                time.sleep(3)
                self.crawl(next_offset)
        else:
            # 错误消息
            logger.error("错误消息，请检查请求头")
            exit()

    @staticmethod
    def save(msg_list):
        msg_list = msg_list.replace("\/", "/")
        data = json.loads(msg_list)
        msg_list = data.get("list")
        for msg in msg_list:
            p_date = msg.get("comm_msg_info").get("datetime")
            msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
            if msg_info:
                SCUJinjiangCollege._insert(msg_info, p_date)
                multi_msg_info = msg_info.get("multi_app_msg_item_list")
                for msg_item in multi_msg_info:
                    SCUJinjiangCollege._insert(msg_item, p_date)
            else:
                logger.warning(u"此消息不是图文推送，data=%s" % json.dumps(msg.get("comm_msg_info")))

    @staticmethod
    def _insert(item, p_date):
        keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
        sub_data = utils.sub_dict(item, keys)
        post = Post(**sub_data)
        p_date = datetime.fromtimestamp(p_date)
        post["p_date"] = p_date
        logger.info('save data %s ' % post.title)
        try:
            post.save()
        except Exception as e:
            logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)

    @staticmethod
    def update_post(post):
        """
        post 参数是从mongodb读取出来的一条数据
        稍后就是对这个对象进行更新保存
        :param post:
        :return:
        """

        # 这个参数是我从Fiddler中拷贝出 URL，然后提取出查询参数部分再转换成字典对象
        # 稍后会作为参数传给request.post方法
        data_url_params = {'__biz': 'MzA3NTY3NjUzMg==', 'appmsg_type': '9', 'mid': '2652567742',
                           'sn': 'c1e80723b9982b85e825e1070dff2cf3', 'idx': '1', 'scene': '38',
                           'title': '%E9%80%89%E6%88%91%E6%B2%A1%E9%94%99%EF%BC%81%E5%B7%9D%E5%A4%A7%E9%94%A6%E6%B1%9F%E6%8B%8D%E4%BA%86%E6%8B%8D%E4%BD%A0',
                           'ct': '1595660850',
                           'abtest_cookie': '',
                           'devicetype': 'Windows 10 x64',
                           'version': '62090529', 'f': 'json',
                           'r': '0.815280901005569', 'is_need_ad': '0', 'comment_id': '1443991147038441474',
                           'is_need_reward': '1', 'both_ad': '0', 'reward_uin_count': '24', 'msg_daily_idx': '1',
                           'is_original': '0', 'uin': 'MzAzMDI4NDA4OQ==', 'key': '1682b2315ca9ee496ced1069afbde4e355182c3cc85404049b57d7403fc7434524ed3579f779a4426cfbcd977a1047432db2e171f317e5c2f9ddea95c1f462e8f24e5590746562ab482cd133b73a7682',
                           'pass_ticket': 'ZaU5UjhVDMVvsOzkK4i3B/jZubj7dI36zAoLaLuE52eYyRmdeP68+Ffs6uiXclfr',
                           'wxtoken': '777', 'clientversion': '62090529',
                           'appmsg_token': '1072_WbRi1PaTNQtHiysKbI2hg1LUqGTnT1OboYeqO0MRHgalIVUArGz-Q8bsEnuoNL3swxRUvL-HSZUgMxFT',
                           'x5': '0'}  # appmsg_token 记得用最新的

        # url转义处理
        content_url = html.unescape(post.content_url)
        # 截取content_url的查询参数部分
        content_url_params = urlsplit(content_url).query
        # 将参数转化为字典类型
        content_url_params = utils.str_to_dict(content_url_params, "&", "=")
        # 更新到data_url
        data_url_params.update(content_url_params)
        body = "r=0.815280901005569&__biz=MzA3NTY3NjUzMg%3D%3D&appmsg_type=9&mid=2652567742&sn=c1e80723b9982b85e825e1070dff2cf3&idx=1&scene=38&title=%25E9%2580%2589%25E6%2588%2591%25E6%25B2%25A1%25E9%2594%2599%25EF%25BC%2581%25E5%25B7%259D%25E5%25A4%25A7%25E9%2594%25A6%25E6%25B1%259F%25E6%258B%258D%25E4%25BA%2586%25E6%258B%258D%25E4%25BD%25A0&ct=1595660850&abtest_cookie=&devicetype=Windows%2010%20x64&version=62090529&is_need_ticket=0&is_need_ad=0&comment_id=1443991147038441474&is_need_reward=0&both_ad=0&reward_uin_count=0&send_time=&msg_daily_idx=1&is_original=0&is_only_read=1&req_id=0422J3pAP3U6ZfMyvrA9qY2z&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&is_temp_url=0&item_show_type=0&tmp_version=1&more_read_type=0&appmsg_like_type=2&related_video_sn=&related_video_num=4&vid=&is_pay_subscribe=0&pay_subscribe_uin_count=0&has_red_packet_cover=0&album_id=1296223588617486300&album_video_num=5"
        data = utils.str_to_dict(body, "&", "=")

        # 通过Fiddler 获取 最新的值
        headers = """
 Host: mp.weixin.qq.com
Connection: keep-alive
Content-Length: 919
Origin: https://mp.weixin.qq.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&mid=2652567742&idx=1&sn=c1e80723b9982b85e825e1070dff2cf3&chksm=8482b6a5b3f53fb3970b3b3701415037bf633b06da98d2dc4c63d476e9a5ce7bd8762d5b27a0&scene=38&key=1682b2315ca9ee496ced1069afbde4e355182c3cc85404049b57d7403fc7434524ed3579f779a4426cfbcd977a1047432db2e171f317e5c2f9ddea95c1f462e8f24e5590746562ab482cd133b73a7682&ascene=7&uin=MzAzMDI4NDA4OQ%3D%3D&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&exportkey=A%2Fuw0CgT2zB13kyRA3OogXM%3D&pass_ticket=ZaU5UjhVDMVvsOzkK4i3B%2FjZubj7dI36zAoLaLuE52eYyRmdeP68%2BFfs6uiXclfr&winzoom=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4
Cookie: rewardsn=; wxtokenkey=777; wxuin=3030284089; devicetype=Windows10x64; version=62090529; lang=zh_CN; pass_ticket=ZaU5UjhVDMVvsOzkK4i3B/jZubj7dI36zAoLaLuE52eYyRmdeP68+Ffs6uiXclfr; wap_sid2=CLnu+aQLElxUNi05blptTWUxVDN3dnI0blRoUXJVcWhOSmpIMWJWWW55SThUcGpHREtQMjJNRWtZMDRtOEhxMUJyNGZfWDZXbUd5MWtReGxXWkd0NFZDNTZMOFFEekFFQUFBfjD16aX5BTgNQAE=
 """

        headers = utils.str_to_dict(headers)

        data_url = "https://mp.weixin.qq.com/mp/getappmsgext"

        r = requests.post(data_url, data=data, verify=False, params=data_url_params, headers=headers)

        result = r.json()
        if result.get("appmsgstat"):
            post['read_num'] = result.get("appmsgstat").get("read_num")
            post['like_num'] = result.get("appmsgstat").get("like_num")
            post['reward_num'] = result.get("reward_total_count")
            post['u_date'] = datetime.now()
            logger.info("「%s」read_num: %s like_num: %s reward_num: %s" %
                        (post.title, post['read_num'], post['like_num'], post['reward_num']))
            post.save()
        else:
            # data={"base_resp":{"ret":301,"errmsg":"default"}}这是微信的反扒机制
            logger.warning(u"没有获取的真实数据，请检查请求参数是否正确，返回的数据为：data=%s" % r.text)
            exit()


if __name__ == '__main__':
    crawler = SCUJinjiangCollege()
    # crawler.crawl()
    for post in Post.objects(reward_num=0):
        crawler.update_post(post)
        time.sleep(1)
