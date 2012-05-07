amqpconsumers
=============

Usage : python launcher.py [tag]

tag is a <code>workers.cfg</code> section's tag.

To add a new consumer, add a new section in <code>workers.cfg</code>, implement a behavior class for this consumer, and add specific configuration to dedicated section in <code>workers.conf</code>

Requirements
=============

[python-pika] (http://pypi.python.org/pypi/pika) is a pure python implementationof the <code>amqp</code> protocol.
[pycurl] (http://pycurl.sourceforge.net/) is a python interface to <code>libcurl</code>. Used in kontagent consumer.
[pymongo] (http://api.mongodb.org/python/2.1.1/) is a Python distribution containing tools for working with <code>MongoDB</code>

Tutorial and Sample Code
=======================

to add a new bahavior, implement the class in <code>src/amqpconsumers/behavior</code> :

<code>
import ... #import behavior's specific dependency
from basebehavior import BaseBehavior

class YourBehavior(BaseBehavior):

    def __init__(self, config, tag):
        # build behavior's specific config
        # ...

        # init BaseBahavior to get behavior's global config
        super(YourBehavior, self).__init__(config, tag)

    def callbackAction(self, body):
        # implement behavior's actions when an element is caught from the queue
        # ...
</code>
