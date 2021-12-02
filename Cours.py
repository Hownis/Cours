import random

releve = [(10, 20), (11, 21), (8, 17), (6, 18), (7, 15), (10, 14), (12, 17)]

#Truc du cours

def moyenne_releve(releve):
  for i in range(len(releve)):
    releve[i] = random.randint(0, 100), random.randint(0, 100)
  moyennes = [0] * len(releve)
  for i in range(len(releve)):
    tmin, tmax = releve[i]
    moyennes[i] = (tmin + tmax) / 2
    #moyennes[i] = int(moyennes[i])
  return moyennes

print(moyenne_releve(releve))

#Exercice 1

def milieu(tupleun, tupledeux):
  xun, yun = tupleun
  xtrois, ydeux = tupledeux
  rep = [((xun + xtrois)/2), ((yun + ydeux)/2)]
  return rep

tupleun = [(5), (3)]
tupledeux = [(2), (6)]

print(milieu(tupleun, tupledeux))

#Exercice 2/a

def anterieur(un, deux):
  jourun, moisun, anneun = un
  jourdeux, moisdeux, annedeux = deux

  if anneun > annedeux:
    if moisun > moisdeux:
      if jourun > jourdeux:
        print("supérieur")
  else:
    print("inférieur")

un = [(12), (5), (2018)]
deux = [(10), (0), (2019)]

anterieur(un, deux)

#Exercice 2/b

def difanne(aun):
  ageun, agedeux = aun[0]

  if ageun > agedeux:
    rep = int(ageun - agedeux)
  else:
    rep = int(agedeux - ageun)

  return rep

age = [(4, 13)]

print(difanne(age))