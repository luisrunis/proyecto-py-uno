import operaciones

x = operaciones.Calcular(9,5)

def run():
  print(x.suma())
  print(x.resta())
  input('Presione enter para salir')

if __name__ == '__main__':
    run()
