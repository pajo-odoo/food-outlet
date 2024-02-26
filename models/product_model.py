#-*- coding: utf-8 -*-

from odoo import fields, models

class ProductModel(models.Model):
    _name = "product.model"
    _description = "Product Model"

    name = fields.Char("Product Name", required=True)
    description = fields.Text("Description")
    is_available = fields.Boolean("Available")
    price = fields.Integer("Price")
    rating = fields.Integer("Rating")
    food_type = fields.Selection(
        string="Type",
        selection=[("veg", "Veg"), ("non_veg", "Non-Veg"), ("eggetarian", "Eggetarian")],
    )
    tag_ids = fields.Many2many(comodel_name="product.tag.model", string="Tags")
    time_to_cook = fields.Integer("Time to cook")
    image = fields.Image("Image")
    subcategory_id = fields.Many2one(comodel_name="subcategory.model", string="Subcategories")
    restaurant_id = fields.Many2one(comodel_name="restaurant.model", string="Restaurant")

    _sql_constraints = [
        ("check_price_positive", "CHECK(price > 0)", "Price must be strictly positive!"),
        ("check_rating_positive", "CHECK(rating > 0)", "Rating must be strictly positive!"),
    ]
