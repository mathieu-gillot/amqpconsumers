import pika

class AmqpWorker(object):

    def __init__(self, config, behavior):
        # get amqp config
        user     = config.get("amqp", "user")
        password = config.get("amqp", "password")
        vhost    = config.get("amqp", "vhost")
        host     = config.get("amqp", "host")

        # create amqp connection
        self.connection = self._createAmqpConnection(user, password, vhost, host)

        # set behavior
        self.behavior = behavior 

    def _createAmqpConnection(self, user, password, vhost, host):
        credentials = pika.PlainCredentials(user, password)
        parameters  = pika.ConnectionParameters(host=host, credentials=credentials, virtual_host=vhost)

        return pika.BlockingConnection(parameters)

    def run(self):
        # set queue configuration, then declare it
        queue_name         = self.behavior.getQueueName()
        queue_is_durable   = self.behavior.getQueueIsDurable()
        no_acknowledgement = self.behavior.getQueueNoAcknowledgement()
        prefetch_count     = self.behavior.getPrefetchCount()

        channel            = self.connection.channel()

        channel.queue_declare(queue=queue_name, durable=queue_is_durable)
        # don't deal with more than one message at a time
        channel.basic_qos(prefetch_count=prefetch_count)
        channel.basic_consume(self.behavior.callback, queue_name, no_ack=no_acknowledgement)
        print ' [*] Waiting for messages. To exit press CTRL+C'

        # start the worker
        channel.start_consuming()
