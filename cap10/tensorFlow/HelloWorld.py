import tensorflow as tf

helloWorld = tf.constant("Hello World com TensorFlow")
print(helloWorld)

# Operações Matemáticas
tensorNumero1 = tf.constant(10)
tensorNumero2 = tf.constant(5)

print(f"A Adição deu = {tensorNumero1 + tensorNumero2}")                        # Adição
print(f"A Subtração deu = {tf.subtract(tensorNumero1, tensorNumero2)}")         # Subtração
print(f"A Divisão deu = {tf.math.truediv(tensorNumero1, tensorNumero2)}")       # Divisão
print(f"A Multiplição deu = {tf.math.multiply(tensorNumero1, tensorNumero2)}")  # Multiplicação
