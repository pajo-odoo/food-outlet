#-*- coding: utf-8 -*-

from odoo import fields, models

class CategoryModel(models.Model):
    _name = 'category.model'
    _description = 'Category Model'

    name = fields.Char('Category Name', required=True)
    description = fields.Text()
    tag = fields.Char()
    image = fields.Image()
    order = fields.Integer()
    isActive = fields.Boolean(default=True)
    restaurant_id = fields.Many2One(string='Restaurant', comodel_name='restaurant.model')
