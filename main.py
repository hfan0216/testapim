import json
import requests
import time


# GET 请求
def data_get(product_id):
    # 以字典形式编辑查询参数
    parameters = {'Productid': product_id}

    # 发送 GET 请求，返回一个包含服务器响应信息的 response 对象
    response = requests.get(url=url, params=parameters)
　　# 发送 POST 请求，返回一个包含服务器响应信息的 response 对象，data以json格式传参
 
    print(response)
    # HTTP 响应状态码为 200 表示请求成功，服务器成功处理了请求
    if response.status_code == 200:
        # 获取字典中的Data值
        print("ok")
    else:
        # HTTP 响应状态码不为 200 时，提示“URL未正常响应请求”
        raise Exception('URL未正常响应请求')
    return value

#GET https://apim-northwindshoes123.azure-api.net/northwindshoes01/api/Products/1 HTTP/1.1

#data = data_get(product_id=1, url='http://域名+接口地址')
while True:
    response = requests.get('https://apim-northwindshoes123.azure-api.net/northwindshoes01/api/Products/1')
    print(response)
    # HTTP 响应状态码为 200 表示请求成功，服务器成功处理了请求
    if response.status_code == 200:
        # 获取字典中的Data值
        print("ok")
    else:
        # HTTP 响应状态码不为 200 时，提示“URL未正常响应请求”
        raise Exception('URL未正常响应请求')
    time.sleep(5)
