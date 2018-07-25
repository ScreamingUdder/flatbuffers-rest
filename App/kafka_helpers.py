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

    for broker_obj in client.brokers.values():
        if broker_obj.host == bytes(broker, 'utf-8'):
            return True
    raise Exception("Broker not found")


def topic_exists(topic_name, broker):
    topic_name = bytes(topic_name, 'utf-8')

    client = KafkaClient(hosts=broker)
    if not (topic_name in client.topics):
        raise Exception("Topic Name not found")


def topic_empty(topic_name, broker):

    client = KafkaClient(hosts=broker)
    topic_obj = client.topics.__getitem__(bytes(topic_name, 'utf-8'))
    if topic_obj.earliest_available_offsets() == topic_obj.latest_available_offsets():
        raise Exception("Topic is empty")


def num_of_messages_int_check(num):
    try:
        return int(num)
    except TypeError as e:
        return error(400, str(e))


def parameter_empty(topic, broker):
    if not topic or not broker:
        raise Exception('One of more of the parameters passed in are empty')


def high_low_offsets(topic_name, broker):
    client = KafkaClient(hosts=broker)
    topic_obj = client.topics.__getitem__(bytes(topic_name, 'utf-8'))
    low_offset = topic_obj.earliest_available_offsets()
    high_offset = topic_obj.latest_available_offsets()
    return low_offset, high_offset


def poll_messages(topic, broker, num):
    parameter_empty(topic, broker)
    num = num_of_messages_int_check(num)
    broker_exists(broker)
    topic_exists(topic, broker)
    topic_empty(topic, broker)
    return broker, topic, num


def check_offsets(topic, broker):
    parameter_empty(topic, broker)
    broker_exists(broker)
    topic_exists(topic, broker)
    topic_empty(topic, broker)
    high_low_offsets(topic, broker)
    low_offset, high_offset = high_low_offsets(topic, broker)
    return broker, topic, low_offset, high_offset
