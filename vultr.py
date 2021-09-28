# coding:utf-8
'''
@File   :   vultr.py
@Time   :   2021/9/28
@Author :   Jarcis
@Link   :   https://github.com/Jarcis-cy/Vultr_API
'''
import requests
import json
import pprint
import argparse

# 获取实例
def get_instance():
    url = 'https://api.vultr.com/v2/instances'
    r = requests.get(url, headers=headers)
    return r.text


# 获取所有区域
def get_all_regions():
    url = 'https://api.vultr.com/v2/regions'
    r = requests.get(url, headers=headers)
    return r.text


# 获取所有计划
def get_all_plans():
    url = 'https://api.vultr.com/v2/plans'
    r = requests.get(url, headers=headers)
    return r.text


# 获取所有操作系统
def get_all_os():
    url = 'https://api.vultr.com/v2/os'
    r = requests.get(url, headers=headers)
    return r.text

# 创建实例
def create_instance(country, plan, label, os_id, hostname, tag):
    data = {
        "region": country,
        "plan": plan,
        "label": label,
        "os_id": os_id,
        "user_data": "QmFzZTY0IEV4YW1wbGUgRGF0YQ==",
        "backups": "disabled",
        "hostname": hostname,
        "tag": tag
    }
    url = 'https://api.vultr.com/v2/instances'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.text


# 删除实例
def delete_instance(instances_id):
    url = 'https://api.vultr.com/v2/instances/'
    instances = instances_id
    r = requests.delete(url+instances_id, headers=headers)
    return r.text

parser = argparse.ArgumentParser(description='Create and delete servers',formatter_class = argparse.RawDescriptionHelpFormatter)
hit = '\n---------------------------------------------\n创建时需要填写的参数列表：\n国家：\n\n    洛杉矶（美国）     lax\n    东京（日本）          nrt\n    新加坡（新加坡）        sgp\n    首尔（韩国）          icn\n    阿姆斯特丹（荷兰）   ams\n    亚特兰大（美国）        atl\n    巴黎（法国）          cdg\n    达拉斯（美国）         dfw\n    新泽西（美国）         ewr\n    法兰克福（德国）        fra\n    伦敦（英国）          lhr\n    迈阿密（美国）         mia\n    芝加哥（美国）         ord\n    西雅图（美国）         sea\n    硅谷（美国）          sjc\n    斯德哥尔摩（瑞典）   sto\n    悉尼（澳大利亚）        syd\n    多伦多（加拿大）        yto\n\n服务器版本：\n\n    ubuntu 18           270\n    ubuntu 20           387\n    ubuntu 21           445\n\n套餐：\n\n    5美元                 vc2-1c-1gb\n    10美元                vc2-1c-2gb\n---------------------------------------------\n请每次选择一个模式\n例：python vultr.py --create -c sto -l jarcis\n---------------------------------------------\n'
parser.description = hit
parser.add_argument('--create', action="store_true", help='输入该参数进入创建模式，默认为False')
parser.add_argument('--delete', action="store_true", help='输入该参数进入删除模式，默认为False，请添加-i参数')
parser.add_argument('--view', action="store_true", help='输入该参数进入查看模式，默认为False')
parser.add_argument('-c', type=str, default='lax', help='请输入你想创建的服务器的所属地区，默认建立在洛杉矶')
parser.add_argument('-p', type=str, default='vc2-1c-1gb', help='选择建立的组合金额，分为5美金与10美金每月，默认5美金')
parser.add_argument('-l', type=str, default='default', help='请输入你想创建的服务器名称，默认为default')
parser.add_argument('-o', type=int, default=387, help='请输入你想创建的服务器系统，默认为ubuntu 20')
parser.add_argument('--hostname', type=str, default='test', help='请输入你想创建的服务器主机名，默认为test')
parser.add_argument('-t', type=str, default='test', help='请输入你想创建的服务器标签，默认为test')
parser.add_argument('-i', type=str, default='', help='请输入你想删除的服务器id')
args = parser.parse_args()

# 修改api_key, 将api_key替换成vultr中的api
headers = {
        'Authorization': 'Bearer ' + 'api_key',
        'Content-Type': 'application/json'
    }

if args.create and args.delete and view:
    print("请选择一个模式")
elif args.create:
    data = json.loads(create_instance(args.c,args.p,args.l,args.o,args.hostname,args.t))
    print("服务器创建成功！")
    print("Server_ID : " + data['instance']['id'])
    print("Server_OS : " + data['instance']['os'])
    print("Server_PLAN : " + data['instance']['plan'])
    print("Server_ADDRESS : " + data['instance']['region'])
    print("Server_STATUS : " + data['instance']['status'])
    print("服务器默认账户：root")
    print("服务器默认密码：" + data['instance']['default_password'])
    print("服务器IP请在创建一分钟后，使用查看模式获取")
elif args.delete:
    if args.i == '':
        print('请输入你想删除的服务器id')
    else:
        data = delete_instance(args.i)
        if len(data) != 0:
            print("该id不存在，删除失败！")
        else :
            print("删除成功！")
elif args.view:
    data = json.loads(get_instance())
    print("您一共有{}个服务器,分别是：\n".format(len(data['instances'])))
    print("-----------------------------------------------------")
    for i in range(len(data['instances'])):
        print("Server_IP : " + data['instances'][i]['main_ip'])
        print("Server_create_time : " + data['instances'][i]['date_created'])
        print("Server_ID : " + data['instances'][i]['id'])
        print("Server_OS : " + data['instances'][i]['os'])
        print("Server_PLAN : " + data['instances'][i]['plan'])
        print("Server_ADDRESS : " + data['instances'][i]['region'])
        print("Server_STATUS : " + data['instances'][i]['status'])
        print("-----------------------------------------------------")
else:
    print("请选择一个模式")
