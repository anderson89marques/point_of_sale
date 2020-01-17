import uuid


def create_product_data(name='Telefone', description="O telefone azul será o seu novo Smartphone possui tela infinita de 6,4", price=799.90, minimum_stock=0, stock=100):
    return dict(name=name, description=description, price=price, minimum_stock=minimum_stock, stock=stock)


def _create_person_data(name="Lucy Cechtelar", age=31, phone="(11) 98473-7941", email="customer@gmail.com"):
    return dict(name=name, age=age, phone=phone, email=email)

def create_customer_data(**kwargs):
    return _create_person_data(**kwargs)

def create_seller_data(**kwargs):
    identify = kwargs.get('identify', str(uuid.uuid4()))
    if kwargs.get('identify'):
        del kwargs['identify'] 
    return {**_create_person_data(**kwargs), **{'identify': identify}}