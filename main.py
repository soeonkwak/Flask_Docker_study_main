from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
# db연결 정보 (mysql://id:pw@host값/table명) -> 이렇게 적으면 docker-compose.yml 파일의 db 랑 연결 할 수 있음.
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False) # Product는 여기서 생성하는 게 아니니까 autoincrement=false
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product') #user_id와 product_id 조합이 유니크하도록(중복되지 않도록)


@app.route('/')
def index():  # 함수 생성
    return 'Hello'


if __name__ == '__main__':  # 조건
    app.run(debug=True, host='0.0.0.0')