from App.schema_mappings import schema_map
from subprocess import run


def deserialize_flatbuffers(message_value):
    file_identifier = (message_value[4:8])
    file_name = schema_map[file_identifier]
    with open('./temp', 'wb')as file:
        file.write(message_value)
    flatc_args = ('flatc --json .\schemas\\'+file_name + ' -- temp')
    print(flatc_args)
    run(flatc_args, shell=True)
    with open('./temp.json', 'r') as file:
        read_message = file.read()
    return read_message
