import numpy as np

# Definir la matriz a (las proporciones de cada material desde cada cantera)
a = np.array([[52, 30, 18],
              [20, 50, 30],
              [25, 20, 55]])

# Definir el vector de requisitos de materiales [arena, grano fino, grano grueso]
b = np.array([4800, 5810, 5690])

# Resolver para x (la cantidad de material que se debe transportar desde cada cantera)
x = np.linalg.solve(a, b)

# Mostrar los resultados
print(f"Cantidad a transportar desde la Cantera 1: {x[0]:.2f} metros cúbicos")
print(f"Cantidad a transportar desde la Cantera 2: {x[1]:.2f} metros cúbicos")
print(f"Cantidad a transportar desde la Cantera 3: {x[2]:.2f} metros cúbicos")
