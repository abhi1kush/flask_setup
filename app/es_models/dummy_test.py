import datetime
from elasticsearch_dsl import Document, Date, Boolean, Text

ALIAS = "dummyIndex"


class DummyTest1(Document):
    name = Text()
    created_on = Date()

    class Index:
        name = ALIAS


class DummyTestManager:
    model = DummyTest1

    @classmethod
    def index(cls, name):
        obj = cls.model(
            index=name,
            created_on=datetime.datetime.now()
        )
        obj.save()
        return obj

