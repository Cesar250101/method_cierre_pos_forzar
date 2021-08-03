# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class SessionPOS(models.Model):
    _inherit = 'pos.session'

    @api.multi
    def pos_session_close(self):
        self.write({
            'state':'closed',
            'stop_at':datetime.datetime.now(),
        })
        
