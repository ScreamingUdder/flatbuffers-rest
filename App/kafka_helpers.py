from pykafka import KafkaClient, exceptions


def broker_exists(broker):
    if ':' not in broker:
        print("broker requires port")
        return False

    try:
        client = KafkaClient(hosts=broker)
    except exceptions.NoBrokersAvailableError:
        print('Client not setup')
        return False

    port = broker.split(':')[1]
    broker = broker.split(':')[0]

    for brokerobj in client.brokers.values():
        # print (broker + " / " + str(brokerobj.host, encoding="utf-8"))
        if brokerobj.host == bytes(broker, 'utf-8'):
            # if not port or port == brokerobj.port:
            #     return False
            print("broker found")
            return True
    print("Broker not found")
    return False


def topic_exists(topicname,broker):
    topicname =bytes(topicname, 'utf-8')

    client = KafkaClient(hosts=broker)

    return (topicname in client.topics)

# broker = 'hinata:9092'
#
# client = KafkaClient(hosts=broker)
# print(client.brokers[1].host)