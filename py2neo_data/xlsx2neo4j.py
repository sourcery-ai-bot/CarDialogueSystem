# coding:utf-8
from py2neo import Graph, Node, Relationship
import pandas as pd

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='123456')

data = pd.read_excel('test3.xlsx',index_col=0)

for index in data.index:
    content = data.loc[index].dropna()
    # print(content)

    #### 创建车系节点 ##########################################################
    car_series_node = graph.nodes.match('车系',name=content['车系1']).first()
    if car_series_node == None:
        car_series_node = Node('车系', name=content['车系1'])
        graph.create(car_series_node)
    ##############################################################
    #### 创建车型节点 ###########################################
    car_model_node = Node('车型', name=content['车型'])
    graph.create(car_model_node)
    ###############################################
    #### 创建车系车型边######################################
    r1 = Relationship(car_model_node, '属于', car_series_node)
    graph.create(r1)
    #######################################################

    #### 读取车型基本参数 ###################################################
    car_model_basicConfig = dict()
    basicConfig_list = ['厂商','级别','能源类型','环保标准',
                        '上市时间','最大功率(kW)','最大扭矩(N·m)',
                        '发动机','变速箱','长*宽*高(mm)','车身结构','最高车速(km/h)',
                        '官方0-100km/h加速(s)','实测0-100km/h加速(s)',
                        '实测100-0km/h制动(m)','实测油耗(L/100km)',
                        '工信部综合油耗(L/100km)','整车保修']
    for li in basicConfig_list:
        try:
            if content[li] != '-':
                car_model_basicConfig[li] = content[li]
            else:
                print('for li in basicConfig_list ----------- content[li] != "-"')
        except:
            print('for li in basicConfig_list 报错')
    #### 创建基本参数节点 ###################################################
    cmb_node = Node('车型基本参数',name=content['车型'],**car_model_basicConfig)
    graph.create(cmb_node)
    #######################################################
    #### 创建车型与基本参数的边 ###################################################
    r2 = Relationship(car_model_node,'基本参数',cmb_node)
    graph.create(r2)
    #######################################################
    #### 读取其他参数###################################################
    car_model_otherConfig = dict()
    car_model_otherConfig_list = ['底盘转向', '车轮制动']
    for li in car_model_otherConfig_list:
        try:
            if content[li] != '-':
                car_model_otherConfig[li] = content[li]
            else:
                print('for li in other_config_list --------- content[li] != "-"')
        except:
            print('for li in other_config_list 报错')
    #######################################################
    ####创建其他参数节点###################################################
    if car_model_otherConfig != {}:
        cmo_node = Node('车型其他参数',name=content['车型'],**car_model_otherConfig)
        graph.create(cmo_node)
        ####创建车型与其他参数节点的边###################################################
        r3 = Relationship(car_model_node,'基本参数',cmo_node)
        graph.create(r3)
    #######################################################

    # break



