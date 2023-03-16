def fibonacci(n):
    """Retorna los primeros n números de la secuencia de Fibonacci"""
    fibo_seq = [0, 1]
    "Generamos la secuencia de Fibonacci añadiendo elementos a la lista fibo_seq mientras su longitud sea menor que n. En cada iteración, añadimos el elemento que es la suma del último elemento (fibo_seq[-1]) y el penúltimo elemento (fibo_seq[-2])."
    while len(fibo_seq) < n:
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
    return fibo_seq

# Llamamos a la función y mostramos los resultados por consola
n = 10
fibo_seq = fibonacci(n)
print(f"Los primeros {n} números de la secuencia de Fibonacci son: {fibo_seq}")
