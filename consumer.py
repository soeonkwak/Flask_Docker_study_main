import pika  # 이벤트를 보내는데 필요한 패키지

# URL주소는 CloudAMQP에서 계정 생성하고 부여 받은 거.
params = pika.URLParameters('amqps://uuyqugbb:koSGNC-lwhlAm83l-uCIDy5g2SGJ5yBj@dingo.rmq.cloudamqp.com/uuyqugbb')

# rabbitMQ로 연결 생성
connection = pika.BlockingConnection(params)

# channel 생성 -> connection의 channel이랑 동일
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()