import pygame
import random
import mm

taille_combinaison = 5
nb_coups_max = 16

def generer_combinaison():
    liste = []
    for i in range(taille_combinaison):
        # choice donne une seule couleur donc on le fait 5 fois
        nouveau = random.choice(mm.TabCouleur)
        liste.append(nouveau)
    return liste
    
def calculer_resultat(proposition, secrete):
    bien_place = 0
    mal_place = 0
    # bien place = meme couleur a la meme position (meme i des deux cotes)
    for i in range(len(proposition)):
            if proposition[i] == secrete[i]:
                bien_place = bien_place + 1
    # on compte les couleurs en commun sans regarder les positions
    # min pour pas compter 2 fois une couleur qui est en trop
    commun = 0
    for couleur in mm.TabCouleur:
        commun = commun + min(proposition.count(couleur), secrete.count(couleur))
    # mal places = en commun - ceux qui sont deja bien places
    mal_place = commun - bien_place
    return bien_place, mal_place

def est_gagne(resultat):
    # resultat[0] c'est les bien_places exemple : (3: bien_place, 1: mal_place)
    return resultat[0] == taille_combinaison #rappel taille_combinaison = 5

def manche_finie(resultat, nb_coups, nb_coups_max):
    # fini si gagne ou si on a utilise tous les coups
    return est_gagne(resultat) or nb_coups >= nb_coups_max

def afficher_dialogue(fenetre, message):
    # boite blanche avec un contour noir en bas (comme dans pokemon)
    fond = pygame.Surface((760, 120), pygame.SRCALPHA)   # feuille de 760 x 120 qui accepte la transparence
    fond.fill((255, 255, 255, 200))                       # blanc + transparence
    fenetre.blit(fond, (20, 540))                         # on la colle au meme endroit
    pygame.draw.rect(fenetre, mm.Noir, [20, 540, 760, 120], 4)
    police = pygame.font.SysFont("monospace", 20)
    texte = police.render(message, True, mm.Noir)
    fenetre.blit(texte, (40, 560))
    pygame.display.update()

def afficher_fin(fenetre, gagne, nb_coups):
    if gagne == True:
        if nb_coups <= 1:
            message = "Tu as réussi à pirater mon code ? Bien joué..."
        elif nb_coups <= 5:
            message = f"BOOM ! Tu as gagné avec {nb_coups} coups c'est impressionnant !"
        else:
            message = f"Tu as gagné avec {nb_coups} coups, pas mal pour un débutant"
    else:
        message = "Entraîne-toi plus et reviens me voir. ÉCHEC"
    afficher_dialogue(fenetre, message)


def test():
    print(generer_combinaison())

    # test 1 : tout pareil -> (5, 0)
    secrete     = [mm.Rouge, mm.Bleu, mm.Vert, mm.Noir, mm.Rose]
    proposition = [mm.Rouge, mm.Bleu, mm.Vert, mm.Noir, mm.Rose]
    print(calculer_resultat(proposition, secrete))

    # test 2 : 1 bien place, 2 mal places -> (1, 2)
    secrete     = [mm.Rouge, mm.Rouge, mm.Bleu, mm.Vert, mm.Noir]
    proposition = [mm.Rouge, mm.Bleu, mm.Rouge, mm.Rouge, mm.Rouge]
    print(calculer_resultat(proposition, secrete))

    # test 3 : rien en commun -> (0, 0)
    secrete     = [mm.Rouge, mm.Rouge, mm.Bleu, mm.Bleu, mm.Vert]
    proposition = [mm.Noir, mm.Blanc, mm.Gris, mm.Rose, mm.Orange]
    print(calculer_resultat(proposition, secrete))

    # test 4 : 5 bien places -> True (gagne)
    print(est_gagne((5, 0)))
    # test 5 : 3 bien places -> False (pas encore gagne)
    print(est_gagne((3, 1)))

    # test 6 : gagne au coup 3 -> True (manche finie)
    print(manche_finie((5, 0), 3, 10))
    # test 7 : pas gagne mais 10 coups sur 10 -> True (plus de coups)
    print(manche_finie((2, 1), 10, 10))
    # test 8 : pas gagne et 3 coups sur 10 -> False (on continue)
    print(manche_finie((2, 1), 3, 10))


def principale():
    
    # afficher l'IHM
    pygame.init()
    fenetre = pygame.display.set_mode([800, 680])
    fenetre.fill(mm.Blanc)
    mm.afficherPlateau(fenetre)
    mm.afficherChoixCouleur(fenetre)

    # combinaison secrete
    secrete = generer_combinaison()

    # c. tant que la manche n'est pas finie
    nb_coups = 1
    resultat = (0, 0)
    while not manche_finie(resultat, nb_coups, nb_coups_max):
        nb_coups = nb_coups + 1
        proposition = mm.construireProposition(fenetre, nb_coups)
        resultat = calculer_resultat(proposition, secrete)
        mm.afficherResultat(fenetre, resultat, nb_coups)
    mm.afficherSecret(fenetre, secrete)

    # message de fin
    afficher_fin(fenetre, est_gagne(resultat), nb_coups - 1)

    # e. attendre que l'utilisateur ferme
    fini = False
    while not fini:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fini = True
    pygame.quit()


if __name__ == '__main__':
    principale()
