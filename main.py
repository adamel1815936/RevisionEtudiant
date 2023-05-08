from Classe_Etudiant import *
# Première instance de la classe Etudiant
E1 = Etudiant()
E1.Surnom = "Has"

Etudiant.nbEtudiants+=1
# Deuxième instance de la classe Etudiant
E2 = Etudiant()
Etudiant.nbEtudiants+=1
Etudiant.list_Etudiants.append(E2)
