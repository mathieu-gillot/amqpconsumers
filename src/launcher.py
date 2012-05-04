import sys
from amqpconsumers.amqpworker import AmqpWorker
import ConfigParser

class Launcher(object):

    def __init__(self):
        pass

if len(sys.argv) != 2:
    raise Exception('launcher takes one argument : behavior\'s tag')

tag = sys.argv[1]

config = ConfigParser.ConfigParser()
config.read('workers.cfg')

try:
    class_name     = config.get(tag, "behavior_class")
except:
    raise Exception('Unknow ' + tag + ' behavior')

# 
import_name      = 'amqpconsumers.behavior.' + class_name.lower()
behavior_module  = __import__(name=import_name, fromlist=[class_name])
behavior_class   = getattr(behavior_module, class_name)  
behavior         = behavior_class(config, tag)

worker = AmqpWorker(config, behavior)
worker.run()
