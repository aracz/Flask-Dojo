from peewee import *

db = PostgresqlDatabase('aracz', user='aracz')

class BaseModel(Model):
    class Meta:
        database = db


class Request(BaseModel):
    type = CharField()


db.connect()
#db.drop_table(Request)
#db.create_table(Request)


