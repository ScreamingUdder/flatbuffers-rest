FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get -y update && apt-get -y install --no-install-recommends cmake make gcc g++ git && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/google/flatbuffers.git

RUN cd flatbuffers && mkdir build && cd build && cmake .. && make && make install && cp ./flatc /usr/local/bin

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app