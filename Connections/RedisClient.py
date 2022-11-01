import os
import redis
import Singleton

"""
    Connect redis singleton
    
    #use 
    from RedisClient import RedisClient
    client = RedisClient()
    

"""

class RedisClient(metaclass=Singleton):
    def __int__(self):
        if os.environ.get('APP_ENV') == 'product':
            redis_host = os.environ.get('APP_REDIS_HOST_PROD')
            redis_port = os.environ.get('APP_REDIS_PORT_PROD')
            redis_auth = os.environ.get('APP_REDIS_AUTH_PROD')
        else:
            redis_host = os.environ.get('APP_REDIS_HOST_DEV')
            redis_port = os.environ.get('APP_REDIS_PORT_DEV')
            redis_auth = os.environ.get('APP_REDIS_AUTH_DEV')
        self.pool = redis.ConnectionPool(host=redis_host, port=redis_port, password=redis_auth)

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.getConnection()
        return self._conn

    def getConnecion(self):
        self._conn = redis.Redis(connection_pool=self.pool)