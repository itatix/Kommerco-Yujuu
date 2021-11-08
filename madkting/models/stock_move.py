# # -*- coding: utf-8 -*-
# # File:           stock_warehouse.py
# # Author:         Gerardo Lopez Vega
# # Copyright:      (C) 2021 All rights reserved by Madkting
# # Created:        2021-06-09

# from odoo import models, fields, api
# from odoo import exceptions
# from datetime import datetime
# from ..log.logger import logger
# from ..responses import results

# class StockMove(models.Model):
#     _inherit = "stock.move"

#     @api.model
#     def create(self, vals):
#         logger.info("## OVERRIDE METHOD CREATE ##")
#         logger.info(vals)
#         res = super(StockMove, self).create(vals)
#         return res

#     def write(self, vals):
#         logger.info("## OVERRIDE METHOD WRITE ##")
#         logger.info(vals)
#         res = super(StockMove, self).write(vals)
#         return res