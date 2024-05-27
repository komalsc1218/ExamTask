# -*- coding: utf-8 -*-

from odoo import api, fields, models
import json


class MailMessage(models.Model):
    _inherit = 'mail.message'

    outgoing_mail_server_name = fields.Char(string="Outgoing Mail Server", compute='_compute_outgoing_mail_server_name', store=True)
    recipients_list = fields.Char(string="Recipients List", compute='_compute_recipients_list', store=True)

    @api.depends('mail_server_id', 'mail_server_id.name', 'mail_server_id.smtp_user')
    def _compute_outgoing_mail_server_name(self):
        for message in self:
            if message.mail_server_id:
                message.outgoing_mail_server_name = f"{message.mail_server_id.name} <{message.mail_server_id.smtp_user}>"

    @api.depends('partner_ids')
    def _compute_recipients_list(self):
        for message in self:
            recipients_list = ', '.join(f"{partner.name} <{partner.email}>" for partner in message.partner_ids)
            message.recipients_list = recipients_list

    def _message_format(self, fnames, format_reply=True, legacy=False):
        result = super(MailMessage, self)._message_format(fnames, format_reply, legacy)
        msg_list = []
        for message_data in result:
            msg_id = self.env['mail.message'].search([('id', '=', message_data.get('id'))])
            if msg_id:
                message_data.update({'outgoing_mail_server_name' : msg_id.outgoing_mail_server_name})
                message_data.update({'recipients_list' : msg_id.recipients_list})      
            msg_list.append(message_data)
        return msg_list