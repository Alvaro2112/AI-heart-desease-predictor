class NoeudDeDecision_cont:
    """ Un noeud dans un arbre de décision. 
    
        This is an updated version from the one in the book (Intelligence Artificielle par la pratique).
        Specifically, if we can not classify a data point, we return the predominant class (see lines 53 - 56). 
    """

    def __init__(self, attribut, donnees, p_class, enfants=None, part_val=None):
        """
            :param attribut: l'attribut de partitionnement du noeud (``None`` si\
            le noeud est un noeud terminal).
            :param list donnees: la liste des données qui tombent dans la\
            sous-classification du noeud.
            :param enfants: un dictionnaire associant un fils (sous-noeud) à\
            chaque valeur de l'attribut du noeud (``None`` si le\
            noeud est terminal).
        """

        self.attribut = attribut
        self.donnees = donnees
        self.enfants = enfants
        self.p_class = p_class
        self.part_val = part_val

    def terminal(self):
        """ Vérifie si le noeud courant est terminal. """

        return self.enfants is None

    def classe(self):
        """ Si le noeud est terminal, retourne la classe des données qui\
            tombent dans la sous-classification (dans ce cas, toutes les\
            données font partie de la même classe. 
        """

        if self.terminal():
            return self.donnees[0][0]

    def classifie(self, donnee):
        """ Classifie une donnée à l'aide de l'arbre de décision duquel le noeud\
            courant est la racine.

            :param donnee: la donnée à classifier.
            :return: la classe de la donnée selon le noeud de décision courant.
        """
        if self.terminal():
            return self.classe()
        else:
            valeur = donnee[self.attribut]
            child = None
            if float(valeur) >= self.part_val:
                child = self.enfants["droite"]
            else:
                child = self.enfants["gauche"]
            try:
                return child.classifie(donnee)
            except:
                return self.p_class

    def repr_arbre(self, level=0):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine. 
        """

        rep = ''
        if self.terminal():
            rep += '---' * level
            rep += 'Alors {}\n'.format(self.classe())
            rep += '---' * level
            rep += '\n'

        else:
            rep += '---' * level
            rep += 'Si {} est  < que  {}: \n'.format(self.attribut, self.part_val)
            rep += self.enfants["gauche"].repr_arbre(level + 1)
            rep += '---' * level
            rep += 'Si {} est >= que  {}: \n'.format(self.attribut, self.part_val)
            rep += self.enfants["droite"].repr_arbre(level + 1)

        return rep

    def __repr__(self):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine. 
        """
        return str(self.repr_arbre(level=0))
