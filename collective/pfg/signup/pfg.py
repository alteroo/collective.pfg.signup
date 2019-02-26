"""Initialise module package."""
from BTrees.OOBTree import OOBTree
from Products.Archetypes import atapi
from Products.ATContentTypes.content.base import registerATCT
from Products.CMFCore import utils
from Products.PloneFormGen.content.actionAdapter import FormActionAdapter
from Products.PloneFormGen.content.actionAdapter import FormAdapterSchema
from Products.PloneFormGen.interfaces import IPloneFormGenActionAdapter
from Products.TALESField import TALESString

from collective.pfg.signup import _
from collective.pfg.signup import config
from collective.pfg.signup import fields as signupFields
from collective.pfg.signup.adapter import SignUpAdapter as BaseSignUpAdapter
from collective.pfg.signup.interfaces import ISignUpAdapter
from zope import schema
from zope.interface import implements
from z3c.form.field import Fields


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    # Retrieve the content types that have been registered with Archetypes
    # This happens when the content type is imported and the registerType()
    # call in the content type's module is invoked. Actually, this happens
    # during ZCML processing, but we do it here again to be explicit. Of
    # course, even if we import the module several times, it is only run
    # once.

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    # Now initialize all these content types. The initialization process takes
    # care of registering low-level Zope 2 factories, including the relevant
    # add-permission. These are listed in config.py. We use different
    # permissions for each content type to allow maximum flexibility of who
    # can add which content types, where. The roles are set up in rolemap.xml
    # in the GenericSetup profile.

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
                          content_types=(atype, ),
                          permission=config.ADD_PERMISSIONS[atype.portal_type],
                          extra_constructors=(constructor,),
                          ).initialize(context)


# SignUpAdapterSchema = FormAdapterSchema.copy() + atapi.Schema((

#     atapi.StringField(
#         'full_name_field',
#         **signupFields.full_name_field(False)
#     ),

#     atapi.StringField(
#         'username_field',
#         **signupFields.username_field(False)
#     ),

#     atapi.StringField(
#         'email_field',
#         **signupFields.email_field(False)
#     ),

#     atapi.StringField(
#         'password_field',
#         **signupFields.password_field(False)
#     ),

#     atapi.StringField(
#         'password_verify_field',
#         **signupFields.password_verify_field(False)
#     ),

#     TALESString(
#         'user_group_template',
#         **signupFields.user_group_template(False)
#     ),

#     TALESString(
#         'manage_group_template',
#         **signupFields.manage_group_template(False)
#     ),

#     atapi.BooleanField(
#         'email_domain_verification',
#         **signupFields.email_domain_verification(False)
#     ),

#     atapi.StringField(
#         'error_message_email_domain_verification',
#         **signupFields.error_message_email_domain_verification(False)
#     )

# ))


# class SignUpAdapter(BaseSignUpAdapter, FormActionAdapter):
#     implements(IPloneFormGenActionAdapter, ISignUpAdapter)
#     schema = SignUpAdapterSchema

#     def __init__(self, oid, **kwargs):
#         """Initialize class."""
#         FormActionAdapter.__init__(self, oid, **kwargs)
#         self.waiting_list = OOBTree()

# registerATCT(SignUpAdapter, config.PROJECTNAME)