from random import choice

import random

class Roles:
    
    def __init__(self, Role, caracteristique, Couleur):
        
        self.Role = Role
        
        self.caracteristique = caracteristique
        
        self.Couleur = Couleur
        
class Quartiers:
    
    def __init__(self, Carte, Valeur, Couleur):
        
        self.Carte = Carte
        
        self.Valeur = Valeur
        
        self.Couleur = Couleur
        
class Joueurs:
    
    def __init__(self, Role, Player, Quartiers, Pieces, Main):
        
        self.Role = Role
        
        self.Player = Player
        
        self.Quartiers = Quartiers
        
        self.Pieces = Pieces
        
        self.Main = Main

def Quartiers_():
    
    global TupleQuartiers
    
    TupleQuartiers = ()
    
    Temple = Quartiers("Temple", 1, "Bleu")
    
    TupleQuartiers += ("Temple",)
    
    Cathedrale = Quartiers("Cathedrale", 5, "Bleu")
    
    TupleQuartiers += ("Cathedrale",)
    
    Eglise = Quartiers("Eglise", 2, "Bleu")
    
    TupleQuartiers += ("Eglise",)
    
    Monastere = Quartiers("Monastere", 3, "Bleu")
    
    TupleQuartiers += ("Monastere",)
    
    Chateau = Quartiers("Chateau", 4, "Jaune")
    
    TupleQuartiers += ("Chateau",)
    
    Manoir = Quartiers("Manoir", 3, "Jaune")
    
    TupleQuartiers += ("Manoir",)
    
    Palais = Quartiers("Palais", 5, "Jaune")
    
    TupleQuartiers += ("Palais",)
    
    Caserne = Quartiers("Caserne", 3, "Rouge")
    
    TupleQuartiers += ("Caserne",)
    
    Forteresse = Quartiers("Forteresse", 5, "Rouge")
    
    TupleQuartiers += ("Forteresse",)
    
    Tour_de_guet = Quartiers("Tour_de_guet", 1, "Rouge")
    
    TupleQuartiers += ("Tour_de_guet",)
    
    Prison = Quartiers("Prison", 2, "Rouge")
    
    TupleQuartiers += ("Prison",)
    
    Comptoir = Quartiers("Comptoir", 3, "Vert")
    
    TupleQuartiers += ("Comptoir",)
    
    Echoppe = Quartiers("Echoppe", 2, "Vert")
    
    TupleQuartiers += ("Echoppe",)
    
    Marche = Quartiers("Marche", 2, "Vert")
    
    TupleQuartiers += ("Marche",)
    
    Hotel_de_ville = Quartiers("Hotel_de_ville", 5, "Vert")
    
    TupleQuartiers += ("Hotel_de_ville",)
    
    Port = Quartiers("Port", 4, "Vert")
    
    TupleQuartiers += ("Port",)
    
    Taverne = Quartiers("Taverne", 1, "Vert")
    
    TupleQuartiers += ("Taverne",)
    
    print(Taverne.__dict__)
    
    return(TupleQuartiers)
    
print(Quartiers_())

global Pieces

Pieces = 2

def CreerJoueurs():
    
    def MajRoles():
        
        global liste

        liste = ["Voleur", "Condottiere", "Architecte", "Roi", "Assassin", "Eveque", "Magicien", "Marchand"]
        
        for _ in range(2):
            
            rdm = random.randint(0, len(liste) - 1)
            
            print(liste[rdm])
            
            liste.pop(rdm)
            
        rdm = random.randint(0, len(liste) - 1)
        
        liste.pop(rdm)
        
        print("UNE CARTE CACHEE A ETE ENLEVEE")
        
        print(liste)
            
    print(MajRoles())
    
    Voleur = Roles("Voleur", "Vous annoncez quel autre personnage vous volez. Lorsque le joueur qui a ce personnage sera appelé et se révèlera, vous lui prendrez toutes ses pièces d’or. Le Voleur ne peut voler ni l’Assassin, ni le personnage assassiné.", "None")
    
    Condottiere = Roles("Condottiere", "Vous recevez une pièce d’or par quartier soldatesque (rouge) dans votre cité. À la fin de votre tour, vous pouvez attaquer une cité pour y détruire un quartier de votre choix. Vous pouvez détruire gratuitement un quartier de coût 1, ou pouvez détruire un quartier de coût plus élevé en payant le coût de ce quartier moins un (1 pièce d’or pour un quartier en coûtant 2 à construire, 2 pièces d’or pour un quartier en coûtant 3, etc…). Le Condottiere peut éventuellement attaquer sa propre cité. Le Condottiere ne peut attaquer une cité déjà terminée, avec ses huit quartiers.", "Rouge")
    
    Roi = Roles("Roi", "Vous recevez une pièce d’or par quartier noble (jaune) dans votre cité*. Vous prenez immédiatement la carte Couronne. C’est désormais vous qui appellerez les personnages et, au tour suivant, vous choisirez votre personnage en premier. Si aucun joueur n’a choisi le Roi, le roi précédent conserve la couronne. Si le Roi est assassiné, il passe son tour comme n’importe quel personnage. Néanmoins, après que tous les autres joueurs ont joué, lorsqu’il annonce qu’il était Roi et a été assassiné, il prend la carte couronne. Ce sera donc lui qui choisira son personnage en premier au tour suivant", "Jaune")
    
    Marchand = Roles("Marchand", "Vous recevez au début de votre tour une pièce d’or supplémentaire – vous pouvez donc prendre soit trois pièces d’or, soit une carte et une pièce d’or. Vous recevez en outre une pièce d’or par quartier commerçant (vert) dans votre cité*.", "Vert")
    
    Eveque = Roles("Eveque", "Vous recevez une pièce d’or par quartier religieux (bleu) dans votre cité. Vous ne pouvez pas être attaqué par le Condottiere.", "Bleu")
    
    Architecte = Roles("Architecte", "Au début de votre tour, vous piochez deux cartes Quartiers supplémentaires – vous pouvez donc prendre en tout trois cartes, ou deux cartes et deux pièces d’or. Vous pouvez en outre bâtir jusqu’à trois quartiers durant votre tour.", "None")
    
    Magicien = Roles("Magicien", "À n’importe quel moment de votre tour*, vous pouvez, au choix : soit échanger toutes les cartes de votre main (pas celles de votre cité !) contre toutes les cartes de la main d’un autre joueur (vous pouvez faire cela même si vous n’avez pas de carte en main, et vous prenez alors les cartes de l’autre joueur). soit vous défausser d’un certain nombre de cartes de votre main, les placer sous la pioche, et piocher le même nombre de cartes en échange.", "None")
    
    Assassin = Roles("Assassin", "Vous annoncez quel autre personnage vous assassinez. Le joueur qui a ce personnage ne doit pas réagir, et ne se déclarera pas non plus lorsque son personnage sera appelé. Il ne révèlera sa carte qu’en dernier, pour annoncer qu’il avait été assassiné et qu’il a donc passé sont tour.", "None")
    
    global Pieces
    
    global TupleQuartiers
        
    Main = ()
        
    for _ in range(3):
            
        rdm_ = random.randint(0, len(TupleQuartiers) - 1)
            
        Main += (TupleQuartiers[rdm_],)
        
    print(Main)
    
    Player = input("NOM:")
    
    def CallRole():
        
        global Joueur
    
        Joueur = input("ROLE:")
        
        if Joueur not in liste:
        
            print(CallRole(), "Role indisponible.")
        
    print(CallRole())
    
    match Joueur:
        
        case "Voleur":
        
            global Joueur1
                
            Joueur1 = Joueurs(Voleur, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Condottiere":
        

                
            Joueur1 = Joueurs(Condottiere, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Roi":
        

                
            Joueur1 = Joueurs(Roi, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Marchand":
        

                
            Joueur1 = Joueurs(Marchand, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Eveque":
        

                
            Joueur1 = Joueurs(Eveque, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Architecte":
        

                
            Joueur1 = Joueurs(Architecte, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Magicien":
        

                
            Joueur1 = Joueurs(Magicien, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
            
        case "Assassin":
        

                
            Joueur1 = Joueurs(Assassin, Player, {}, Pieces, Main)
            
            print(Joueur1.__dict__)
            
            print(Joueur1.Role.__dict__)
    
    Main = ()
        
    for _ in range(3):
            
        rdm_ = random.randint(0, len(TupleQuartiers) - 1)
            
        Main += (TupleQuartiers[rdm_],)
        
    print(Main)
    
    Player = input("NOM:")
    
    def CallRole():
        
        global Joueur
    
        Joueur = input("ROLE:")
        
        if Joueur not in liste:
        
            print(CallRole(), "Role indisponible.")
        
    print(CallRole())
    
    match Joueur:
        
        case "Voleur":
        
            global Joueur2
                
            Joueur2 = Joueurs(Voleur, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Condottiere":
        

                
            Joueur2 = Joueurs(Condottiere, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Roi":
        

                
            Joueur2 = Joueurs(Roi, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Marchand":
        

                
            Joueur2 = Joueurs(Marchand, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Eveque":
        

                
            Joueur2 = Joueurs(Eveque, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Architecte":
        

                
            Joueur2 = Joueurs(Architecte, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Magicien":
        

                
            Joueur2 = Joueurs(Magicien, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
        case "Assassin":
        

                
            Joueur2 = Joueurs(Assassin, Player, {}, Pieces, Main)
            
            print(Joueur2.__dict__)
            
            print(Joueur2.Role.__dict__)
            
    Main = ()
        
    for _ in range(3):
            
        rdm_ = random.randint(0, len(TupleQuartiers) - 1)
            
        Main += (TupleQuartiers[rdm_],)
        
    print(Main)
    
    Player = input("NOM:")
    
    def CallRole():
        
        global Joueur
    
        Joueur = input("ROLE:")
        
        if Joueur not in liste:
        
            print("Role indisponible.", CallRole())
        
    print(CallRole())
    
    match Joueur:
        
        case "Voleur":
        
            global Joueur3
                
            Joueur3 = Joueurs(Voleur, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Condottiere":
        

                
            Joueur3 = Joueurs(Condottiere, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Roi":
        

                
            Joueur3 = Joueurs(Roi, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Marchand":
        

                
            Joueur3 = Joueurs(Marchand, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Eveque":
        

                
            Joueur3 = Joueurs(Eveque, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Architecte":
        

                
            Joueur3 = Joueurs(Architecte, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Magicien":
        

                
            Joueur3 = Joueurs(Magicien, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
            
        case "Assassin":
        

                
            Joueur3 = Joueurs(Assassin, Player, {}, Pieces, Main)
            
            print(Joueur3.__dict__)
            
            print(Joueur3.Role.__dict__)
    
    Main = ()
        
    for _ in range(3):
            
        rdm_ = random.randint(0, len(TupleQuartiers) - 1)
            
        Main += (TupleQuartiers[rdm_],)
        
    print(Main)
    
    Player = input("NOM:")
    
    def CallRole():
        
        global Joueur
    
        Joueur = input("ROLE:")
        
        if Joueur not in liste:
        
            print(CallRole(), "Role indisponible.")
        
    print(CallRole())
    
    match Joueur:
        
        case "Voleur":
        
            global Joueur4
                
            Joueur4 = Joueurs(Voleur, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Condottiere":
        

                
            Joueur4 = Joueurs(Condottiere, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Roi":
        

                
            Joueur4 = Joueurs(Roi, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Marchand":
        

                
            Joueur4 = Joueurs(Marchand, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Eveque":
        

                
            Joueur4 = Joueurs(Eveque, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Architecte":
        

                
            Joueur4 = Joueurs(Architecte, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Magicien":
        

                
            Joueur4 = Joueurs(Magicien, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)
            
        case "Assassin":
        

                
            Joueur4 = Joueurs(Assassin, Player, {}, Pieces, Main)
            
            print(Joueur4.__dict__)
            
            print(Joueur4.Role.__dict__)

print(CreerJoueurs())