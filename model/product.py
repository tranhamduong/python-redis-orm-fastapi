import ssl
from redis_om import get_redis_connection, HashModel
import config 

redis = get_redis_connection(
    host=config.redis_host,
    port=config.port,
    password=config.password,
    decode_responses=True,
    ssl=True
)

class Product(HashModel):
    name: str
    price: float
    discount: float
   
    class Meta:
        database = redis