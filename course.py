# importation des bibliothèques
import time, sys, keyboard, os, colorama
from threading import Thread

"""
Ce que j'aurais aimé réaliser :
- Modifier complètement le code de mon jeu pour en faire une interface graphique avec Pygame.
- Ajouter d'autres modes de jeu tels que la course contre la montre et le saut de haies (faciles à coder en interface graphique).
- Adapter mon code pour que N joueurs puissent jouer au lieu de seulement 2.
"""

colorama.init()

class Player(Thread):

    def __init__(self, position, name, commande, parcour, time, color):
        Thread.__init__(self)
        """
        Initialise les attributs de la classe Player (la position, son pseudo et sa commande pour avancer).
        """
        self.position = position
        self.name = name
        self.commande = commande
        self.parcour = parcour
        self.time = time
        self.color = color
        self.design = "🐴"  # Son affichage fonctionne sur VS Code

    
    def run(self):
        """
        Code à exécuter pendant l'exécution du thread.
        Méthode : avance d'une unité la position du cheval.
        Entrée : la position du joueur.
        Sortie : la nouvelle position du joueur.
        """
        while self.position < self.parcour:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_UP:
                if event.name.lower() == self.commande:
                    self.position += 1
                    print(self.color + self.design, "==>", self.name, ":", self.position, "mètres.")
                    if self.position == self.parcour:
                        self.time = time.time() - self.time
                        return self.position, self.time


# Quitter le jeu (modifications pygames)
def quitter_jeu():
    """
    Fonction : sert à quitter le jeu.
    Entrée : réponse de l'utilisateur.
    Sortie : _ 
    """
    print("Merci d'avoir joué ! Au revoir !")
    sys.exit(0) 
            

# Affiche le menu de parcours proposé
def choix_parcour(): 
    """
    Fonction : affiche le menu des maps.
    Entrée : _
    Sortie : _
    """
    print(colorama.Fore.GREEN + '╔' + '═' * 41 + '╗')
    print("║" + ' ' * 41 + "║")
    print("║" + " " * 17 + "Parcours" + " " * 16 + "║")
    print("║" + ' ' * 41 + "║")
    print("╠" + '═'*41 + "╣")
    print("║" + ' ' * 41 + "║")
    print("║   0 - Test (10m)" + " " * 24 + "║")
    print("║   1 - Plaine (100m)" + " " * 21 + "║")
    print("║   2 - L'Hippodrome Olympique (150m)" + " " * 5 + "║")
    print("║   3 - Route Arc-en-ciel (200m)" + " " * 10 + "║")
    print("║" + ' ' * 41 + "║")
    print("╠" + '═'*41 + "╣")
    print("║" + " " * 15 + "[B]  Retour" + " " * 15 + "║") 
    print("╚" + "═" * 41 + "╝")


def regle():
    """
    Fonction : affiche le menu des règles.
    Entrée : _
    Sortie : _ 
    """
    print(colorama.Fore.GREEN + '╔' + '═' * 55 + '╗')
    print("║"+ " " * 55 + "║")
    print("║" + " " * 24 + "Règles:" + " " * 24 + "║")
    print("║"+ " " * 55 + "║")
    print("╠"+ "═" * 55 + "╣")
    print("║ - Les règles de la course de chevaux                  ║")
    print("║ - Ce jeu se joue à 2                                  ║")
    print("║ - Le but du jeu est d'atteindre le premier à l'arrivée║")
    print("║ - De 4 à 99 ans                                       ║") 
    print("╠" + "═" * 55 + "╣")
    print("║                      B - Retour                       ║")
    print("╚" + "═" * 55 + "╝")


def condition_retour():
    """
    Fonction : demande à l'utilisateur son choix.
    Entrée : un caractère de type str.
    Sortie : la réponse de l'utilisateur dans une variable.
    """
    regle()
    retour = input("Appuyez sur [B] pour revenir dans le menu principal : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return retour


def commande():
    """
    Fonction : initie la commande du joueur (un seul caractère valide parmi la liste 'caractere').
    Entrée : _
    Sortie : la variable commande correspondant à la réponse de l'utilisateur (un seul caractère valide).
    """
    caractere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    commandes = input("Entrer votre commande (alphabet minuscule) : ")
    if len(commandes) == 1:
        if commandes in caractere:
            return commandes
        else:
            return None                 
    else:
        return None
    

def names(joueur_n):
    """
    Fonction : initie le pseudo du joueur (non défini).
    Entrée : une chaîne de caractères.
    Sortie : la variable pseudo correspondant à la réponse de l'utilisateur.
    """
    caractere = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [str(i+1) for i in range(9)] + [chr(i) for i in range(32, 127) if not chr(i).isalnum()]
    name = input(joueur_n + " Entrer votre pseudo : ")
    if len(name) >= 1: 
        for elt in name:
            if elt not in caractere:
                return None
        return name
    else:
        return None


def main():
    """
    Fonction : lance le jeu.
    Entrée : la réponse de l'utilisateur.
    Sortie : entre dans la section du jeu correspondant à la réponse de l'utilisateur.
    Sortie alternative : quitte le jeu.
    """
    menu()
    choix = input("Que voulez-vous faire ? ")
    if choix == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        quitter_jeu()
    elif choix == '1': 
        os.system('cls' if os.name == 'nt' else 'clear')
        play()
    elif choix == '2':
        os.system('cls' if os.name == 'nt' else 'clear') 
        retour = condition_retour()
        os.system('cls' if os.name == 'nt' else 'clear')
        while retour.upper() != 'B':
            print('Option invalide.')
            os.system('cls' if os.name == 'nt' else 'clear')
            retour = condition_retour()
        if retour.upper() == 'B':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


def p_1():
    """
    Fonction : sert à couper les étapes de configuration des joueurs en 2 (player 1 et player 2).
    Entrée : _
    Sortie : le nom du joueur 1 et sa commande.
    """
    name1 = names("Joueur 1, ")
    if name1 == None:
        name1 = "glougloubs"
        print("Vous n'avez pas respecté les règles de ce jeu.")
        print("Dorénavant, vous allez vous appeler [glougloubs].")
        time.sleep(1)
    else:
        print("Votre pseudo est", name1)
    commande1 = commande()
    if commande1 == None:
        commande1 = "a"
        print(name1, "vous êtes tellement stupide que votre commande sera [a].")
        time.sleep(1)
    else:
        print("Votre commande est", commande1)
        time.sleep(1)
    return name1, commande1


def p_2(name1, commande1):
    """
    Fonction : sert à couper les étapes de configuration des joueurs en 2 (player 1 et player 2).
    Entrée : le nom du joueur 1 et sa commande.
    Sortie : le nom des deux joueurs et les commandes des deux joueurs.
    """
    name2_v1 = names("Joueur 2, ")
    if name2_v1 == None:
        name2_v1 = "popo"
        print("Vous n'avez pas respecté les règles de ce jeu.")
        print("Dorénavant, vous allez vous appeler [popo].")
        time.sleep(1)
    else:
        name2 = check_pseudonymes_mm(name1, name2_v1)
        if name2 == None:
            name2 = "popo"
            print("Vous n'avez pas respecté les règles de ce jeu.")
            print("Dorénavant, vous allez vous appeler [popo].")
            time.sleep(1)
        else:
            print("Votre pseudo est", name2)
    commande2 = p_2_commande(name1, commande1)
    if commande2 == None:
        commande2 = "p"
        print("votre commande sera [p].")
        time.sleep(1)
    else:
        print("Votre commande est", commande2)
        time.sleep(1)
    return name2, commande2


def p_2_commande(name1, commande1):
    """
    Entrée : le nom du joueur 1 et sa commande.
    Sortie : la commande du joueur 2.
    """
    commande2_v1 = commande()
    commande2 = check_commandes_players_2_mm(name1, commande1, commande2_v1)
    return commande2


def menu_rapide():
    """
    Fonction n1 : configure les pseudos et commandes des deux joueurs 
    en les initiant et en vérifiant certaines conditions via des fonctions de vérification.
    Si l'une des configurations est fausse, il reconfigure les variables faussées.
    Fonction n2 : lance la partie.
    Entrée : _
    Sortie : il retourne les deux pseudos des deux joueurs et leurs commandes associées validées par les fonctions de vérification.
    """
    print(colorama.Fore.GREEN + '╔' + '═'*108 + '╗')
    print(colorama.Fore.GREEN + "║                                               Menu rapide                                                  ║")
    print(colorama.Fore.GREEN + "╠" + "═"*108 + "╣")
    print(colorama.Fore.GREEN + "║", " "*45,  colorama.Fore.BLUE + "Joueur 1"+ " "*52,  colorama.Fore.GREEN + "║") 
    print(colorama.Fore.GREEN + '╚' + '═'*108 + '╝', colorama.Fore.BLUE)
    name_player_1, commande_player_1 = p_1()
    print(colorama.Fore.GREEN + "═"*110)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorama.Fore.GREEN + '╔' + '═'*108 + '╗')
    print(colorama.Fore.GREEN + "║                                               Menu rapide                                                  ║")
    print(colorama.Fore.GREEN + "╠" + "═"*108 + "╣")
    print(colorama.Fore.GREEN + "║", " "*45,  colorama.Fore.RED + "Joueur 2"+ " "*52,  colorama.Fore.GREEN + "║")
    print(colorama.Fore.GREEN + '╚' + '═'*108 + '╝', colorama.Fore.RED)
    name_player_2, commande_player_2 = p_2(name_player_1, commande_player_1)
    print(colorama.Fore.GREEN + "═"*110)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    return name_player_1, commande_player_1, name_player_2, commande_player_2


# Compte à rebours (modifications pygames)
def compte_a_rebours():
    """
    Fonction : lance un compte à rebours de 3 secondes.
    Entrée : _
    Sortie : il affiche à chaque seconde le temps (en secondes) qu'il reste avant la fin du compte à rebours.
    """
    count_down = ["3", "2", "1", "GO"]
    for elt in count_down: 
        print(colorama.Fore.CYAN + elt)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')



def check_pseudonymes_mm(name1, name2):
    """
    Fonction : initie le pseudo du joueur 2 et s'assure que le pseudo du joueur 2 ne soit pas le même que celui du joueur 1.
    Entrée : prend en paramètre le pseudo du joueur 1 (pour remplir la condition de la fonction).
    Sortie : le pseudo entré du joueur 2 validé par la fonction.
    """
    if name1 == name2:
        name2 = None
        return name2
    else:
        return name2


def check_commandes_players_2_mm(name1, commande1, commande2):
    """
    Fonction : initie et vérifie si la touche que le joueur 2 entre est la même que le joueur 1.
    Entrée : prend en paramètre la touche du joueur 1.
    Sortie : la touche entrée du joueur 2 validée par le code.
    """
    if commande1 == commande2:
        p_2(name1, commande1)
    else:
        return commande2


def fonction_menu_parcour():
    """
    Fonction : selon le choix de l'utilisateur, la 'map' sera différente.
    Entrée : prend en paramètre le choix de l'utilisateur.
    Sortie : la map.
    """
    choix_parcour()
    rep = input("choisissez le parcours : ")
    choix = ["0", "1", "2", "3",]
    cons = [10, 100, 150, 200]
    if rep in choix:
        for i in range(len(choix)):
            if rep == choix[i]:
                return cons[i]
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        fonction_menu_parcour()


def menu():
    """
    Fonction : affiche le menu principal du jeu.
    Entrée : _
    Sortie : _
    """
    print(colorama.Fore.GREEN, '╔' + '═' * 41 + '╗')
    print(" ║" + " " * 41 + "║")
    print(" ║" + " " * 15 + "MENU DU JEU" + " " * 15 + "║")
    print(" ║" + " " * 41 + "║")
    print(" ╠" + '═' * 41 + "╣")
    print(" ║" + " " * 41 + "║")
    print(" ║    0 - Quitter le jeu                   ║")
    print(" ║    1 - Rejouer                          ║")
    print(" ║    2 - Afficher les règles              ║")
    print(" ║" + " " * 41 + "║")
    print(colorama.Fore.GREEN, '╚' + '═' * 41 + '╝')


def play():
    """
    Fonction : sert à initialiser entièrement les deux joueurs et à lancer leurs threads pour jouer la partie.
               Selon les résultats, elle affichera un score et relancera le jeu.
    Entrée : _
    Sortie : la partie, les scores et le jeu.
    """
    name1, commande1, name2, commande2 = menu_rapide()
    parcour = fonction_menu_parcour()
    compte_a_rebours()
    os.system('cls' if os.name == 'nt' else 'clear')
    temp = time.time()
    color1 = colorama.Fore.BLUE
    color2 = colorama.Fore.RED
    pseudo_1 = Player(0, name1, commande1, parcour, temp, color1)
    pseudo_2 = Player(0, name2, commande2, parcour, temp, color2)
    pseudo_1.start()
    pseudo_2.start()
    pseudo_1.join()
    pseudo_2.join()
    os.system('cls' if os.name == 'nt' else 'clear')
    if pseudo_1.time > pseudo_2.time:
        print(colorama.Fore.RED + '╔' + '═' * 29 + '╗')
        print("║" + " " * 10 + "VAINQUEUR" + " " * 10 + "║ ==>    ║ 1 - ", name2,"   ║   sec: ", int(pseudo_2.time), " ║  🐴")
        print('╚' + '═' * 29 + '╝')
        print("")
        print(colorama.Fore.BLUE + '╔' + '═' * 29 + '╗')
        print("║" + " " * 10 + "PERDANT" + " " * 10 + "║ ==>    ║ 1 - ", name1,"   ║   sec: ", int(pseudo_1.time), " ║    🐴")
        print('╚' + '═' * 29 + '╝')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        input(colorama.Fore.GREEN + "Relancer: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    elif pseudo_1.time < pseudo_2.time:
        print(colorama.Fore.BLUE + '╔' + '═' * 29 + '╗')
        print("║" + " " * 10 + "VAINQUEUR" + " " * 10 + "║ ==>    ║ 1 - ", name1,"   ║   sec: ", int(pseudo_1.time), " ║")
        print('╚' + '═' * 29 + '╝')
        print("")
        print(colorama.Fore.RED + '╔' + '═' * 29 + '╗')
        print("║" + " " * 10 + "PERDANT" + " " * 10 + "║ ==>    ║ 1 - ", name2,"   ║   sec: ", int(pseudo_2.time), " ║")
        print('╚' + '═' * 29 + '╝')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        input(colorama.Fore.GREEN + "Relancer: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        print("Égalité")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        input(colorama.Fore.GREEN + "Relancer: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

main()



    
