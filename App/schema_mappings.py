import os
from os import path


def create_schema_map():
    schemas = os.listdir(path.join('..', 'streaming-data-types', 'schemas'))
    dynamic_schemas = {}
    print(schemas)
    for files in schemas:
        print('b\''+(files[0:4]))

        dynamic_schemas[bytes(files[0:4], 'utf-8')] = files
    print(dynamic_schemas)
    return dynamic_schemas
