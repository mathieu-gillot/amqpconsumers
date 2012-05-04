import pycurl
from basebehavior import BaseBehavior

class KontagentBehavior(BaseBehavior):

    def __init__(self, config, tag):
        # create curl object
        self._curl = pycurl.Curl()

        super(KontagentBehavior, self).__init__(config, tag)

    def callbackAction(self, body):
        self._curl.setopt(pycurl.URL, body)
        self._curl.perform()
