tempetature = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#Vytvořte seznam průměrných teplot pro každý den
average = [round(sum(y)) for y in tempetature]
print(f"Seznam průměrných teplot pro každý den: {average}")

#Vytvořte seznam ranních teplot
morning_temperature = [x[0] for x in tempetature]
print(f"Seznam ranních teplot: {morning_temperature}")

#Vytvořte seznam nočních teplot
night_temperature = [z[3] for z in tempetature]
print(f"Seznam nočních teplot: {night_temperature}")

#Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
afternoon_and_night_temperature = [(q[1], q[3]) for q in tempetature]
print(f"Seznam obsahující polední a noční teplotu: {afternoon_and_night_temperature}")
