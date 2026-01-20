# Gestión de Paquetería y Camiones

Este módulo permite gestionar una empresa de transporte mediante el control de
paquetes, camiones y el seguimiento de los envíos.

## Los Modelos
- Paquete: representa un envío con remitente, destinatario y seguimiento.
- Seguimiento: almacena los estados del paquete a lo largo del tiempo.
- Camión: gestiona la flota de camiones y los paquetes transportados.

## Funcionamiento
Cada paquete puede tener múltiples actualizaciones de seguimiento que se muestran
dentro de su vista de formulario. Los camiones pueden transportar varios paquetes
y tener conductores actuales y antiguos.

## Uso
1. Crear camiones
2. Crear paquetes y asignarlos a un camión
3. Añadir seguimientos desde el formulario del paquete

