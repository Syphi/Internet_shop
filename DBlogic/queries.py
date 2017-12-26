import sqlalchemy as sqlal


def conection_disconection(f):
    def wrapper(db, *args, **kwargs):
        db_string = "postgresql://postgres:revo1917@localhost/shop"
        try:
            db = sqlal.create_engine(db_string)
        except Exception as e:
            print(e)

        gen = f(db, *args, **kwargs)
        db.close()

        return gen

    return wrapper


class DBqueries():

    def __init__(self):
        try:
            self.db_string = "postgresql://postgres:revo1917@localhost/shop"
            self.db = sqlal.create_engine(self.db_string)
            self.connection = self.db.connect()
            print('Init class and connection')
        except Exception as e:
            print('shit - no such db')
            print(e)

    def __del__(self):
        self.connection.close()
        print('Close class and connection')

    def select_all_from_table(self):
        pass

    def add_category(self, cat_name, image_pass, description, slug, parent_id):

        raw_sql = '''INSERT INTO category (cat_name, image, description, slug, parent_id)
                     VALUES 
                     ('{}', '{}', '{}', '{}', '{}');'''.format(cat_name, image_pass, description, slug, parent_id)
        print(raw_sql)
        self.connection.execute(raw_sql)

    def add_product(self, category_id, prod_name, image, description, slug, price_ua, in_stock, other_info):

        raw_sql = '''   INSERT INTO product (category_id, prod_name, image, description, slug, price_ua, in_stock, other_info)
                    VALUES 
                          ({}, '{}', '{}', '{}', '{}', {}, {}, '{}');'''.\
                    format(category_id, prod_name, image, description, slug, price_ua, in_stock, other_info)
        self.connection.execute(raw_sql)

    def add_customer(self, user_name, email, password, phone, shipping_address):

        raw_sql = '''   INSERT INTO customer (user_name, email, password, phone, shipping_address)
                    VALUES 
                          ('{}', '{}', '{}', '{}', '{}');'''.\
                    format(user_name, email, password, phone, shipping_address)
        self.connection.execute(raw_sql)

    def add_orders(self, customer_id, sum_price, delivery_data_time, payment_type, dict):
        print(1)
        raw_sql = '''   INSERT INTO orders(customer_id, sum_price, delivery_data_time, payment_type) 
                    VALUES
                    ({}, {}, '{}'::timestamp, '{}');'''.format(customer_id, sum_price, delivery_data_time, payment_type)

        print(raw_sql)
        self.connection.execute(raw_sql)
        print(2)

        raw_sql = ''' SELECT id FROM orders 
                      WHERE customer_id = {} AND sum_price = {} 
                      AND  delivery_data_time = '{}' AND payment_type = '{}';
                       '''.format(customer_id, sum_price, delivery_data_time, payment_type)

        order_id = self.connection.execute(raw_sql)
        print(order_id)
        print(3)

        for key, value in dict.items():
            print(4)
            raw_sql = '''   INSERT INTO order_products(orders_id, product_id, number_prod) 
                          VALUES ('{}', '{}', '{}');'''.format(order_id, key, value)

    def get_category(self):
        raw_sql = '''SELECT cat_name FROM category'''
        result_set = self.connection.execute(raw_sql)
        return list(result_set)

    def get_subcategories(self):
        pass

    def products_for_category(self):
        pass

    def orders_for_customer(self):
        pass

    def get_customer_from_login_and_password(self):
        pass

db = DBqueries()
db.get_category()
# db.add_category('name', '//pass//', 'description', 'slug', 1)

# db.add_product(category_id=1, prod_name='phone2', image='//pass//', description='description', slug='//slug//2',
#                price_ua=100, in_stock=25, other_info={})

# db.add_customer(user_name='Denis', email='ralko@gmail.com', password='qwerty',
#                phone='0671773238', shipping_address='Kovalski 5')
db.add_orders(customer_id=1, sum_price=20, delivery_data_time='2017-12-19 10:23:54', payment_type='card', dict={1: 2})