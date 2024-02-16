#-*- coding: utf-8 -*-

from odoo import fields, models

class CategoryTagModel(models.Model):
    _name = "category.tag.model"
    _description = "Category Tag model"

    name = fields.Char("Tag Name", required=True)
