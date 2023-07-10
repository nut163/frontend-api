```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    usage = Column(Float, default=0.0)

class DataInput(Base):
    __tablename__ = 'data_inputs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    data = Column(String)
```