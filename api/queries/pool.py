import os
from psycopg_pool import ConnectionPool

<<<<<<< HEAD

pool = ConnectionPool(conninfo=os.environ.get("DATABASE_URL"))
=======
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
>>>>>>> 07bb1e9a4afcd1ff4da0d0254a945f01eb482928
