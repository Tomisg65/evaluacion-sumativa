cat << 'EOF' > suma.py
def sumar(a, b):
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")
    return resultado

sumar(5, 3)
EOF
