def num_of_messages_int_check(num):
    try:
        return int(num)
    except ValueError:
        raise Exception("Number of messages cannot be converted into an int")


def parameter_empty(topic, broker):
    if not topic or not broker:
        raise Exception('One of more of the parameters passed in are empty')


def default_port(broker):
    if ':' not in broker:
        return broker + ":9092"
    return broker
