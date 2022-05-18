from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from model.product import Product

app = FastAPI()


@app.post('/product')
def create(product: Product):
    return product.save()

@app.get('/product/{pk}')
def get(pk: str):
    return Product.get(pk)

@app.get('/products')
def all():
    result = []
    for pk in Product.all_pks():
        result.append(Product.get(pk))
    return result

@app.delete('/product/{pk}')
def delete(pk: str):
    product = Product.get(pk)
    return product.delete()


@app.get('/')
def index(): 
    return "Hello World"