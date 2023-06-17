import numpy as np
import matplotlib.pyplot as plt

# 统计每天评论数给出折线图
def PerDayCommentLine(): 
    plt.subplot(1,1,1)
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,])
    y = np.array([107,79,158,108,109,141,111,104,114,95,146,128])
    plt.rcParams['font.sans-serif']=['KaiTi']
    plt.rcParams['axes.unicode_minus']=False
    plt.plot(x,y,color="k",linestyle="dashdot",
            linewidth=1,marker="o",markersize=5,label="评论量")
    plt.title("2021年各月份《Python从入门到实践》评论量",loc="center")
    for a,b in zip(x,y):
        plt.text(a,b,b,ha='center',va="bottom",fontsize=10)
    plt.grid(True)
    plt.legend()
    # plt.savefig(r"C:\Users\xiaoLiu\Desktop\keshihua\1.jpg")
    plt.show()

# 统计每个评分段（score）的人数给出柱状图
def PerScoreCol:
    import numpy as np
    import matplotlib.pyplot as plt
    plt.subplot(1,1,1)
    fig=plt.figure()
    plt.figure(figsize=(8,6))
    plt.rcParams['font.sans-serif']=['KaiTi']
    plt.rcParams['axes.unicode_minus']=False
    x=np.array(["一星","二星","三星","五星"])
    y=np.array([192,71,128,923])
    plt.bar(x,y,width=0.5,align="center",label="人数")
    plt.title("《Python从入门到实践》星级评价柱状图",loc="center")
    for a,b in zip(x,y):
        plt.text(a,b,b,ha='center',va='center',fontsize=12)
    plt.ylabel("人数")
    plt.xlabel("评价星级")
    plt.legend()
    plt.show()

