FROM python:3.11.2-alpine3.16

RUN apk update && apk upgrade

RUN apk add --no-cache make

RUN apk add git musl-dev go 

RUN apk update && apk add python3-dev gcc libc-dev libffi-dev

# Configure Go
ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN git clone https://github.com/catileptic/androidqf.git
WORKDIR /androidqf
RUN make linux

WORKDIR /

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# TODO mount backup paths, don't copy everything inside the container
COPY ./mvt_companion /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

