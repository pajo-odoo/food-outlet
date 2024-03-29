#-*- coding: utf-8 -*-

from odoo import fields, models

class CategoryModel(models.Model):
    _name = "category.model"
    _description = "Category Model"
    _order = "sequence, id desc"

    name = fields.Char("Category Name", required=True)
    description = fields.Text("Description")
    sequence = fields.Integer("Sequence", default=1)
    tag_ids = fields.Many2many(comodel_name="category.tag.model", string="Tags")
    image = fields.Image("Image")
    order = fields.Integer("Order")
    active = fields.Boolean("Active", default=True)
    restaurant_ids = fields.Many2many(comodel_name="restaurant.model", string="Restaurants")
    subcategory_ids = fields.Many2many(comodel_name="subcategory.model", string="Subcategories")

    _sql_constraints = [
        ("check_order_positive", "CHECK(order >= 0)", "Order must be positive!"),
    ]
