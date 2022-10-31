import json  # 이벤트를 보내는데 필요한 패키지
import pika

# URL주소는 CloudAMQP에서 계정 생성하고 부여 받은 거.
from main import Product, db

params = pika.URLParameters('amqps://uuyqugbb:koSGNC-lwhlAm83l-uCIDy5g2SGJ5yBj@dingo.rmq.cloudamqp.com/uuyqugbb')

# rabbitMQ로 연결 생성
connection = pika.BlockingConnection(params)

# channel 생성 -> connection의 channel이랑 동일
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()