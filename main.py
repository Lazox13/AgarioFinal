import core
from creep import Creep
from ennemi import Ennemi
from joueur import Joueur


def setup():
    # Paramètres fenetre
    core.WINDOW_SIZE = [800, 800]
    core.fps = 60

    # Variables joueurs
    core.memory("J", Joueur())

    # Variables ennemies
    core.memory("E", Ennemi())
    core.memory("TabE", [])

    for e in range(5):
        core.memory("TabE").append(Ennemi())

    # Variables creep
    core.memory("TabC", [])
    core.memory("C", Creep())

    for c in range(150):
        core.memory("TabC").append(Creep())


def run():
    # RAZ ecran
    core.cleanScreen()

    # Commande creep
    for c in core.memory("TabC"):
        c.dessiner()

    # Commande ennemi
    for e in core.memory("TabE"):
        e.dessiner()

    # Decision mouvement Ennemi
    for e in core.memory("TabE"):
        if core.memory("J").Rayon > e.Rayon:
            e.deplacerVersCreep(core.memory("C").Position)
            ##A voir comment chercher le plus proche dans la list de creep
            ##Car les ennemis ne bougent pas s'il n'ont pas une cible fixe

        else:
            e.deplacerVersJoueur(core.memory("J").Position)

    # Commande joueur
    core.memory("J").dessiner()
    core.memory("J").deplacer(core.getMouseLeftClick())

    # Calcul grossir
    # Joueur mange creep
    for c in core.memory("TabC"):
        if c.Position.distance_to(core.memory("J").Position) < core.memory("J").Rayon + c.Rayon:
            c.mourir()
            core.memory("J").grossir()

    # Ennemi mange creep
    for c in core.memory("TabC"):
        for e in core.memory("TabE"):
            if c.Position.distance_to(e.Position) < e.Rayon + c.Rayon:
                c.mourir()
                core.memory("E").grossir()

    # Joueur mange ennemi
    for e in core.memory("TabE"):
        if core.memory("J").Rayon > e.Rayon:
            if e.Position.distance_to(core.memory("J").Position) < core.memory("J").Rayon + e.Rayon:
                e.mourir()
                core.memory("J").grossir()

    # Ennemi mange joueur
    for e in core.memory("TabE"):
        if e.Rayon > core.memory("J").Rayon:
            if core.memory("J").Position.distance_to(e.Position) < core.memory("J").Rayon + e.Rayon:
                core.memory("J").mourir()
                e.grossir()

core.main(setup, run)
