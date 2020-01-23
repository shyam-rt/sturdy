# -*- coding: utf-8 -*-

from odoo import models, fields, api


class showroom(models.Model):
    _name = 'showroom.showroom'
    _description = 'showroom.showroom'

    Bike_Name = fields.Char()
    Cost = fields.Integer()
    Customer_Name = fields.Char()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
