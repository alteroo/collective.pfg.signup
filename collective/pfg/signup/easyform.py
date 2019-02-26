# -*- coding: utf-8 -*-

from collective.easyform.actions import Action
from collective.easyform.actions import ActionFactory
from collective.easyform.interfaces import IAction
from plone import api
from plone.supermodel.exportimport import BaseHandler
from zope import schema
from zope.component import queryMultiAdapter
from zope.globalrequest import getRequest
from zope.interface import implementer

import requests

from collective.pfg.signup import _
from collective.pfg.signup.adapter import SignUpAdapter
from collective.pfg.signup.interfaces import ISignUpAdapterSchema


class ISignUpAction(IAction, ISignUpAdapterSchema):
    """IFTTT action adapter on easyform that
    will send form fields data to IFTTT event."""


@implementer(ISignUpAction)
class SignupTrigger(SignUpAdapter):
    """Trigger for signup."""
    def __init__(self, **kw):
        for i, f in ISignUpAdapterSchema.namesAndDescriptions():
            setattr(self, i, kw.pop(i, f.default))
        super(SignupTrigger, self).__init__(**kw)


SignupAction = ActionFactory(
    SignupTrigger, _(u'SignUpAdapter'), 'collective.pfg.signup.easyformsignup'
)

SignupHandler = BaseHandler(SignupTrigger)