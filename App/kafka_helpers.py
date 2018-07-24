from pykafka import KafkaClient, exceptions
from App.errors import error


def broker_exists(broker):
    if ':' not in broker:
        raise Exception("Broker requires port")

    try:
        client = KafkaClient(hosts=broker)
    except exceptions.NoBrokersAvailableError:
        raise Exception("Client not found")

    port = broker.split(':')[1]
    broker = broker.split(':')[0]

    for brokerobj in client.brokers.values():
        # print (broker + " / " + str(brokerobj.host, encoding="utf-8"))
        if brokerobj.host == bytes(broker, 'utf-8'):
            return True
    raise Exception("Broker not found")


def topic_exists(topicname,broker):
    topicname = bytes(topicname, 'utf-8')

    client = KafkaClient(hosts=broker)
    if not (topicname in client.topics):
        raise Exception("Topic Name not found")


def topic_empty(topicname, broker):

    client = KafkaClient(hosts=broker)
    topicobj = client.topics.__getitem__(bytes(topicname, 'utf-8'))
    if topicobj.earliest_available_offsets() == topicobj.latest_available_offsets():
        raise Exception("Topic is empty")


def numofmessagesintcheck(num):
    try:
        return int(num)
    except ValueError as e:
        return (error(400, str(e)))


def poll_messages(topic, broker, num):
    num = numofmessagesintcheck(num)
    broker_exists(broker)
    topic_exists(topic, broker)
    topic_empty(topic,broker)
    return (broker,topic,num)
