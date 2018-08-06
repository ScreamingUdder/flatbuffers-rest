import os
from os import path


def create_schema_map():
    schemas = os.listdir(path.join('..', '..', 'streaming-data-types', 'schemas'))
    dynamic_schemas = {}
    for files in schemas:
        dynamic_schemas[bytes(files[0:4], 'utf-8')] = files
    return dynamic_schemas
