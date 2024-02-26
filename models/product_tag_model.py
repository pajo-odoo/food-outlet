#-*- coding: utf-8 -*-

from odoo import fields, models

class ProductTagModel(models.Model):
    _name = "product.tag.model"
    _description = "product Tag model"
    _order = "name"

    name = fields.Char("Tag Name", required=True)

    _sql_constraints = [
        ("unique_product_tag", "unique(name)", "Tag with same name already exists."),
    ]
    