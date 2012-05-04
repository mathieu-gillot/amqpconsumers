import pymongo
from basebehavior import BaseBehavior

class MongoBehavior(BaseBehavior):

    def __init__(self, config, tag):
        host       = config.get(tag, "host")
        port       = int(config.get(tag, "port"))
        dbname     = config.get(tag, "dbname")
        collection = config.get(tag, "collection")

        # create mongo collection 
        self.mongo_connection = pymongo.Connection(host, port)
        self.mongo_collection = self.mongo_connection.dbname.collection

        super(MongoBehavior, self).__init__(config, tag)

    def callbackAction(self, body):
        self.mongo_collection.insert(body)
