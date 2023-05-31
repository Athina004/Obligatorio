from metodos.menu import *

def main():
    op = 0
    print('\033[1m' + "Menú principal:" + "\033[0m")
    
    while op!=6:
       menu()
       p = int(input("Seleccion la opcion del menu: "))
       
       if op == 1:
           AltaEmpleado()
           
       if op == 2:
           AltaSector()
           
       if op == 3:
           asignar_empleado_a_sector()
           
       if op == 4:
           otorgar_puntos_a_sector()
           
       if op == 5:
           realizar_consultas()
           
       if op == 6:
           return
           
main()
