#
#

from zope.interface import implements
from twisted.trial.itrial import IReporter
from twisted.plugin import IPlugin


class _Reporter(object):
    implements(IPlugin, IReporter)

    def __init__(self, name, module, description, longOpt, shortOpt, klass):
        self.name = name
        self.module = module
        self.description = description
        self.longOpt = longOpt
        self.shortOpt = shortOpt
        self.klass = klass

junitxml = _Reporter('JUnitXml Reporter',
    'trialjunitxml.trialjunitxml',
    description='Outputs the test results in JUnit compatible xml',
    longOpt='junitxml',
    shortOpt=None,
    klass='JUnitXmlReporter')
