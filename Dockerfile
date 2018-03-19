FROM python:3

EXPOSE 8888

RUN apt-get update
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

#RUN VOLUME /work
WORKDIR /work

CMD ["bash"]
