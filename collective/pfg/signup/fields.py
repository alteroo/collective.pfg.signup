from collective.pfg.signup import _
from collective.pfg.signup.validators import isTALES
from Products.Archetypes import atapi


def full_name_field(isDx=True):
    _params = dict(
        default=u'fullname',
        required=False,
    )
    title = _(u'label_full_name', default=u'Full Name Field')
    description = _(
        u'help_full_name_field',
        default=u"""Enter the id of the field that will be used for the
                    user's full name.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params


def username_field(isDx=True):
    _params = dict(required=False)
    title = _(u'label_username', default=u'Username Field')
    description = _(
        u'help_username_field',
        default=u"""Enter the id of the field that will be used for the
                    user's user id. If this field is left empty the
                    email address will be used for the username.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params


def email_field(isDx=True):
    _params = dict(
        default=u'email',
        required=True
    )
    title = _(u'label_email', default=u'Email Field')
    description = _(
        u'help_email_field',
        default=u"""Enter the id of the field that will be used for the
                    user's email address. This field is required.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params

def password_field(isDx=True):
    _params = dict(required=False)
    title = _(u'label_password', default=u'Password Field')
    description = _(
        u'help_password_field',
        default=u"""Enter the id of the field that will be used for the
                    user's password. If the Approval Group Template
                    field is empty, and this field is empty, users
                    signing up will be sent a password reset email.
                    """)
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params

def password_verify_field(isDx=True):
    _params = dict(required=False)
    title = _(
        u'label_password_verify',
        default=u'Password Verify Field')
    description = _(
        u'help_password_verify_field',
        default=u"""If there is a password and password verify field
                    and the Approval Group Template field is empty,
                    Users will be able to set their passwords and login
                    immediately.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params

def user_group_template(isDx=True):
    _params = dict(
        default=u"python:{'Administrators': ['*']}",
        required=True
    )
    title = _(
        u'label_user_group_template',
        default=u'Add to User Group Template')
    description  =_(
        u'help_add_to_user_group_template',
        default=u"""A TALES expression to calculate the group the user
                    should be added to. Fields in the form can be used
                    to populate this. eg string:${department}_${role}.
                    Leave both this and 'Manage Group Template' empty
                    to allow creation of user accounts without any
                    management.
                    """)
    if isDx:
        _params['title'] = title
        _params['description'] = description
        _params['constraint'] = isTALES
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params


def manage_group_template(isDx=True):
    _params = dict(required=False)
    title = _(
        u'label_manage_group_template',
        default=u'Manage Group Template')
    description = _(
        u'help_manage_group_template',
        default=u"""A TALES expression return a dictionary where 'key'
                    value is which group the 'value' value should be
                    manage by. Leave both this and
                    'Add to User Group Template' empty to allow
                    creation of user accounts without any management.
                    eg python:{'Administrators': ['group_name']}.
                    This TALES expression is allowing all the users
                    under 'group_name' group will be managed by
                    'Administrators' group.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        _params['constraint'] = isTALES
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params


def email_domain_verification(isDx=True):
    _params = dict(
        default=False,
        required=False
    )
    title = _(
        u'label_email_domain_verification',
        default=u'Email Domain Verification')
    description = _(
        u'help_email_domain_verification',
        default=u"""Check this option to have addition 
        verification for domain in email field need to match with 
        the association group.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.BooleanWidget(
        label=title,
        description=description
    )
    return _params


def error_message_email_domain_verification(isDx=True):
    _params = dict(required=False)
    
    title = _(u'label_error_message_email_domain_verification',
            default=u'Error Message When Email Domain Is Not Match')
    description = _(
        u'help_email_domain_verification',
        default=u"""Enter error message that will display to the user 
        when domain of the email address is not match. It will use 
        default message if this field is blank.""")
    if isDx:
        _params['title'] = title
        _params['description'] = description
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params


def execCondition(isDx=True):
    _params = dict(default=u'', required=False)
    title = _(u'label_execcondition_text', default=u'Execution Condition')
    description = _(
        u'help_execcondition_text',
        default=u'A TALES expression that will be evaluated to determine '
                u'whether or not to execute this action. Leave empty if '
                u'unneeded, and the action will be executed. Your '
                u'expression should evaluate as a boolean; return True '
                u'if you wish the action to execute. PLEASE NOTE: errors '
                u'in the evaluation of this expression will  cause an '
                u'error on form display.'
    )
    if isDx:
        _params['title'] = title
        _params['description'] = description
        _params['constraint'] = isTALES
        return _params
    _params['widget'] = atapi.StringWidget(
        label=title,
        description=description
    )
    return _params