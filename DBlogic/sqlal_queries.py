import sqlalchemy as sa



class DbSqlalQueries():

    def __init__(self):
        try:
            self.db_string = "postgresql://postgres:revo1917@localhost/shop"
            self.db = sa.create_engine(self.db_string)
            self.connection = self.db.connect()
            self.metadata = sa.MetaData()
            self.orders = sa.Table('orders', self.metadata, autoload=True, autoload_with=self.db)
            self.customer = sa.Table('customer', self.metadata, autoload=True, autoload_with=self.db)
            self.product = sa.Table('product', self.metadata, autoload=True, autoload_with=self.db)
            self.category = sa.Table('category', self.metadata, autoload=True, autoload_with=self.db)
            self.order_products = sa.Table('order_products', self.metadata, autoload=True, autoload_with=self.db)
            print('Init class and connection')
        except Exception as e:
            print('shit - no such db')
            print(e)

    def __del__(self):
        self.connection.close()
        print('Close class and connection')

    def add_category(self, cat_name, image_pass, description, slug, parent_id):
        insert = sa.insert(self.category)
        insert = insert.values({'cat_name': str(cat_name), 'image': str(image_pass), 'description': str(description),
                                'slug': str(slug), 'parent_id': parent_id})
        self.connection.execute(insert)

    def add_product(self, category_id, prod_name, image, description, slug, price_ua, in_stock, other_info):
        insert = sa.insert(self.product)
        insert = insert.values({'category_id': category_id, 'prod_name': str(prod_name), 'image': str(image),
                               'description': str(description), 'slug': str(slug), 'price_ua': price_ua,
                               'in_stock': in_stock, 'other_info': other_info})
        self.connection.execute(insert)

    def add_customer(self, user_name, email, password, phone, shipping_address):
        insert = sa.insert(self.customer)
        insert = insert.values({'user_name': str(user_name), 'email': str(email), 'password': str(password),
                                'phone': phone, 'shipping_address': shipping_address})
        self.connection.execute(insert)

    def add_orders(self, customer_id, sum_price, delivery_data_time, payment_type, dict):
        # add to orders table
        insert = sa.insert(self.orders)
        insert = insert.values({'customer_id': customer_id, 'sum_price': sum_price,
                                'delivery_data_time': delivery_data_time, 'payment_type': payment_type})
        self.connection.execute(insert)

        # select last id in orders table
        select = self.orders.select()
        select = select.where(sa.and_(self.orders.c.customer_id == customer_id,
                                      self.orders.c.sum_price == sum_price,
                                      # self.orders.c.delivery_date_time == delivery_data_time, //how to
                                      self.orders.c.payment_type == payment_type))
        result_id = self.connection.execute(select).fetchall()
        result_id = result_id[-1][0]

        print(result_id)
        print(dict)

        # add to orders_product name
        insert = self.order_products.insert()
        insert_list = []
        for key, value in dict.items():
            print(result_id, key, value)
            new_row = {'orders_id': result_id, 'product_id': key, 'number_prod': value}
            insert_list.append(new_row)

        print(insert_list)
        self.connection.execute(insert, insert_list)


    def get_category(self):
        select = self.category.select()
        result = self.connection.execute(select).fetchall()
        print(result)
        return result

    def get_subcategories(self, category_id):
        join = self.category.join(self.category,
                                  category_id == self.category.c.parent_id)
        result = sa.select([self.category]).select_from(join)
        print(result.fetchall())
        return result

    def products_for_category(self, category_id):
        select = self.product.select()
        select = select.where(self.product.c.category_id == category_id)
        return self.connection.execute(select).fetchall()

    def orders_for_customer(self):
        pass

    def get_customer_from_login_and_password(self, login, password):
        select = self.customer.select().\
            where(self.customer.c.user_name == sa.bindparam('login')).\
            where(self.customer.c.password == sa.bindparam('password'))
        return print(self.connection.execute(select, login=login, password=password).fetchall())

test = DbSqlalQueries()
# test.add_category('name2', '//pass2//', '2description2', 'slug2', 1)
# test.add_product(category_id=1, prod_name='phone2', image='//pass//', description='description', slug='//slug//2',
#                  price_ua=100, in_stock=25, other_info={})
# test.add_customer(user_name='Denis2', email='2ralko2@gmail.com', password='2qwerty2',
#                   phone='0671663238', shipping_address='Kovalski2')
# test.add_orders(customer_id=1, sum_price=20, delivery_data_time='2017-12-19 10:23:54',
#                 payment_type='card', dict={1: 2})
# test.get_category()
# test.products_for_category(1)


test.add_orders(customer_id=1, sum_price=20, delivery_data_time='2004-10-19 10:23:54+02',
                payment_type='card', dict={1: 2, 5: 10})


# try:
#     test.get_customer_from_login_and_password('Denis', 'ralko@gmail.com')
# except Exception as e:
#     print(e)