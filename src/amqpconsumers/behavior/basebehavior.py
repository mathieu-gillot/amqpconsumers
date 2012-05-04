class BaseBehavior(object):

    def __init__(self, config, tag):
        # get specific queue conf values
        self._queue_name         = config.get(tag, "queue_name")
        self._no_acknowledgement = self.getConfValue(config, tag, "no_acknowledgement")
        self._queue_is_durable   = bool(self.getConfValue(config, tag, "queue_is_durable"))
        self._prefetch_count     = int(self.getConfValue(config, tag, "prefetch_count"))

    def getQueueName(self):
        return self._queue_name

    def getQueueIsDurable(self):
        return self._queue_is_durable

    def getQueueNoAcknowledgement(self):
        return self._no_acknowledgement

    def getPrefetchCount(self):
        return self._prefetch_count

    def callback(self, channel, method, properties, body):
        print " [x] Received %r" % (body,)

        # register asset movement in mongo collection
        self.callbackAction(body)

        # send aknowledgement for critical datas
        if self.no_acknowledgement:
            channel.basic_ack(delivery_tag=method.delivery_tag)

    def getConfValue(self, config, tag, field):
        if config.has_option(tag, field):
            ret = config.get(tag, field)
        elif config.has_option("DEFAULT", field):
            ret = config.get("DEFAULT", field)
        else:
            raise Exception(field + ' missing from mongo and DEFAULT config sections')

        return ret
