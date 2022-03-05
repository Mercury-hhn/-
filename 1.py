import requests
# 1. 组装请求
url = "http://share.change.tm/api/contest/group/getGroupList?limit=200"  # 这里只有url，字符串格式
# 2. 发送请求，获取响应
res = requests.get(url) # res即返回的响应对象
# 3. 解析响应
print(res.text)  # 输出响应的文本