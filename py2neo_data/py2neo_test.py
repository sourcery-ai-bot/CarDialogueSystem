from py2neo import Graph, Node, Relationship,NodeMatcher




#连接neo4j数据库
def py2neo_connect():
    knowledge_graph = Graph('http://127.0.0.1:7474', username='neo4j', password='123456')
    return knowledge_graph

def nodes_access(knowledge_graph):
    '''测试访问结点函数'''

    # 打印结点直接出编号
    # for node in nodes:
    #     print(node)
    nodes=knowledge_graph.nodes
    models=nodes.match("车型")
    for model in models:
        #直接打印结点中文出现utf-8编码问题
        print(model)
        #字典式访问node中的数据，中文不会乱码
        print(model["name"])

    brands = nodes.match("品牌")
    for brand in brands:
        print(brand)
        print(brand['name'])

    transmissions = nodes.match("变速箱")
    for transmission in transmissions:
        print(transmission)
        print(transmission['name'])

    basic_parameters = nodes.match('基本参数')
    for basic_parameter in basic_parameters:
        print(basic_parameter)
        print(basic_parameter['name'])

    chassis_steerings = nodes.match('底盘转向')
    for chassis_steering in chassis_steerings:
        print(chassis_steering)
        print(chassis_steering['name'])

    cars = nodes.match('车系')
    for car in cars:
        print(car)
        print(car['name'])

    car_sounds = nodes.match('车身')
    for car_sound in car_sounds:
        print(car_sound)
        print(car_sound['name'])

    wheel_brakes = nodes.match('车轮制动')
    for wheel_brake in wheel_brakes:
        print(wheel_brake)
        print(wheel_brake['name'])

def relationships_access(knowledge_graph):
    relationships = knowledge_graph.relationships
    for r in relationships:
        print(r)



def search_car_info(car_type,car_part):
    synonym=['2021款 2.4L汽油手动两驱精英版长厢高底盘','新款汽车','2021款两驱','2021款高底盘','大通2021款新车','今年大通新款汽车','2021新款']
    if car_type in synonym:
        car_type=synonym[0]
    print(car_type)
    print(car_part)
    knowledge_graph = Graph('http://127.0.0.1:7474', username='neo4j', password='123456')
    query_cql="match  (n:车型)-[:配置]->(p:基本参数) where n.name='"+car_type+"' return p."+car_part
    p=knowledge_graph.run(query_cql)
    return str(list(p)[0])

if __name__ == '__main__':
    knowledge_graph=py2neo_connect()
    # nodes=knowledge_graph.nodes
    # a=nodes.match('车型',name='2021款 2.4L汽油手动两驱精英版长厢高底盘')
    # nodematcher= NodeMatcher(knowledge_graph)
    # p=knowledge_graph.run("match  (n:车型)-[:配置]->(p:基本参数) where n.name='2021款 2.4L汽油手动两驱精英版长厢高底盘' return p.上市时间")
    # print(list(p)[0])
    # car_type='2021款 2.4L汽油手动两驱精英版长厢高底盘'
    # car_part='上市时间'
    # query_cql="match  (n:车型)-[:配置]->(p:基本参数) where n.name='"+car_type+"' return p."+car_part
    # p=knowledge_graph.run(query_cql)
    # a=str(list(p)[0])
    # print(a)
    a=search_car_info('2021新款','上市时间')
    print(a)

    # for rel in knowledge_graph.match_one(a,'配置'):
    #     print(rel.end_node()["name"])







