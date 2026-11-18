# demo.py
# Script de demostración para probar el motor fractal desde el móvil

from motor_piso_fractal import renderizar_matriz_ascii

def ejecutar_prueba():
    print("=== INICIANDO PRUEBA DEL MOTOR FRACTAL ===")
    
    # Genera una vista compacta ideal para pantalla de celular
    resultado = renderizar_matriz_ascii(ancho=45, alto=20, max_iter=30)
    print(resultado)
    
    print("=== PRUEBA FINALIZADA CON ÉXITO ===")

if __name__ == "__main__":
    ejecutar_prueba()
