#-*- coding: utf-8 -*-

from odoo import fields, models

class CategoryTagModel(models.Model):
    _name = "category.tag.model"
    _description = "Category Tag model"
    _order = "name"

    name = fields.Char("Tag Name", required=True)

    _sql_constraints = [
        ("unique_category_tag", "unique(name)", "Tag with same name already exists."),
    ]
