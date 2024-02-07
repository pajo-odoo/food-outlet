from odoo import fields, models

class ProductModel(models.Model):
    _name = "product.model"
    _description = "Product Model"

    name = fields.Char("Product Name", required=True)
    description = fields.Text()
    is_available = fields.Boolean()
    price = fields.Integer()
    final_price = fields.Integer()
    rating = fields.Integer()
    discount = fields.Integer()
    food_type = fields.Selection(
        string='Type',
        selection=[('veg', 'Veg'), ('non_veg', 'Non-Veg'), ('eggetarian', 'Eggetarian')],
        )
    tag = fields.Char()
    time_to_cook = fields.Integer()
