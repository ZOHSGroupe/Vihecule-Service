import os
from dotenv import load_dotenv

load_dotenv()

workers = 2
worker_class = "gevent"
# in development
bind = f"127.0.0.1:{os.getenv('VIHECULE_DOCKER_PORT')}"
# in Dockerize
#bind = f"0.0.0.0:{os.getenv('VIHECULE_DOCKER_PORT')}"
reload = True
