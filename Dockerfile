#docker compose up ! 한 후에 도커가 할 일을 지정 -> 이미지가 올라간 후 할 일을 예약해놓는 것
FROM python:3.9
ENV PYTHONNUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
#모든 파일을 도커의 앱으로 copy하겠다.
COPY . /app