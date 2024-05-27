/** @odoo-module **/

import { clear } from '@mail/model/model_field_command';
import { registerPatch } from '@mail/model/model_core';
import { attr, many, one } from '@mail/model/model_field';

registerPatch({
    name: 'Message',
    modelMethods: {
        convertData(data) {
            const data2 = this._super(...arguments);
            if ('outgoing_mail_server_name' in data) {
                data2.outgoing_mail_server_name = data.outgoing_mail_server_name
            }
            if ('recipients_list' in data) {
                data2.recipients_list = data.recipients_list
            }
            return data2;
        },
    },
    fields: {
        /**
         * Determines whether this message should have the outgoing_mail_server_name and recipient list
         */
        
        outgoing_mail_server_name : attr({
            compute() {
                if(this.outgoing_mail_server_name) {
                    return this.outgoing_mail_server_name
                }
            }
        }),
        recipients_list : attr({
            compute() {
                if(this.recipients_list) {
                    return this.recipients_list
                }
            }
        }),
    },
});
