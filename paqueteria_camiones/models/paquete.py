from odoo import models, fields

class Paquete(models.Model):
    _name = "paqueteria.paquete"
    _description = "Paquete"

    name = fields.Char(
        string="Nº de seguimiento",
        required=True
    )

    remitente_id = fields.Many2one(
        "res.partner",
        string="Remitente",
        required=True
    )

    destinatario_id = fields.Many2one(
        "res.partner",
        string="Destinatario",
        required=True
    )

    direccion_entrega = fields.Text(
        string="Dirección de entrega"
    )

    camion_id = fields.Many2one(
        "paqueteria.camion",
        string="Camión"
    )

    actualizaciones_ids = fields.One2many(
        "paqueteria.seguimiento",
        "paquete_id",
        string="Seguimiento del envío"
    )
