import subprocess

with open('binario.py', 'r', encoding='utf-8') as f:
    codigo_original = f.read()

codigo_mutado = codigo_original.replace('elif lista[mitad] < objetivo:', 'elif lista[mitad] <= objetivo:')

try:
    with open('binario.py', 'w', encoding='utf-8') as f:
        f.write(codigo_mutado)
    
    print("\nEjecutando prueba de mutación...")
    
    resultado = subprocess.run(['python', '-m', 'pytest', 'test_binario.py', '-q'], capture_output=True, text=True)
  
    print("-" * 50)
    if resultado.returncode == 0:
        print(" EL MUTANTE SOBREVIVIÓ.")
        print("Tus pruebas en 'test_binario.py' PASARON a pesar de que el código estaba roto.")
        print("Conclusión: Necesitas agregar un test más estricto (ej. probar con números repetidos).")
    else:
        print("EL MUTANTE MURIÓ.")
        print("Tus pruebas detectaron el error y fallaron correctamente.")
        print("Conclusión: Tu test_binario.py es de buena calidad.")
    print("-" * 50)

finally:
    with open('binario.py', 'w', encoding='utf-8') as f:
        f.write(codigo_original)
    print("\nTu archivo 'binario.py' ha sido restaurado a la normalidad.\n")