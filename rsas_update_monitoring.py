import os
import json
data = {
    'RSAS 6.0 系统':{'url': 'http://update.nsfocus.com/update/listRsasDetail/v/rsassys', 'version': '', 'uptime': ''},
    'RSAS 6.0 系统插件':{'url': 'http://update.nsfocus.com/update/listRsasDetail/v/vulsys', 'version': '', 'uptime': ''},
    'RSAS 6.0 Web插件':{'url': 'http://update.nsfocus.com/update/listRsasDetail/v/vulweb', 'version': '', 'uptime': ''},
    }
# 读取历史
data_file = 'data.json'
if os.path.exists(data_file):
    try:
        data = json.loads(open(data_file,'r',encoding='utf8').read())
    except:
        with open(data_file, 'w',encoding='utf-8') as f:
            json.dump(data, f,ensure_ascii=False,indent = 4)
else:
    with open(data_file, 'w',encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False,indent = 4)
# 更新README.md
with open("README.md",'w',encoding='utf8') as fd:
    fd.write('### 绿盟远程安全评估系统更新情况\n\n')
    fd.write('| 类型 | 版本 | 更新时间 |\n')
    fd.write('| :----:| :----: | :----: |\n')
    for name in data:
        fd.write('| {} | {} | {} |\n'.format(name,data[name].get('version',''),data[name].get('uptime','')))

# 写入历史
with open(data_file, 'w',encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False,indent = 4)