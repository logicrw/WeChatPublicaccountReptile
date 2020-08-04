# 可视化全部数据
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

display_columns = ["标题", "阅读数", "喜欢数", "评论数", "赞赏数", "日期"]

# 从本地MongoDB导入数据
import pymongo
from pymongo import MongoClient

# 链接mongodb
c = MongoClient()
cursor = c.wechat_scujinjiangcollege['post'].find()
df = pd.DataFrame(list(cursor))
# 删除"_id"列
df = df.drop(columns=["_id"], axis=1)
df = df.drop(columns=["content_url"], axis=1)
df = df.drop(columns=["source_url"], axis=1)
df = df.drop(columns=["digest"], axis=1)
df = df.drop(columns=["cover"], axis=1)
df = df.drop(columns=["author"], axis=1)
df = df.drop(columns=["c_date"], axis=1)
df = df.drop(columns=["u_date"], axis=1)
print(df)
# 重设列顺序
# df = df.reindex(columns=display_columns)
# p_data的数据类型： timestamp -> datetime
# date = pd.to_datetime(df['p_date'])
print(df.describe())

# 获取阅读量最高的10篇文章
top_read_num_10 = df.sort_values(by=['read_num'], ascending=False)[:10]
print(top_read_num_10)

# 历史文章阅读量变化曲线
ax = df.plot(y='read_num', x='p_date', title='article read trend', figsize=(9, 6))
ax.set_ylabel('read_count')
ax.set_xlabel('')
ax.legend().set_visible(True)
plt.show()


# 文章与点赞
ax =df.plot(kind="scatter", y="like_num", x="read_num", s=10, figsize=(9,6),
            fontsize=15)
ax.set_xlabel('read_count')
ax.set_ylabel('like_count')
z = np.polyfit(df.read_num, df.like_num, 1)
p = np.poly1d(z)
plt.plot(df.read_num, p(df.read_num), 'r--')
plt.show()

print(df.title)
# 标题关键字
from wordcloud import WordCloud
import  jieba
words = []
for i in df.title:
    seg_list = jieba.cut(i, cut_all=False)
    words.append(" ".join(seg_list))
wordcloud = WordCloud(background_color='white', max_words=80).generate(" ".join(words))
plt.figure(figsize=(9,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
