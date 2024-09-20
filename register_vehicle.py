# -*- coding: utf-8 -*-
# Copyright 2022-Today TechKhedut.
# Part of TechKhedut. See LICENSE file for full copyright and licensing details.
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class RegisterVehicle(models.Model):
    """Register Vehicle"""
    _name = 'register.vehicle'
    _description = __doc__
    _rec_name = 'vehicle_brand_id'

    customer_id = fields.Many2one('res.partner', string='Customer')
    vehicle_brand_id = fields.Many2one('vehicle.brand', string="Vehicle")
    vehicle_model_id = fields.Many2one('vehicle.model', string="Model",
                                       domain="[('vehicle_brand_id', '=', vehicle_brand_id)]")
    registration_no = fields.Char(string="Registration No")
    vehicle_fuel_type_id = fields.Many2one('vehicle.fuel.type', string="Fuel Type")
    transmission_type = fields.Selection([('manual', "Manual"), ('automatic', "Automatic"), ('cvt', "CVT")],
                                         string="Transmission Type")
    vin_no = fields.Char(string="VIN Number")

    _sql_constraints = [
        ('unique_registration_no', 'unique (registration_no)',
         'Registration number already in use.')
    ]
