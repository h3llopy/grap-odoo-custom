# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    @api.constrains("active")
    def _check_archive(self):
        return True
