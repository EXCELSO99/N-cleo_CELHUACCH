# motor_piso_fractal.py
# Módulo central de cálculo fractal - Nucleo Recursivo CELHUACCH

def calcular_mandelbrot(c, max_iter=100):
    """Evalúa la divergencia de un número complejo c en el plano."""
    z = 0.0j
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return max_iter

def renderizar_matriz_ascii(ancho=40, alto=20, x_lim=(-2.0, 0.5), y_lim=(-1.25, 1.25), max_iter=30):
    """Construye una representación matricial en caracteres del fractal."""
    paleta = " .:-=+*#%@"
    lienzo = []
    
    x_min, x_max = x_lim
    y_min, y_max = y_lim
    
    for fila in range(alto):
        linea = ""
        y = y_max - (fila / (alto - 1)) * (y_max - y_min)
        for col in range(ancho):
            x = x_min + (col / (ancho - 1)) * (x_max - x_min)
            iteraciones = calcular_mandelbrot(complex(x, y), max_iter)
            
            indice = int((iteraciones / max_iter) * (len(paleta) - 1))
            linea += paleta[indice]
        lienzo.append(linea)
        
    return "\n".join(lienzo)
