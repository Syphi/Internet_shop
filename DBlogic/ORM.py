import sqlalchemy as sa



engine = sa.create_engine("postgresql://postgres:revo1917@localhost/shop")
metadata = sa.MetaData()
db_string = "postgresql://postgres:revo1917@localhost/shop"
db = sa.create_engine(db_string)
connection = db.connect()

order = sa.Table('orders', metadata, autoload=True, autoload_with=engine)
customer = sa.Table('customer', metadata, autoload=True, autoload_with=engine)
product = sa.Table('product', metadata, autoload=True, autoload_with=engine)
category = sa.Table('category', metadata, autoload=True, autoload_with=engine)
order_products = sa.Table('order_products', metadata, autoload=True, autoload_with=engine)
print(repr(order))


# orders = sa.Table('orders', metadata,
#                sa.Column('id', sa.Integer, primary_key=True),
#                sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id')),
#                sa.Column('sum_price', sa.Numeric, nullable=False),
#                sa.Column('delivery_data_time', sa.TIMESTAMP),
#                sa.Column('payment_type', sa.String(4), sa.CheckConstraint('payment_type' in ('cash', 'card')))
#                )

print(repr(order.columns.id))
statment = sa.select([
    customer.c.id,
    customer.c.user_name,
    customer.c.email
])
result = connection.execute(statment).fetchall()
print(result)