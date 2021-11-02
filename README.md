# Vultr_API
----
### 脚本介绍
使用者可通过该脚本实现实时创建、查看、删除vultr上的服务器，脚本中的填写参数示例只提供部分参数，想要看详细参数，可自行修改代码，通过调用代码中的`get_all_regions()`、`get_all_plans()`、`get_all_os()`获得更多的信息。
**注意修改脚本中的api_key**
- 如果报错，请查看是否是自己当前的邮箱帐号还无法创建vps。
- 该脚本不需要翻墙
### Help
##### 参数列表
国家：

    洛杉矶（美国）     lax
    东京（日本）          nrt
    新加坡（新加坡）        sgp
    首尔（韩国）          icn
    阿姆斯特丹（荷兰）   ams
    亚特兰大（美国）        atl
    巴黎（法国）          cdg
    达拉斯（美国）         dfw
    新泽西（美国）         ewr
    法兰克福（德国）        fra
    伦敦（英国）          lhr
    迈阿密（美国）         mia
    芝加哥（美国）         ord
    西雅图（美国）         sea
    硅谷（美国）          sjc
    斯德哥尔摩（瑞典）   sto
    悉尼（澳大利亚）        syd
    多伦多（加拿大）        yto

服务器版本：

    ubuntu 18           270
    ubuntu 20           387
    ubuntu 21           445

套餐：

    5美元                 vc2-1c-1gb
    10美元                vc2-1c-2gb
##### 参数详解
```
optional arguments:
  -h, --help           show this help message and exit
  --create             输入该参数进入创建模式
  --delete             输入该参数进入删除模式，请添加-i参数
  --view               输入该参数进入查看模式
  -c C                 请输入你想创建的服务器的所属地区，默认建立在洛杉矶
  -p P                 选择建立的组合金额，分为5美金与10美金每月，默认5美金
  -l L                 请输入你想创建的服务器名称，默认为default
  -o O                 请输入你想创建的服务器系统，默认为ubuntu 20
  --hostname HOSTNAME  请输入你想创建的服务器主机名，默认为test
  -t T                 请输入你想创建的服务器标签，默认为test
  -i I                 请输入你想删除的服务器id
```
- `--create`、`--delete`、`--view`这三个参数只能选择一个，也必须选择一个。
### 例子
python vultr.py --create -c sto -l jarcis
