#-*- coding: utf-8 -*-

from odoo import fields, models

class ProductTagModel(models.Model):
    _name = "product.tag.model"
    _description = "product Tag model"

    name = fields.Char("Tag Name", required=True)
