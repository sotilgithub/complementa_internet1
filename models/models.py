# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class basico_generado9(models.Model):
#     _name = 'basico_generado9.basico_generado9'
#     _description = 'basico_generado9.basico_generado9'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
