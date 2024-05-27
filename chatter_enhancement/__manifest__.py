# -*- coding: utf-8 -*-

{
    'name': 'Chatter Enhancement',
    'version': '16.0.1',
    'category': 'Productivity/Discuss',
    'summary': 'Enhancement into chatter message template.',
    'description': """
        Display the exact date and time when an email was sent directly in the chatter message.
        Display the name of the outgoing mail server and the email address used for sending the email.
        Display the recipient's name and email address directly in the chatter message.
    """,
    'depends': ['base','mail'],
    'data': [
    ],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'chatter_enhancement/static/src/component/message_extend.xml'
        ],
        'mail.assets_core_messaging': [

            'chatter_enhancement/static/src/component/message_extend.js',
        ],
    },
    'license': 'LGPL-3',
}
