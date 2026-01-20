from odoo import models, fields

class Seguimiento(models.Model):
    _name = "paqueteria.seguimiento"
    _description = "Seguimiento del Paquete"

    paquete_id = fields.Many2one(
        "paqueteria.paquete",
        string="Paquete",
        required=True,
        ondelete="cascade"
    )

    fecha = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now
    )

    estado = fields.Selection(
        [
            ("almacen", "En almacén"),
            ("transito", "En tránsito"),
            ("reparto", "En reparto"),
            ("entregado", "Entregado"),
        ],
        string="Estado",
        required=True
    )

    notas = fields.Text(
        string="Notas"
    )
