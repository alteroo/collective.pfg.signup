"""Initialise module package."""
import logging
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
_ = MessageFactory('collective.pfg.signup')
logger = logging.getLogger('collective.pfg.signup')
