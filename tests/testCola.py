from collections import deque

cola = deque()
cola.append("selenis")
print(cola)
cola.append("wendy")
print(cola)
cola.append("vanessa")
print(cola)

print("Se supone que se quita lo primero que ingreso <selenis> ")
cola.popleft()
print(cola)


print("Se agrega uno nuevo")
cola.append("xxx")
print(cola)

print("Se supone que se quita lo primero que ingreso <wendy> ")
cola.popleft()
print(cola)
