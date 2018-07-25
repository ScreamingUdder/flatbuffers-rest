from pykafka import KafkaClient, exceptions, common
from App.errors import error


def broker_exists(broker):
    if ':' not in broker:
        raise Exception("Broker requires port")

    try:
        client = KafkaClient(hosts=broker)
    except exceptions.NoBrokersAvailableError:
        raise Exception("Broker not found")

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
    topic_obj = client.topics[(bytes(topic_name, 'utf-8'))]
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

    topic_obj = find_topic(broker, topic_name)

    low_offset = {}
    earliest_offsets = topic_obj.earliest_available_offsets()

    high_offset = {}

    for i in range(len(earliest_offsets)):
        if earliest_offsets[i].err != 0:
            raise Exception("Failed to query offset")
        low_offset['partition ' + str(i)] = earliest_offsets[i].offset[0]

    latest_offsets = topic_obj.latest_available_offsets()

    for i in range(len(latest_offsets)):
        if latest_offsets[i].err != 0:
            raise Exception("Failed to query offset")
        high_offset['partition ' + str(i)] = latest_offsets[i].offset[0]
    return {'low offsets': low_offset, 'high offsets': high_offset}


def find_topic(broker, topic_name):
    client = KafkaClient(hosts=broker)
    topic_obj = client.topics[bytes(topic_name, 'utf-8')]
    return topic_obj


def get_last_messages(topic, broker, num):
    print("start")
    messages = dict()
    topic_obj = find_topic(broker, topic)

    consumer = topic_obj.get_simple_consumer(auto_offset_reset=common.OffsetType.LATEST, reset_offset_on_start=True)
    if num > 0:
        offsets = [(p, op.next_offset - num -2) for p, op in consumer._partitions.items()]# -2 is to fix a problem with it giving 2 less than the user requests
        consumer.reset_offsets(offsets)
    message_num = 1
    if not consumer.consume():
        raise Exception("Failed to consumer from topic: {}".format(topic))
    if consumer:
        print("iterating")
        for message in consumer:
            print(message)
            messages["message num: {}".format(message_num)] = message
    print("Finished iteration")
    return messages


def poll_messages(topic, broker, num):
    parameter_empty(topic, broker)
    num = num_of_messages_int_check(num)
    broker_exists(broker)
    topic_exists(topic, broker)
    topic_empty(topic, broker)
    return get_last_messages(topic, broker, num)


def check_offsets(topic, broker):
    parameter_empty(topic, broker)
    broker_exists(broker)
    topic_exists(topic, broker)
    topic_empty(topic, broker)
    return high_low_offsets(topic, broker)
