{
    "name": "Gestión de Paquetería y Camiones",
    "version": "1.0",
    "category": "Logistics",
    "summary": "Gestión de paquetes, camiones y seguimiento de envíos",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/paquete_views.xml",
        "views/seguimiento_views.xml",
        "views/camion_views.xml",
    ],
    "application": True,
}
