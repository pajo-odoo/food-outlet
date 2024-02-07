from odoo import fields, models

class SubcategoryModel(models.Model):
    _name = "subcategory.model"
    _description = "Subcategory Model"

    name = fields.Char("Subcategory Name", required=True)
    image = fields.Image()
