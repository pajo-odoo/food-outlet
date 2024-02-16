#-*- coding: utf-8 -*-

from odoo import fields, models

class RestaurantModel(models.Model):
    _name = "restaurant.model"
    _description = "Restaurant Model"

    name = fields.Char("Restaurant Name", required=True)
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    address = fields.Text("Address")
    description = fields.Text("Description")
    open_time = fields.Datetime("Open Time")
    close_time = fields.Datetime("Close Time")
    image = fields.Image("Image")
    category_ids = fields.Many2many(comodel_name="category.model", string="Categories")
