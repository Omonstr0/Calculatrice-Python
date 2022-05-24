print("\n###############.\tBienvenue sur votre calculatrice.\t###############\n")


def menu():
  print("\n1. Addition: a + b.")
  print("2. Soustraction: a - b.")
  print("3. Division: a / b.")
  print("4. Multiplication: a * b.")
  print("5. Quitter le programme.\n")

while True:
  menu()

  user_choice = input("Entrer le type de calcul que vous souhaitez effectuer: ")
  while user_choice.isdigit() == False or int(user_choice) <= 0 or int(user_choice) > 5:
    print("\nErreur")
    user_choice = input("Entrer le type de calcul que vous souhaitez effectuer: ")

  if user_choice == 5:
    print(exit())

  nb1 = input("Entrer une première valeur: ")
  nb2 = input("Entrer une deuxième valeur: ")

  if int(user_choice) == 1:
    try:
      print(f"\nL'addition entre {float(nb1)} et {float(nb2)} vaut {float(nb1) + float(nb2)}")
    except  ValueError:
      print(f"\nLe calcul demandé entre '{nb1}' et '{nb2}' est impossible.")

  elif int(user_choice) == 2:
    try:
      print(f"\nLa soustraction entre {float(nb1)} et {float(nb2)} vaut {float(nb1) - float(nb2)}")
    except ValueError:
      print(f"\nLe calcul demandé entre '{nb1}' et '{nb2}' est impossible.")

  elif int(user_choice) == 3:
    try:
      print(f"\nLa division entre {float(nb1)} et {float(nb2)} vaut {round(float(nb1) / float(nb2), 2)}")
    except ZeroDivisionError:
      print(f"\nLa division entre '{nb1}' et '{nb2}' est impossible, car division par 0")

  elif int(user_choice) == 4:
    try:
      print(f"\nLa multiplication entre {float(nb1)} et {float(nb2)} vaut {round(float(nb1) * float(nb2), 2)}")
    except ValueError:
      print(f"\nLe calcul demandé entre '{nb1}' et '{nb2}' est impossible.")


  repeat = input("Un autre calcul ?\nOui: 0\nNon: 1\nVotre saisie: ")
  while repeat.isdigit() == False or int(repeat) != 0 and int(repeat) != 1:
    print("\nValeur non valide.")
    repeat = input("Un autre calcul ?\nOui: 0\nNon: 1\nVotre saisie: ")

  if int(repeat) == 0:
    continue
  else:
    print(exit())
