import pygame #on importe le module pygame

def principale()->None:
    pygame.init() # on initialise pygame
        
    # on crée un fenetre 1000 pixels de large sur 500 de haut
    fenetre = pygame.display.set_mode([1000,500])
    
    #on colorie le fond de la fenetre (0 Rouge, 32 Vert, 192 Bleu)
    fenetre.fill([0,32,192])
    
    #on cree une fonte (police et taille)
    myfont = pygame.font.SysFont("monospace", 80)
    # on cree une etiquette (label en anglais), texte à ecrire, et la couleur
    lab = myfont.render("coucou",1,[192,0,128])
    #on place cette etiquette dans la fenetre en possition x=550 et y=25
    fenetre.blit(lab,[550,25])
    
    #on applique les changements précédents pour les afficher
    pygame.display.update()
    
    fini = False
    print("appuyer sur RETURN pour quitter le programme")
    while not fini:
        for event in pygame.event.get(): #pygame.event.get() renvoie une "espece" de liste d'evenements
            
            # pour chaque evenement on regarde son type (est ce une touche du clavier pressee; un clic ...etc)
            if event.type == pygame.KEYDOWN: # est ce une touche du clavier pressee
                keys = pygame.key.get_pressed() # on recupere une "espece" de dictionnaire de touche 
                fini = keys[pygame.K_RETURN] # keys[pygame.K_RETURN] vaudra True si la touche "enter" a été enfoncee
                print(keys[pygame.K_RETURN])
                if not fini:
                    print("1 touche quelconque a été pressee:")
                if keys[pygame.K_b]: # est ce qu'on a enfoncer la touche 'b'?
                    print("b")
                    pygame.draw.circle(fenetre,[255,255,0], [-10,80],60) #on dessine un cercle 
                    pygame.draw.rect(fenetre,[255,255,255],[500,0,100,200]) #on dessine un rectangle
                    pygame.display.update() # on applique les modifications
            if event.type == pygame.QUIT:
                fini = True
    print("AU REVOIR")

    pygame.quit()


if __name__ == '__main__' :
    principale()