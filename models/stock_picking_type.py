# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    report_title = fields.Char(
        string='Report title', default=False,
        help="This is the title that will be displayed in the reports of the pickings type.")

