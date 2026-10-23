# Proyecto final: sistema de atención de solicitudes

**Integración:** semana 14 · **Entrega y presentación:** semana 15 · **Ponderación:** 20%

## Propósito

Construya una aplicación de consola para que un pequeño equipo de soporte registre y atienda solicitudes. El sistema debe guardar la información en una base SQLite de SQLite Cloud, de modo que los registros permanezcan disponibles al cerrar el programa y se pueda acceder a ellos por internet.

El proyecto integra los aprendizajes de Programación I: análisis del problema y algoritmos; variables, entradas y salidas; decisiones y ciclos; colecciones; funciones; módulos y Git; archivos y métodos; generadores y decoradores; clases y objetos; herencia y polimorfismo; y operaciones CRUD con una base de datos.

## Situación y datos

Una persona de soporte recibe solicitudes de estudiantes o docentes y debe poder organizarlas, revisar su estado y decidir cuáles atender primero. Cada solicitud tendrá un identificador, título, descripción, categoría, prioridad, estado y nombre de quien la reporta. Use los estados **Abierta**, **En proceso** y **Cerrada**, y las prioridades **Baja**, **Media** y **Alta**.

## Funciones requeridas

El menú debe permitir:

1. Registrar una solicitud y validar sus campos obligatorios.
2. Mostrar todas las solicitudes, con un mensaje claro si todavía no hay registros.
3. Buscar por identificador o por parte del título.
4. Cambiar la prioridad o el estado, comprobando que la solicitud exista y que el nuevo valor sea válido.
5. Eliminar una solicitud con confirmación.
6. Mostrar un reporte de solicitudes abiertas, filtrado por prioridad.
7. Exportar el reporte a un archivo de texto para poder compartirlo.
8. Salir sin perder los cambios guardados en la base de datos.

## Integración de los temas

- **Análisis y fundamentos:** incluya una descripción del problema, los datos de entrada, las reglas y el algoritmo o pseudocódigo antes de programar.
- **Decisiones, ciclos y colecciones:** use un menú repetitivo, validaciones y estructuras adecuadas para procesar resultados y búsquedas.
- **Funciones y módulos:** separe la interacción con la persona usuaria, la lógica del sistema y el acceso a la base de datos. Pase valores mediante parámetros y retornos; evite variables globales para compartir información.
- **Archivos y métodos:** exporte el reporte con `with open` y use métodos apropiados para normalizar texto y procesar registros.
- **Generadores y decoradores:** use un generador para recorrer las solicitudes que cumplen el filtro del reporte y un decorador que anuncie el inicio y el cierre de su generación.
- **Clases, herencia y polimorfismo:** modele la solicitud con una clase base y al menos dos tipos especializados que compartan un método, por ejemplo para describir o calcular prioridad. Recorra los tipos mediante ese método común.
- **Base de datos:** persista los datos en SQLite Cloud con `sqlitecloud`, consultas parametrizadas con `?` y la variable `SQLITECLOUD_URL`.
- **Git:** guarde avances con commits descriptivos y prepare instrucciones para descargar, configurar y ejecutar el proyecto.

No es necesario crear una página web ni una interfaz gráfica. El alcance es una aplicación de consola clara, completa y fácil de demostrar.

## Base de datos gratuita

La guía de [semana 13](../semana_13_sqlite/README.md) explica cómo registrarse en SQLite Cloud, crear un proyecto y una base, instalar `sqlitecloud` y configurar la cadena de conexión. El plan gratuito publicado ofrece 512 MB de almacenamiento y hasta 20 conexiones simultáneas; sus límites pueden cambiar.

Revise la [introducción oficial al SDK de Python](https://docs.sqlitecloud.io/docs/sdk-python-introduction) y las condiciones del [plan gratuito](https://sqlitecloud.io/pricing). Guarde las credenciales fuera del código y nunca las incluya en Git.

## Organización recomendada

Puede partir de `ejemplo_estructura/` y adaptarla. Se recomienda mantener módulos separados para el menú, las clases del dominio, las consultas de base de datos y los reportes. Los nombres y las responsabilidades pueden variar si se mantiene una organización clara.

## Etapas de trabajo

1. **Planificar:** describa el problema, defina los campos y reglas, y bosqueje el menú y las operaciones.
2. **Construir el flujo:** implemente el menú y la validación con datos temporales antes de conectar la base.
3. **Modelar y persistir:** añada las clases, especializaciones y operaciones de base de datos.
4. **Integrar y reportar:** conecte las operaciones, el generador, el decorador y la exportación del reporte.
5. **Revisar y presentar:** pruebe todos los caminos, documente la ejecución y prepare una demostración breve.

## Entrega

- Código fuente `.py` organizado en módulos y un `requirements.txt`.
- Este repositorio o una carpeta del proyecto con commits que muestren el avance.
- Un `README.md` propio con propósito, configuración de SQLite Cloud, instalación y pasos de ejecución; no debe contener credenciales.
- Descripción de la tabla y de las decisiones de diseño principales.
- Casos de prueba y evidencia de una ejecución con solicitudes creadas, consultadas, actualizadas, eliminadas y reportadas.
- Presentación oral en la que cada integrante explique una parte del programa y responda preguntas sobre su funcionamiento.

## Criterios de evaluación

| Criterio | Ponderación |
|---|---:|
| Funciones requeridas y validación de datos | 25% |
| Integración de los temas del curso y diseño del programa | 25% |
| Persistencia, esquema y consultas seguras | 20% |
| Organización en módulos, legibilidad y documentación | 15% |
| Pruebas, demostración y explicación del trabajo | 15% |

## Condiciones para considerar completo el sistema

- Una solicitud creada sigue apareciendo después de reiniciar el programa.
- Los datos inválidos y los identificadores inexistentes se manejan con mensajes comprensibles.
- Las operaciones de actualización y eliminación afectan solo al registro seleccionado.
- El reporte respeta los filtros y el archivo exportado puede abrirse y leerse.
- El programa puede ejecutarse siguiendo únicamente las instrucciones entregadas.

## Material de apoyo

- [Actividad de integración de semana 14](actividad_clase.md)
- [Tarea evaluada de semana 15](tarea_evaluada.md)
- [Ejemplo de estructura inicial](ejemplo_estructura/)
