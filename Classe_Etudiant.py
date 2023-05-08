class Etudiant: # Revision projet Etudiant
    """
    Classe Etudiant
    """
    # Attribut de classe
    nbEtudiants = 0
    list_Etudiants = []

    def __init__(self, pNumEtud : str = "", pNom : str = "", pPrenom : str = "", pAge : int = 0, pSurnom : str = ""):
        """
        Constructeur de la classe Etudiant
        :param pNumEtud: Numéro de l'étudiant
        :param pNom: Nom de l'étudiant
        :param pPrenom: Prénom de l'étudiant
        :param pAge: Âge de l'étudiant
        :param pSurnom:
        """
        # Attributs d'instance
        self._num_etud = pNumEtud # Privé
        self._nom = pNom # Privé
        self._prenom = pPrenom # Privé
        self._age = pAge # Privé
        self.Surnom = pSurnom # Public
        # Incrémenter l'attribut de classe qui permet de calculer le nombre d'étudiants
        Etudiant.nbEtudiants += 1
        Etudiant.list_Etudiants.append(self)

    # Propriétés

    # Propriété NumEtud
    # On ne peut afficher que les trois premier caractères
    def _get_num_etud(self):
        return self._num_etud[0:3]
    def _set_num_etud(self, v_num):
        if len(v_num) == 5 and v_num[0].isalpha() and v_num[1] == "-" and v_num[2:5].isnumeric():
            self._num_etud = v_num
    NumEtud = property(_get_num_etud, _set_num_etud)

    # Propriété Nom
    def _get_nom(self):
        """
        Getter de la propriété Nom
        :return: L'initial du nom
        """
        return self._nom[0].capitalize()
    def _set_nom(self, v_nom):
        if len(v_nom) and v_nom.isalpha() :
            self._nom = v_nom

    Nom = property(_get_nom, _set_nom)

    # Méthode magique str
    def __str__(self):
        """
        Retourne la chaine qui représente l'objet instancié
        :return: L'objet Etudiant
        """
        chaine = "L'âge de l'étudiant est : "+ str(self._age) + self._nom+\
                 "Les initiales de l'étudiant: " + self._RetournerInitiale()

        return chaine

    # Méthode d'instace (exige un self)
    def _RetournerInitiale(self):
        return self._nom[0].capitalize() + "." + self._prenom[0].capitalize()

    def CalculerDecennie(self):
        if int(self._age/10) == 2 :
            return "Jeune"
        else :
            return "Agé"
