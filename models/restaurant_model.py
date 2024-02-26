#-*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class RestaurantModel(models.Model):
    _name = "restaurant.model"
    _description = "Restaurant Model"
    _order = "id desc"

    name = fields.Char("Restaurant Name", required=True)
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    address = fields.Text("Address")
    description = fields.Text("Description")
    open_time = fields.Datetime("Open Time")
    close_time = fields.Datetime("Close Time")
    image = fields.Image("Image")
    category_ids = fields.Many2many(comodel_name="category.model", string="Categories")
    product_ids = fields.One2many(comodel_name="product.model", string="Products", inverse_name="restaurant_id")

    @api.constrains("open_time", "close_time")
    def _check_date_end(self):
        for record in self:
            if record.close_time < record.open_time:
                raise ValidationError("The close time must not before open time")
