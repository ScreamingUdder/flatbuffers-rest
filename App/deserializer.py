from App.schema_mappings import create_schema_map
from subprocess import run
from os import path

def deserialize_flatbuffers(message_value):
    schema_map = create_schema_map()
    file_identifier = (message_value[4:8])
    file_name = schema_map[file_identifier]
    with open(path.join('.', 'temp'), 'wb')as file:
        file.write(message_value)
    location = path.join('.', 'streaming-data-types', 'schemas', file_name)
    flatc_args = ('flatc --json '+location +' -- temp')
    print(flatc_args)
    run(flatc_args, shell=True)
    with open(path.join('.', 'temp.json',), 'r') as file:
        read_message = file.read()
    read_message = read_message.replace('\n', '')
    return read_message
