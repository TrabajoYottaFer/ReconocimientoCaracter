FROM ubuntu
LABEL maintainer="Ronnie Velasquez ronnieitor@gmail.com"
ENV HOME /home

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev
RUN pip3 install pillow
RUN pip3 install pytesseract
RUN pip3 install Flask
RUN pip3 install Flask-restful
RUN pip3 install Flask_cors
COPY ReconocimientoCaracterIA.py /home/ReconocimientoCaracter/ReconocimientoCaracterIA.py

EXPOSE 5000
CMD [ "python3", "/home/ReconocimientoCaracter/ReconocimientoCaracterIA.py" ]
#RUN python3 /home/ReconocimientoCaracter/ReconocimientoCaracterIA.py


