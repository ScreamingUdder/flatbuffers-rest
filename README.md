# flatbuffers-rest
flatbuffers to human readable json output with a REST interface.

Also provides a very basic web interface at the root route.

To Clone
--------

Relies on git submodule so clone this repo with
```
git clone --recurse-submodules
```
or run the following after cloning
```
git submodule update --init --recursive
```

To Run
------

Simply run `main.py` for development. Or run `docker-compose up` to build and launch a production server in a docker container.
