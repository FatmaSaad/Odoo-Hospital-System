from odoo import models, fields

class Doctors(models.Model):
    _name = "hms.doctors"
    _rec_name = 'fname'
    fname=fields.Char()
    lname=fields.Char()
    image=fields.Binary("Image")
