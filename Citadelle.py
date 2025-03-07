from random import choice

import random

class Roles:
    
    def __init__(self, Role, Player, caracteristique, Couleur):
        
        self.Role = Role
        
        self.Player = Player
        
        self.caracteristique = caracteristique
        
        self.Couleur = Couleur
        
class Quartiers:
    
    def __init__(self, Carte, Valeur, Couleur):
        
        self.Carte = Carte
        
        self.Valeur = Valeur
        
        self.Couleur = Couleur

def Quartiers_():
    
    ListeQuartiers = ()
    
    Temple = Quartiers("Temple", 1, "Bleu")
    
    ListeQuartiers += ("Temple",)
    
    Cathedrale = Quartiers("Cathedrale", 5, "Bleu")
    
    ListeQuartiers += ("Cathedrale",)
    
    Eglise = Quartiers("Eglise", 2, "Bleu")
    
    ListeQuartiers += ("Eglise",)
    
    Monastere = Quartiers("Monastere", 3, "Bleu")
    
    ListeQuartiers += ("Monastere",)
    
    Chateau = Quartiers("Chateau", 4, "Jaune")
    
    ListeQuartiers += ("Chateau",)
    
    Manoir = Quartiers("Manoir", 3, "Jaune")
    
    ListeQuartiers += ("Manoir",)
    
    Palais = Quartiers("Palais", 5, "Jaune")
    
    ListeQuartiers += ("Palais",)
    
    Caserne = Quartiers("Caserne", 3, "Rouge")
    
    ListeQuartiers += ("Caserne",)
    
    Forteresse = Quartiers("Forteresse", 5, "Rouge")
    
    ListeQuartiers += ("Forteresse",)
    
    Tour_de_guet = Quartiers("Tour_de_guet", 1, "Rouge")
    
    ListeQuartiers += ("Tour_de_guet",)
    
    Prison = Quartiers("Prison", 2, "Rouge")
    
    ListeQuartiers += ("Prison",)
    
    Comptoir = Quartiers("Comptoir", 3, "Vert")
    
    ListeQuartiers += ("Comptoir",)
    
    Echoppe = Quartiers("Echoppe", 2, "Vert")
    
    ListeQuartiers += ("Echoppe",)
    
    Marche = Quartiers("Marche", 2, "Vert")
    
    ListeQuartiers += ("Marche",)
    
    Hotel_de_ville = Quartiers("Hotel_de_ville", 5, "Vert")
    
    ListeQuartiers += ("Hotel_de_ville",)
    
    Port = Quartiers("Port", 4, "Vert")
    
    ListeQuartiers += ("Port",)
    
    Taverne = Quartiers("Taverne", 1, "Vert")
    
    ListeQuartiers += ("Taverne",)
    
    print(Taverne.__dict__)
    
    return(ListeQuartiers)
    
print(Quartiers_())

liste = ["Voleur", "Condottiere", "Architecte", "Roi", "Assassin", "Eveque", "Magicien", "Marchand"]
    
for _ in range(1):
    
    for _ in range(2):
        
        rdm = random.randint(0, len(liste) - 1)
        
        print(liste[rdm])
        
        liste.pop(rdm)
        
    rdm = random.randint(0, len(liste) - 1)
    
    liste.pop(rdm)
    
    print("UNE CARTE CACHEE A ETE ENLEVEE")
    
    print(liste)
    
    for _ in range(5):
    
        Joueur = input("ROLE JOUEUR:")
        
        Player = input("NOM:")
        
        match Joueur:
            
            case "Voleur":
            
                Voleur = Roles("Voleur", Player, "Vous annoncez quel autre personnage vous volez. Lorsque le joueur qui a ce personnage sera appelé et se révèlera, vous lui prendrez toutes ses pièces d’or. Le Voleur ne peut voler ni l’Assassin, ni le personnage assassiné.", "None")
            
                print(Voleur.__dict__)
        
            case "Condottiere":
                
                Condottiere = Roles("Condottiere", Player, "Vous recevez une pièce d’or par quartier soldatesque (rouge) dans votre cité. À la fin de votre tour, vous pouvez attaquer une cité pour y détruire un quartier de votre choix. Vous pouvez détruire gratuitement un quartier de coût 1, ou pouvez détruire un quartier de coût plus élevé en payant le coût de ce quartier moins un (1 pièce d’or pour un quartier en coûtant 2 à construire, 2 pièces d’or pour un quartier en coûtant 3, etc…). Le Condottiere peut éventuellement attaquer sa propre cité. Le Condottiere ne peut attaquer une cité déjà terminée, avec ses huit quartiers.", "Rouge")
            
                print(Condottiere.__dict__)
                
            case "Roi":
            
                Roi = Roles("Roi", Player, "Vous recevez une pièce d’or par quartier noble (jaune) dans votre cité*. Vous prenez immédiatement la carte Couronne. C’est désormais vous qui appellerez les personnages et, au tour suivant, vous choisirez votre personnage en premier. Si aucun joueur n’a choisi le Roi, le roi précédent conserve la couronne. Si le Roi est assassiné, il passe son tour comme n’importe quel personnage. Néanmoins, après que tous les autres joueurs ont joué, lorsqu’il annonce qu’il était Roi et a été assassiné, il prend la carte couronne. Ce sera donc lui qui choisira son personnage en premier au tour suivant", "Jaune")
            
                print(Roi.__dict__)
        
            case "Marchand":
                
                Marchand = Roles("Marchand", Player, "Vous recevez au début de votre tour une pièce d’or supplémentaire – vous pouvez donc prendre soit trois pièces d’or, soit une carte et une pièce d’or. Vous recevez en outre une pièce d’or par quartier commerçant (vert) dans votre cité*.", "Vert")
            
                print(Marchand.__dict__)
                
            case "Eveque":
            
                Eveque = Roles("Eveque", Player, "Vous recevez une pièce d’or par quartier religieux (bleu) dans votre cité. Vous ne pouvez pas être attaqué par le Condottiere.", "Bleu")
            
                print(Eveque.__dict__)
        
            case "Architecte":
                
                Architecte = Roles("Architecte", Player, "Au début de votre tour, vous piochez deux cartes Quartiers supplémentaires – vous pouvez donc prendre en tout trois cartes, ou deux cartes et deux pièces d’or. Vous pouvez en outre bâtir jusqu’à trois quartiers durant votre tour.", "None")
            
                print(Architecte.__dict__)
                
            case "Magicien":
            
                Magicien = Roles("Magicien", Player, "À n’importe quel moment de votre tour*, vous pouvez, au choix : soit échanger toutes les cartes de votre main (pas celles de votre cité !) contre toutes les cartes de la main d’un autre joueur (vous pouvez faire cela même si vous n’avez pas de carte en main, et vous prenez alors les cartes de l’autre joueur). soit vous défausser d’un certain nombre de cartes de votre main, les placer sous la pioche, et piocher le même nombre de cartes en échange.", "None")
            
                print(Magicien.__dict__)
        
            case "Assassin":
                
                Assassin = Roles("Assassin", Player, "Vous annoncez quel autre personnage vous assassinez. Le joueur qui a ce personnage ne doit pas réagir, et ne se déclarera pas non plus lorsque son personnage sera appelé. Il ne révèlera sa carte qu’en dernier, pour annoncer qu’il avait été assassiné et qu’il a donc passé sont tour.", "None")
            
                print(Assassin.__dict__)
                
            case _:
                
                print("WRONG INPUT")