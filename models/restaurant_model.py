from odoo import fields, models

class RestaurantModel(models.Model):
    _name = "restaurant.model"
    _description = "Restaurant Model"

    name = fields.Char("Restaurant Name", required=True)
    phone = fields.Text()
    email = fields.Text()
    address = fields.Text()
    description = fields.Text()
    open_time = fields.Char()
    close_time = fields.Char()
    image = fields.Image()
