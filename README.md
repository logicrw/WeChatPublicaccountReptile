# :globe_with_meridians:微信公众号爬虫

如果你喜欢这个小项目，请为我点个Star !  

感谢:heart:



------



### :chart_with_downwards_trend:需求：

- 爬取【四川大学锦江学院*公众号】全部历史文章数据
- 将爬取的文章数据本地持久化存储到MongoDB数据库中[python中的ORM框架：pip install mongoengine]
- 获取文章的阅读数、点赞数、评论数等
- Matplotlib数据可视化展示

通过MongoExport工具，将爬取到的数据保存到MongoDB的数据导出为csv文件。

可在项目查看到wechat.csv，这就是最终的爬取的数据集合。



### :bug:爬取目标: 

- 四川大学锦江学院【公众号】



### :department_store:代码说明：

进行了如下爬虫编写：

- 获取四川大学锦江学院最新的10条历史记录
- 获取四川大学锦江学院全部的历史记录
- 关于Windows版微信如何进入公众号的全部历史界面和相关Fiddler关键位置抓包截图可参考doc下的截图文件

> windows下启动MongoDB服务：cmd -> mongod
>
> 如果是启动客户端： cmd -> mongo

:stuck_out_tongue:软件和工具：

- PyCharm 2020.1.3版【激活可联系我】
- 抓包Fiddler
- WeChat【Windows版】
- JSON-handle【json格式化预览插件 ……Chrome版】
- Robo3T 【MongoDB可视化工具】

------

### 返回的json数据说明：

```json
{
    "ret": 0,
    "errmsg": "ok",
    "msg_count": 10,
    "can_msg_continue": 1,
    "general_msg_list": "{\"list\":[{\"comm_msg_info\":{\"id\":1000001005,\"type\":49,\"datetime\":1593761521,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"重磅预告丨川大锦江招生咨询网上直通车\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081730,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565391&amp;idx=1&amp;sn=613c58d794d49f0f1b7e8ca0759d3bbc&amp;chksm=8482a194b3f5288247011a683df0cfc3f8fa7fbeeed2ab60d035c110a8e5572e0d5f31f3ad59&amp;scene=27#wechat_redirect\",\"source_url\":\"https://b.u.h5mc.com/c/oiha/qhsb/index.html?t=886912004&amp;custom=&amp;crid=&amp;s=1\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBEIax387VoTG8RddC8b3Gc3O2icetnADnNESG47fUX3VQRCMicXiaE1WAxzibCV99Ew9MXXNHFkCm4lRg/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"\",\"copyright_stat\":100,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000001004,\"type\":49,\"datetime\":1593696476,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"川大锦江打造“最催泪”云毕业典礼\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081699,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565373&amp;idx=1&amp;sn=d9e689d0dbbabeab445ac7ff6bf84a58&amp;chksm=8482a166b3f528700ddf0bf6f2fdd9acc8d8e5766ea49f6a79e5da37c101ba237b27955d65d5&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBEScqsNXyhUmstH90oictRicUsQDLjQUnzjcvkxaC1BubiaNO4l4mF6F6LCYxLOI3nK2VI0DKqPhds6w/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000001003,\"type\":49,\"datetime\":1593615877,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"四川大学锦江学院马克思主义学院揭牌成立\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081644,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565329&amp;idx=1&amp;sn=289f9354f847213cd5227281fb4e3576&amp;chksm=8482a14ab3f5285c6437088a46f2fdeeb377114710295fbbb61b15e309bcf968c7cabe095637&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBHWhicAk8sUqnzkE21pbwSYjW6ariceyrJbhz2jbKIh4nhXGguevjE0PCjPtzd7iaM7AOCo6HOg8Rxiag/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":1,\"multi_app_msg_item_list\":[{\"title\":\"学校举行庆祝中国共产党成立99周年暨表彰会\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081654,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565329&amp;idx=2&amp;sn=89c48f2d481b72422a036276ed1f08c8&amp;chksm=8482a14ab3f5285c1de6bed49a7f8df11ad455579ee141aa5763eec2534de3596125c5549ecd&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBHWhicAk8sUqnzkE21pbwSYjcRL0aa0Ir3V5Pnxxtamt0KzuicCerDUceqYkJ3El9DSxT0Jsvg08Kxw/0?wx_fmt=jpeg\",\"author\":\"锦江官微\",\"copyright_stat\":100,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"duration\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000001002,\"type\":49,\"datetime\":1593526920,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"重磅预告丨川大锦江“云”毕业典礼  与你相约\",\"digest\":\"内含“云上创意毕业照DIY大礼包”\",\"content\":\"\",\"fileid\":505081637,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565288&amp;idx=1&amp;sn=8584cf5988585237a7a39cf1727117fd&amp;chksm=8482a133b3f528253a94c21c98b3bb66e7aee2d70540c62167db1c65abbc1f1473293e18505c&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBH4hkpjdmor4ibAcnmVhEslydoMRKP9rZibk1ksiawQfT5Kia7EU7ZmUI17qIjPz40cz2L98XLRic2CeWg/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000001001,\"type\":49,\"datetime\":1593154247,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"线上线下同频共振！川大锦江教师的硬核课堂\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081607,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565264&amp;idx=1&amp;sn=d8f3e4881be676ec6235461331ee1848&amp;chksm=8482a10bb3f5281da87809911e7a58ca78ffefd970b9f84716d5a9002fd0c729f448545646cd&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBG8qjPEDtJk44g4NWLQkZy4Jsom05ammxyg1npbiaiatp5rm4ykeOrMXicaN6Z7XJBWKQGiaEyFv7IeFQ/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000001000,\"type\":49,\"datetime\":1592989305,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"权威发布丨四川大学锦江学院2020年招生章程\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081557,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565245&amp;idx=1&amp;sn=94024cc8014681d497b4f731f651dc2d&amp;chksm=8482a0e6b3f529f0dcee7246d05b7fe6ee53531b9918f827be055fc5a0563447ecf9e77c80a4&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBH0B3AibCoDliab1Ticr1g9zyKq255k449wu0GEwQl9jR3smic2HhPL8xj7BNmcIvB5Jb3ESJqLQhqjpQ/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"\",\"copyright_stat\":100,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000000999,\"type\":49,\"datetime\":1592811279,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"@高考生   川大锦江专属盲盒到啦！\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081523,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565221&amp;idx=1&amp;sn=834d3f84d962c0ae468000e3ac6db4a0&amp;chksm=8482a0feb3f529e84904a8c4f9757017296cb4a728e0194b37a3c2666b8469e5d9890a7deb0c&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_png/lTxxRKoWBBFtNDEdZeruTNEdWfdeGgpXm0GX7Gn2TdVGsJXtx8ibnEJCYrBH0V11Gfo7997X1PHfJe0ic1RFQpyQ/0?wx_fmt=png\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000000998,\"type\":49,\"datetime\":1592399818,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"重启校园时光，这些瞬间好美！\",\"digest\":\"\",\"content\":\"\",\"fileid\":0,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652565170&amp;idx=1&amp;sn=3f5c15f9894d98f50384ed636f4e0531&amp;chksm=8482a0a9b3f529bf1cea8fe8d6948013dd849cd789e2e1ab14aaa154bc368e5c15adffec4110&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBFUsI2KY1FVpEbaLyLXXXSBpbTPhicCnuATZ8TwicOFXLnMib4fBvD2w0n0g7DVbcrnF07VWKgykHFrg/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000000997,\"type\":49,\"datetime\":1592230156,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"返校复课第一天 教学秩序井然\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081322,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652564974&amp;idx=1&amp;sn=4fece5fe00007bab7b1c0a384f274c97&amp;chksm=8482a3f5b3f52ae31149824aedfdc15bcb9d22d45cc6475fa1e42b49da669b1820fd8c220c29&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBGE38vleCocosRiajhOfUYUUgqWV7vsGohTG97vOQ8frtxOlr6ia8kHfAqcSOl5uwJlGZLzFDVP9tag/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":100,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}},{\"comm_msg_info\":{\"id\":1000000996,\"type\":49,\"datetime\":1591869656,\"fakeid\":\"3075676532\",\"status\":2,\"content\":\"\"},\"app_msg_ext_info\":{\"title\":\"去往更高处 遇见更好的自己\",\"digest\":\"\",\"content\":\"\",\"fileid\":505081251,\"content_url\":\"http://mp.weixin.qq.com/s?__biz=MzA3NTY3NjUzMg==&amp;mid=2652564920&amp;idx=1&amp;sn=1cdedaa995906c1e0a4583b1c656270a&amp;chksm=8482a3a3b3f52ab513103d21167a238276e19468d7dddb3309f55eeeb226da0feebfadc44277&amp;scene=27#wechat_redirect\",\"source_url\":\"\",\"cover\":\"http://mmbiz.qpic.cn/mmbiz_jpg/lTxxRKoWBBHFygwxp4Cbu3Fficey2bicuE8n8F6ohCoMbukqJW9fD279tOTD3EicLB3HXedUgd7B8U4yvN4bW6DKg/0?wx_fmt=jpeg\",\"subtype\":9,\"is_multi\":0,\"multi_app_msg_item_list\":[],\"author\":\"锦江官微\",\"copyright_stat\":11,\"duration\":0,\"del_flag\":1,\"item_show_type\":0,\"audio_fileid\":0,\"play_url\":\"\",\"malicious_title_reason_id\":0,\"malicious_content_type\":0}}]}",
    "next_offset": 31,
    "video_count": 1,
    "use_video_tab": 1,
    "real_type": 0,
    "home_page_list": []
}
```

以上是全部历史消息请求返回的json格式数据

具体字段的含义：

- ret: 请求是否成功。0代表成功
- msg_count: 返回的数据条数
- can_msg_continue: 是否还有下一页数据
- next_offset: 下一次请求的起始位置
- general_msg_list: 真实数据

其中general_msg_list是历史文章里面的基本信息。包括每篇文章的：

- 标题
- 发布时间
- 摘要
- 链接地址
- 封面图

对于文章的阅读数、评论数、赞赏数等数据则需要通过其他接口获取【Fiddler抓包自行查看】

------

### :thinking:爬取更多页的公众号历史文章思路：

根据上面返回的json可以根据字面意思推断出：

- 字段can_msg_continue可以确定是否继续抓取
- 字段next_offset可以加载更多的数据

然后经过Fiddler多次抓包发现，在windows的微信上多次往下滚，会发送很多请求，但是这些请求基准地址是不变的，变化的只是url中的参数，符合软件开发中的GET请求规范。

那么是不是每次改变url中的请求参数就可以达到分页请求效果呢？

观察发现：offset参数是可变的。

那么只需要把url中的可变参数offset用变量替代，然后调用，直到请求返回的json数据中的can_msg_continue字段的值为0即表示全部历史文章获取完毕。



