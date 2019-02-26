"""Interfaces."""
from plone.app.z3cform import widget
from plone.autoform import directives
from plone.supermodel import model
from zope import schema
from zope.interface import Interface

from collective.pfg.signup import _
from collective.pfg.signup.config import MODIFY_PORTAL_CONTENT
from collective.pfg.signup.validators import isTALES


class ISignUpAdapter(Interface):

    """A PloneFormGen adapter that saves signup form."""


class ISignUpAdapterSchema(model.Schema):

    full_name_field = schema.TextLine(
        default=u'fullname',
        required=False,
        title=_(u'label_full_name', default=u'Full Name Field'),  # noqa H702
        description=_(
            u'help_full_name_field',
            default=u"""Enter the id of the field that will be used for the
                        user's full name."""),
    )

    username_field = schema.TextLine(
        required=False,
        title=_(u'label_username', default=u'Username Field'),
        description=_(
            u'help_username_field',
            default=u"""Enter the id of the field that will be used for the
                        user's user id. If this field is left empty the
                        email address will be used for the username."""),
    )

    email_field = schema.TextLine(
        default=u'email',
        required=True,
        title=_(u'label_email', default=u'Email Field'),
        description=_(
            u'help_email_field',
            default=u"""Enter the id of the field that will be used for the
                        user's email address. This field is required."""),
    )

    password_field = schema.TextLine(
        required=False,
        title=_(u'label_password', default=u'Password Field'),
        description=_(
            u'help_password_field',
            default=u"""Enter the id of the field that will be used for the
                        user's password. If the Approval Group Template
                        field is empty, and this field is empty, users
                        signing up will be sent a password reset email.
                        """),
    )

    password_verify_field = schema.TextLine(
        required=False,
        title=_(
            u'label_password_verify',
            default=u'Password Verify Field'),
        description=_(
            u'help_password_verify_field',
            default=u"""If there is a password and password verify field
                        and the Approval Group Template field is empty,
                        Users will be able to set their passwords and login
                        immediately."""),
    )

    user_group_template = schema.TextLine(
        default=u"python:{'Administrators': ['*']}",
        required=True,
        title=_(
            u'label_user_group_template',
            default=u'Add to User Group Template'),
        description=_(
            u'help_add_to_user_group_template',
            default=u"""A TALES expression to calculate the group the user
                        should be added to. Fields in the form can be used
                        to populate this. eg string:${department}_${role}.
                        Leave both this and 'Manage Group Template' empty
                        to allow creation of user accounts without any
                        management.
                        """),
        constraint=isTALES,
    )

    manage_group_template = schema.TextLine(
        required=False,
        title=_(
            u'label_manage_group_template',
            default=u'Manage Group Template'),
        description=_(
            u'help_manage_group_template',
            default=u"""A TALES expression return a dictionary where 'key'
                        value is which group the 'value' value should be
                        manage by. Leave both this and
                        'Add to User Group Template' empty to allow
                        creation of user accounts without any management.
                        eg python:{'Administrators': ['group_name']}.
                        This TALES expression is allowing all the users
                        under 'group_name' group will be managed by
                        'Administrators' group."""),
        constraint=isTALES,
    )

    email_domain_verification = schema.Bool(
        default=False,
        required=False,
        title=_(
            u'label_email_domain_verification',
            default=u'Email Domain Verification'),
        description=_(
            u'help_email_domain_verification',
            default=u"""Check this option to have addition 
            verification for domain in email field need to match with 
            the association group.""")
    )
    directives.widget(
        'email_domain_verification',
        widget.SingleCheckBoxBoolWidget
    )

    error_message_email_domain_verification = schema.TextLine(
        required=False,
        title=_(u'label_error_message_email_domain_verification',
                default=u'Error Message When Email Domain Is Not Match'),
        description=_(
            u'help_email_domain_verification',
            default=u"""Enter error message that will display to the user 
            when domain of the email address is not match. It will use 
            default message if this field is blank."""),
    )

    model.fieldset(
        'overrides',
        label=_(u"Overrides"),
        fields=['execCondition']
    )
    directives.read_permission(execCondition=MODIFY_PORTAL_CONTENT)
    directives.write_permission(execCondition=MODIFY_PORTAL_CONTENT)
    execCondition = schema.TextLine(
        title=_(u'label_execcondition_text', default=u'Execution Condition'),
        description=_(
            u'help_execcondition_text',
            default=u'A TALES expression that will be evaluated to determine '
                    u'whether or not to execute this action. Leave empty if '
                    u'unneeded, and the action will be executed. Your '
                    u'expression should evaluate as a boolean; return True '
                    u'if you wish the action to execute. PLEASE NOTE: errors '
                    u'in the evaluation of this expression will  cause an '
                    u'error on form display.'
        ),
        default=u'',
        constraint=isTALES,
        required=False,
    )
