import pymysql
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
con = pymysql.connect(host='localhost',user='root',passwd='hadoop',db='keshe2',port=3306,charset='utf8')
cur = con.cursor()
sql = 'select * from cipin'
cur.execute(sql)
see = cur.fetchall()

word = []
count = []
str_=""
for data in see:
    # for cishu in range(data[1]):
        str_=str_+' '+data[0]
    # word.append(data[0])
    # count.append(data[1])
print(word)
print(count)
print(str_)

cur.close()
con.close()


def makewordcloud(str_):

    print(str_)

    wcheight = 500
    wcwidth = 500
    wc = WordCloud(
        font_path='///usr/share/fonts/msyhl.ttc',
        # 设置字体，不指定就会出现乱码
        # 设置背景色
        background_color='white',
        # 设置背景宽
        width=wcwidth,
        # 设置背景高
        height=wcheight,
        # 最大字体
        max_font_size=100,
        # 最小字体
        min_font_size=10,
        # 屏蔽词
        stopwords=['既然','要','第二','现在','当下','希望'],
        # 词汇数量
        max_words=300,
        # 颜色模型
        mode='RGBA',
        # 为每个单词随机绘制颜色
        colormap='summer',
        # 是否重复使用关键词
        repeat=False,
        # mask=np.array(Image.open('edgnb.jpg'))
    )
    # 产生词云
    wc.generate(str_)
    # 保存图片
    wc.to_file("wordcloud.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
    return wc
# 配置plt,否则标签会显示乱码
def setplt():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
# 对分析的词云结果做词云图展示
def showp(wc):
    setplt()
    # 4.显示图片
    # 指定所绘图名称
    plt.figure("招聘要求词云图")
    # 以图片的形式显示词云
    plt.imshow(wc)
    # 关闭图像坐标系
    plt.axis("off")
    plt.show()

def dealLogic():
    wc = makewordcloud(str_)
    showp(wc)
# 主函数
def main():
    dealLogic()
if __name__ == "__main__":
    main()
