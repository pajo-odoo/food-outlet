#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Food Outlet",
    "category": "Food",
    "description": "This is for Restaurants",
    "summary": "This is a food management system for restaurants to show menu and get bookings from the customers.",
    "installable": True,
    "application": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "security/food_outlet_security.xml",

        "views/restaurant_views.xml",
        "views/category_views.xml",
        "views/subcategory_views.xml",
        "views/product_views.xml",
        "views/category_tag_views.xml",
        "views/product_tag_views.xml",
        "views/food_outlet_menus.xml",
    ],
}
