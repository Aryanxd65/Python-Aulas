import os
os.system("cls || clean")

meta_horas = float(input("Digite a meta de horas para estudar: "))

horas_usadas = 0

while horas_usadas <= meta_horas:
        gasto_h_diarias = float(input("Digite quantas hrs foram gastas: "))

        horas_usadas += gasto_h_diarias

        if horas_usadas > meta_horas:
            break
                              
        print(f"Total de horas gastas até agr:  {horas_usadas}")


excedente = horas_usadas - meta_horas

print(f"Total gasto de hrs:{horas_usadas}")
print(f"Horas excedidas: {excedente}")