import pandas as pd

# 为了获取到每天的评论数，对评论时间进行清洗，仅需要年月日，不需要精确到具体时间
datafile = './book2.csv'
data = pd.read_csv(datafile,encoding = 'gb18030')
csv_df = pd.DataFrame(data)
replaces = csv_df['评论时间'].astype(str)
# print(replaces)
for i in range(0, len(replaces)):
    replaces[i]=replaces[i].split(' ')[0]
csv_df['评论时间'] = replaces
csv_df.to_csv('clear.csv', index=None, encoding='utf-8-sig')

# 对爬取的数据一小部分存在空值，对缺失值进行清洗：
datafile = './clear.csv'  # 文件所在位置
data = pd.read_csv(datafile, encoding='utf-8')
print("显示缺失值，缺失则显示为TRUE：\n", data.isnull())
print("\n显示每一列中有多少个缺失值：\n", data.isnull().sum())
data = data.dropna(axis=0, how='any')
data.to_csv('clear1.csv', encoding='utf-8')
