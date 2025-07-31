#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
def verificar_instalacion():
    """
    Verifica si las librerías de ciencia de datos y Streamlit están instaladas.
    """
    librerias_a_revisar = [
        "pandas",
        "matplotlib",
        "numpy",
        "seaborn",
        "scipy",
        "streamlit"
    ]
    
    print("🔎 Verificando la instalación de librerías...")
    print("-" * 40)
    
    todo_correcto = True
    
    for lib in librerias_a_revisar:
        try:
            __import__(lib)
            print(f"✅  La librería '{lib}' está instalada correctamente.")
        except ImportError:
            print(f"❌  ERROR: La librería '{lib}' no se encuentra instalada.")
            print(f"   -> Sugerencia de instalación: pip install {lib}")
            todo_correcto = False
            
    print("-" * 40)
    
    if todo_correcto:
        print("🎉 ¡Excelente! Todas las librerías están listas para ser usadas.")
    else:
        print("Algunas librerías no fueron encontradas. Por favor, instálalas.")

if __name__ == "__main__":
    verificar_instalacion()