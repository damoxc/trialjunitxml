import sys
from junitxml import JUnitXmlResult
from twisted.trial.reporter import Reporter

class JUnitXmlReporter(JUnitXmlResult, Reporter):
    
    def __init__(self, stream=sys.stdout, tbformat='default',
            realtime=False, publisher=None):
        JUnitXmlResult.__init__(self, stream)
        Reporter.__init__(self, stream, tbformat, realtime, publisher)
        self.startTestRun()

    def done(self):
        self.stopTestRun()
