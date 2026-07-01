# Calculadora de Áreas 📐

Programa desarrollado en Python que permite calcular el área de diferentes figuras geométricas mediante un menú interactivo en la consola.

## Descripción

El usuario selecciona una figura geométrica, ingresa las medidas solicitadas y el programa calcula automáticamente su área utilizando la fórmula correspondiente.

## Figuras disponibles

- ⬜ Cuadrado
- ▭ Rectángulo
- 🔺 Triángulo
- ⚪ Círculo

## Tecnologías

- Python 3
- Módulo estándar `math`

## Cómo ejecutar

1. Clona este repositorio o descarga el archivo.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python calculadora_area.py
```

## Ejemplo de uso

```text
=======================
Calculadora de área 📐
=======================

1. Cuadrado
2. Rectángulo
3. Triángulo
4. Círculo

Figura: 4

Radio: 5

El área del círculo es: 78.53981633974483
```

## Lo que practiqué

Durante este proyecto practiqué:

- Entrada de datos con `input()`
- Conversión de tipos (`int` y `float`)
- Condicionales (`if`, `elif`, `else`)
- Operadores aritméticos
- Uso del módulo `math`
- Interacción con el usuario mediante un menú

### Próximas mejoras (Para practicar Python)

* **Validar que las medidas ingresadas sean positivas:** Evitar que el programa procese números negativos o cero en las dimensiones.
* **Permitir realizar varios cálculos sin reiniciar el programa:** Implementar un bucle para que el usuario pueda calcular varias áreas en la misma sesión.
* **Redondear los resultados:** Limitar la cantidad de decimales en la salida para que los resultados (como el del círculo) se vean más limpios.
* **Organizar el código utilizando funciones:** Migrar la lógica actual a funciones estructuradas para mejorar la legibilidad y modularidad.

## Estado del proyecto

Proyecto finalizado como práctica de Python básico.
