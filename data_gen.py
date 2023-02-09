import random
import string
import names
import datetime
import faker
import uuid


fake = faker.Faker()
ids = {
    'employee_id': [],
    'customer_id': [],
    'seller_id': [],
    'product_id': [],
    'category_id': [],
    'review_id': [],
    'brand_id': [],
    'cart_id': [],
    'wishlist_id': [],
    'order_id': [],
    'courier_id': [],
    'customer_transaction_id': []
    
}
def generate_employee():
    employee_id = uuid.uuid4()
    ids['employee_id'].append(employee_id)
    employee_first_name = names.get_first_name()
    employee_middle_name = names.get_first_name() if random.randint(0,2) else ' '
    employee_last_name = names.get_last_name()
    employee_email = fake.email()
    employee_login_password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    employee_mobile_number = fake.phone_number()
    employee_date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)
    employee_gender = random.choice(['Male', 'Female', 'Other'])
    employee_house_number = random.randint(1, 500)
    employee_locality = fake.street_name()
    employee_city = fake.city()
    employee_state = fake.state()
    employee_country = fake.country()
    employee_pincode = fake.zipcode()
    employee_employee_role = fake.job()
    employee_date_of_hiring = fake.date_this_decade(before_today=True, after_today=False)
    employee_pan = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    employee_blood_group = random.choice(['A+', 'B+', 'O+', 'AB+', 'A-', 'B-', 'O-', 'AB-'])
    employee_emergency_contact_number = fake.phone_number()
    employee_emergency_contact_name = names.get_full_name()
    employee_salary = random.randint(50000, 200000)
    return (employee_id,employee_first_name, employee_middle_name, employee_last_name, employee_email, employee_login_password,employee_mobile_number,employee_date_of_birth,employee_gender,employee_house_number,employee_locality,employee_city,employee_state,employee_country,employee_pincode,employee_employee_role,employee_date_of_hiring,employee_pan,employee_blood_group,employee_emergency_contact_number,employee_emergency_contact_name,employee_salary)
    



def generate_customer():
    customer_id = uuid.uuid4()
    ids['customer_id'].append(customer_id)
    fake = faker.Faker()
    first_name = names.get_first_name()
    middle_name = names.get_first_name() if random.randint(0,2) else ' '
    last_name = names.get_last_name()
    email = fake.email()
    login_password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    mobile_number = fake.phone_number()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)
    gender = random.choice(['Male', 'Female', 'Other'])
    house_number = random.randint(1, 500)
    locality = fake.street_name()
    city = fake.city()
    state = fake.state()
    country = fake.country()
    pincode = fake.zipcode()

    return (customer_id, first_name, middle_name, last_name, email, login_password, mobile_number, date_of_birth,gender, house_number, locality, city, state, country, pincode)



def generate_seller():
    seller_id = uuid.uuid4()
    ids['seller_id'].append(seller_id)
    fake = faker.Faker()
    first_name = names.get_first_name()
    middle_name = names.get_first_name() if random.randint(0,2) else ' '
    last_name = names.get_last_name()
    email = fake.email()
    login_password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    mobile_number = fake.phone_number()
    company_name = fake.company()
    property_number = random.randint(1, 500)
    locality = fake.street_name()
    city = fake.city()
    state = fake.state()
    country = fake.country()
    pincode = fake.zipcode()
    return (seller_id, first_name, middle_name, last_name, email, login_password, mobile_number, company_name, property_number, locality, city, state, country, pincode)


def generate_random_category():
    category_id = uuid.uuid4()
    ids['category_id'].append(category_id)
    category_name = fake.word()
    category_description = fake.text()
    return (category_id, category_name, category_description)

def generate_random_brand():
    brand_id = uuid.uuid4()
    ids['brand_id'].append(brand_id)
    brand_name = fake.word()
    brand_description = fake.text()
    
    brand_logo = fake.image_url()
    founder = fake.name()
    country_of_origin = fake.country()
    return (brand_id, brand_name, brand_description,brand_logo, founder, country_of_origin)

def generate_random_product():
    product_id = uuid.uuid4()
    ids['product_id'].append(product_id)
    product_name = fake.word()
    product_description = fake.text()
    product_price = round(random.uniform(100, 100000), 2)
    product_quantity = random.randint(1, 100)
    product_images = [fake.image_url() for _ in range(3)]
    product_ingredients = [fake.word() for _ in range(5)]
    brand_id = random.choice(ids['brand_id'])
    category_id = random.choice(ids['category_id'])
    seller_id = random.choice(ids['seller_id'])
    return (product_id, product_name, product_description, product_price, product_quantity, product_images, product_ingredients,brand_id, category_id, seller_id)


def generate_random_review():
    review_id = uuid.uuid4()
    ids['review_id'].append(review_id)
    review_rating = random.randint(1, 6)
    review_title = fake.word()
    comments = fake.text()
    review_date = fake.date()
    product_id = random.choice(ids['product_id'])
    customer_id = random.choice(ids['customer_id'])
    return (review_id, review_rating, review_title, comments, review_date, product_id, customer_id)


def generate_random_cart():
    cart_id = uuid.uuid4()
    ids['cart_id'].append(cart_id)
    quantity = random.randint(1, 10)
    discount = random.randint(1, 70)/100
    product_id = random.choice(ids['product_id'])
    customer_id = random.choice(ids['customer_id'])
    return (cart_id, quantity, discount, product_id, customer_id)
    
    
def generate_random_wishlist():
    wishlist_id = uuid.uuid4()
    ids['wishlist_id'].append(wishlist_id)
    product_id = random.choice(ids['product_id'])
    customer_id = random.choice(ids['customer_id'])
    return (wishlist_id, product_id, customer_id)

def generate_random_order():
    order_id = uuid.uuid4()
    ids['order_id'].append(order_id)
    order_date = fake.date()
    amount = round(random.uniform(100, 100000), 2)
    order_status = random.choice([ 'Delivered', 'Under Process'])
    delivery_date = fake.date()
    delivery_fee = round(random.uniform(10, 500), 2)
    customer_id = random.choice(ids['customer_id'])
    return (order_id, order_date,amount, order_status, delivery_date, delivery_fee, customer_id)

def generate_random_courier():
    courier_id = uuid.uuid4()
    ids['courier_id'].append(courier_id)
    courier_name = fake.word()
    tracking_url = fake.url()
    order_id = random.choice(ids['order_id'])
    return (courier_id, courier_name, tracking_url, order_id)

def generate_random_transaction():
    transaction_id = uuid.uuid4()
    ids['customer_transaction_id'].append(transaction_id)
    amount = round(random.uniform(100, 100000), 2)
    transaction_status = random.choice([ 'Successful', 'Failed','Pending'])
    payment_method = random.choice(['Credit/Debit Card', 'Netbanking', 'UPI', 'Cash On Delivery', 'Pay Later'])
    order_id = random.choice(ids['order_id'])
    ids["order_id"].remove(order_id)
    return (transaction_id, amount, transaction_status, payment_method, order_id)


def generate_data():
    num = {
    'employee': (100,generate_employee),
    'customer': (100,generate_customer),
    'seller': (100,generate_seller),
    'category': (100,generate_random_category),
    'brand': (100,generate_random_brand),
    'product': (100,generate_random_product),
    'review': (1000,generate_random_review),
    'cart': (100,generate_random_cart),
    'wishlist': (100,generate_random_wishlist),
    'orders': (100,generate_random_order),
    'courier': (100,generate_random_courier),
    'transaction': (100,generate_random_transaction)
    }
    with open('data.csv', 'w') as f:
        for k,v in num.items():
            rep, func = v
            f.write(k + '\n')
            for _ in range(rep):
                res = func()
                f.write('('+','.join(str(x) for x in res)+'),\n')
            f.write('\n')

generate_data()