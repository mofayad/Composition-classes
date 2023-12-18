from abc import ABC, abstractmethod

class Composition :
    def __init__(self, produit_elementaire, quantite):
        self.__produit_elementaire = produit_elementaire
        self.__quantite = quantite

    @property
    def Getproduit(self):
        return self.__produit_elementaire
    
    def Setproduit(self, value):
        self.__produit_elementaire = value

    @property
    def Getquantite(self):
        return self.__quantite
    
    def Setquantite(self, value):
        self.__quantite = value

class Produit(ABC):
    def __init__(self, nom, code):
        self._nom = nom
        self._code = code

    @property
    def Getnom(self):
        return self._nom
    
    def Setnom(self, value):
        self._nom = value

    @property
    def Getcode(self):
        return self._code
    
    def Setcode(self, value):
        self._code = value

    @abstractmethod
    def GetPrixHT(self):
        pass

class Produit_Elementaire(Produit):
        def __init__(self, nom, code, prixAchat):
            super().__init__(nom, code)
            self._prixAchat = prixAchat
        
        @property
        def GetprixAchat(self):
            return self._prixAchat
        
        def SetprixAchat(self, value):
            self._prixAchat = value

        def __str__(self):
            return f"{self._nom} ({self._code}) - Prix d'achat : {self._prixAchat}"

        def GetPrixHT(self):
            return self._prixAchat 
        
class Produit_Compose(Produit):
    def __init__(self, nom, code, fraisFabrication, tauxTVA):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__tauxTVA = tauxTVA
        self.__listeConstituants = []

    @property
    def GetfraisFabrication(self):
        return self.__fraisFabrication
    
    def SetfraisFabrication(self, value):
        self.__fraisFabrication = value

    @property
    def GettauxTVA(self):
        return self.__tauxTVA
    
    def SettauxTVA(self, value):
        self.__tauxTVA = value
         
    @property
    def GetlisteConstituants(self):
        return self.__listeConstituants
    
    def SetlisteConstituants(self, value):
        self.__listeConstituants = value 

    def __str__(self):
        return f"{self._nom} ({self._code}) - Frais de fabrication : {self.__fraisFabrication}%"

    def GetPrixHT(self):
        prix_total_ht = 0
        for constituant in self.__listeConstituants:
            prix_total_ht += constituant.Getproduit.GetPrixHT() * constituant.Getquantite

        return prix_total_ht + (prix_total_ht * self.GetfraisFabrication / 100)

# Test
if __name__ == "__main__":
    # Création de produits élémentaires
    p1 = Produit_Elementaire("P1", "001", 10.0)
    p2 = Produit_Elementaire("P2", "002", 20.0)

    # Création de produits composés
    p3 = Produit_Compose("P3", "003", 5.0, 18)
    p3.GetlisteConstituants.append(Composition(p1, 2))
    p3.GetlisteConstituants.append(Composition(p2, 4))

    p4 = Produit_Compose("P4", "004", 8.0, 18)
    p4.GetlisteConstituants.append(Composition(p2, 3))
    p4.GetlisteConstituants.append(Composition(p1, 2))

    # Affichage des informations
    print(p1)
    print(p2)
    print(p3)
    print(p4)

    # Calcul et affichage des prix hors taxe
    print(f"Prix HT P1 : {p1.GetPrixHT()}")
    print(f"Prix HT P2 : {p2.GetPrixHT()}")
    print(f"Prix HT P3 : {p3.GetPrixHT()}")
    print(f"Prix HT P4 : {p4.GetPrixHT()}")
