from math import log
from noeud_cont import NoeudDeDecision_cont

class ID3_cont:
    """ Algorithme ID3. 
        This is an updated version from the one in the book (Intelligence Artificielle par la pratique).
        Specifically, in construit_arbre_recur(), if donnees == [] (line 70), it returns a terminal node with the predominant class of the dataset -- as computed in construit_arbre() -- instead of returning None.
        Moreover, the predominant class is also passed as a parameter to NoeudDeDecision().
        difference par rapport a la version non modifiee: les valeurs des attributs sont continues, un noeud divise avec un attribut et une valeur particuliere
    """
    
    def construit_arbre(self, donnees):
        """ Construit un arbre de décision à partir des données d'apprentissage.
            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """
        
        # Nous devons extraire les domaines de valeur des 
        # attributs, puisqu'ils sont nécessaires pour 
        # construire l'arbre.
        attributs = {}
        for donnee in donnees:
            for attribut, valeur in donnee[1].items():
                valeurs = attributs.get(attribut)
                if valeurs is None:
                    valeurs = set()
                    attributs[attribut] = valeurs
                valeurs.add(float(valeur))
        # Find the predominant class
        classes = set([row[0] for row in donnees])
        predominant_class_counter = -1
        for c in classes:
            if [row[0] for row in donnees].count(c) >= predominant_class_counter:
                predominant_class_counter = [row[0] for row in donnees].count(c)
                predominant_class = c
            
        arbre = self.construit_arbre_recur(donnees, attributs, predominant_class)

        return arbre

    def construit_arbre_recur(self, donnees, attributs, predominant_class):
        """ Construit récurcivement un arbre de décision à partir 
            des données d'apprentissage et d'un dictionnaire liant
            les attributs à la liste de leurs valeurs possibles.
            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :param attributs: un dictionnaire qui associe chaque\
            attribut A à son domaine de valeurs a_j.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """
        def classe_unique(donnees):
            """ Vérifie que toutes les données appartiennent à la même classe. """
            
            if len(donnees) == 0:
                return True 
            premiere_classe = donnees[0][0]
            for donnee in donnees:
                if donnee[0] != premiere_classe:
                    return False 
            return True

        if donnees == []:
            return NoeudDeDecision_cont(None, [str(predominant_class), dict()], str(predominant_class))

        elif classe_unique(donnees):
            return NoeudDeDecision_cont(None, donnees, str(predominant_class))
            
        else:
            min_attr, part_val = self.find_min_entr(donnees,attributs)
            
            new_attr_gauche = attributs.copy()
            new_attr_droite = attributs.copy()

            partitions = self.partitionne(donnees, min_attr, part_val)
            enfants = {}

            newdroite = set()
            newgauche =set()
            for x in attributs[min_attr]:
                    if (x >= part_val):
                        newdroite.add(x)
                    else:
                        newgauche.add(x)
            
            new_attr_gauche[min_attr] =newgauche
            new_attr_droite[min_attr] = newdroite

            enfants["droite"] = self.construit_arbre_recur(partitions["droite"],new_attr_droite,predominant_class)
            enfants["gauche"] = self.construit_arbre_recur(partitions["gauche"],new_attr_gauche,predominant_class)
            return NoeudDeDecision_cont(min_attr, donnees, str(predominant_class), enfants,part_val)

    def partitionne(self, donnees, attribut, val_part):
        """ Partitionne les données sur les valeurs a_j de l'attribut A.
            :param list donnees: les données à partitioner.
            :param attribut: l'attribut A de partitionnement.
            :param list valeurs: les valeurs a_j de l'attribut A.
            :return: un dictionnaire qui associe à chaque valeur a_j de\
            l'attribut A une liste l_j contenant les données pour lesquelles A\
            vaut a_j.
        """
        partitions = dict()

        
        for donnee in donnees:
            where =""
            if float(donnee[1][attribut]) < val_part:
                where ="gauche"
            else :
                where ="droite"

            if partitions.get(where)== None:
                partitions[where] = list()

            partitions[where].append(donnee)

        return partitions

    def p_ci_aj(self, donnees, attribut, part_val, classe, where = "droite"):
        """ p(c_i|a_j) - la probabilité conditionnelle que la classe C soit c_i\
            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur: la valeur a_j de l'attribut A.
            :param classe: la valeur c_i de la classe C.
            :return: p(c_i | a_j)
        """
        # Nombre d'occurrences de la valeur a_j parmi les données.
        d_j = list()
        if where =="droite":
            for d in donnees:
                if float(d[1][attribut])>= part_val:
                    d_j.append(d)
        else:
            for d in donnees:
                if float(d[1][attribut]) < part_val:
                    d_j.append(d)

        
        # Permet d'éviter les divisions par 0.
        if not d_j :
            return 0
        
        donnees_ci = [donnee for donnee in d_j if donnee[0] == classe]

        # p(c_i|a_j) = nombre d'occurrences de la classe c_i parmi les données 
        #              pour lesquelles A vaut a_j /
        #              nombre d'occurrences de la valeur a_j parmi les données.
        return float(len(donnees_ci) / len(d_j))

    def h_C_aj(self, donnees, attribut, valeur_de_partition, where = "droite"):
        """ l'entropie de la classe parmi les données pour lesquelles\
            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur_de_partition: la valeur de partition pour l'attribut A.
        """
        # Les classes attestées dans les exemples.
        classes = list(set([donnee[0] for donnee in donnees]))
        
        # Calcule p(c_i|a_j) pour chaque classe c_i.

        p_ci_ajs = [self.p_ci_aj(donnees, attribut, valeur_de_partition, classe, where)
                    for classe in classes]

        # Si p vaut 0 -> plog(p) vaut 0.
        return -sum([p_ci_aj * log(p_ci_aj, 2.0) 
                    for p_ci_aj in p_ci_ajs 
                    if p_ci_aj != 0])

    def h_C_A(self, donnees, attribut, part_val):
        """ H(C|A) - l'entropie de la classe après avoir choisi de partitionner\
            les données suivant les valeurs de l'attribut A.
            
            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param list valeur_de_partition: la valeur de l'attribut A selon laquelle on divise.
            :return: H(C|A)
        """
        
        
        prob_less = 0
        
        for donnee in donnees:
            if float(donnee[1][attribut]) < part_val:
                prob_less += 1/len(donnees)

        p = [prob_less, 1-prob_less]

        h_more = self.h_C_aj(donnees, attribut, part_val)
        h_less = self.h_C_aj(donnees, attribut, part_val, where="gauche")
        h = [ h_less,h_more]

        return sum([p_a * h_a for p_a, h_a in zip(p, h)])

    def range_of_attr(self,donnees,attributs,attribut):
        return range(int(min(attributs[attribut])), int(max(attributs[attribut])))
   
    def find_min_entr(self,donnees,attributs):
        min_entr = 1e6
        min_attr = " "
        min_val =1
        for a in attributs.keys():
            for v in self.range_of_attr(donnees,attributs,a):
                entr = self.h_C_A(donnees,a,v)
                if min_entr > entr:
                    min_entr=entr
                    min_attr =a
                    min_val = v

        return min_attr,min_val





