import csv
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
book_list=[]
for i in range(0,100):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12842874&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&fold=1'

    res = requests.get(url, headers=headers)

    jd = json.loads(res.text.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))

    com_list = jd['comments']
    for i in com_list:
        comment=i['content']
        creationTime=i['creationTime']
        score=i['score']
        book_name=i['productColor']
        dic={
            '书籍名称':book_name,
            '评论内容':comment,
            '评分星级':score,
            '评论时间':creationTime
        }
        book_list.append(dic)
# for i in range(len(book_list)):
#     print(book_list[i])
with open('book.csv','w',encoding='utf-8',newline='')as f:
    w = csv.DictWriter(f,book_list[0].keys())
    w.writeheader()
    w.writerows(book_list)
f.close()
