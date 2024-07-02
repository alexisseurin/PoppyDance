
# Réalisation des mouvements du robot avec :
# - VMWare Workstation (OS : Bodhi Linux)
# - IDE Spyder et simulateur CoppeliaSim (version EDU)
# - Python 3.6
#
# Septembre 2021


# Importation des bibliothèques du robot (virtuel ou physique)
# from pypot.creatures import PoppyErgoJr

# Uniquement pour la simulation du robot entre Spyder et CoppeliaSim
# poppy = PoppyErgoJr(simulator = 'vrep', scene="poppy_ergo_jr_holder.ttt") 

# Utilisation du robot sans utiliser la caméra
# poppy = PoppyErgoJr(camera='dummy')

# --------------------------------------------------------

# Fonction principale utilisé pour notre robot Poppy Ergo Jr.

def poppy_dance():
    time.sleep(1)
    
    pos_initiale= { 'm1':0,'m2':0, 'm3':0,'m4':0, 'm5':0, 'm6':0 }
    pos_reverse = { 'm1':0,'m2':0, 'm3':90,'m4':180, 'm5':-90, 'm6':-20 }
    pos_sky_watching = { 'm1':0,'m2':0, 'm3':90,'m4':180, 'm5':0, 'm6':-20 }
    pos_Plongeur = {'m1':0,'m2':-40, 'm3':60,'m4':0, 'm5':-70, 'm6':-20 }
    pos_Balai = {'m1':0,'m2':0, 'm3':90,'m4':0, 'm5':-90, 'm6':0 }
    pos_Balai_gauche = {'m1':90,'m2':0, 'm3':90,'m4':0, 'm5':-90, 'm6':0 }
    pos_Balai_droite = {'m1':-90,'m2':0, 'm3':90,'m4':0, 'm5':-90, 'm6':0 }
    pos_Balai_gauche = {'m1':90,'m2':0, 'm3':90,'m4':0, 'm5':-90, 'm6':0 }
    pos_Shaker = {'m1':0,'m2':0, 'm3':0,'m4':0, 'm5':90, 'm6':-20 }
    pos_Shaker_haut = {'m1':90,'m2':0, 'm3':0,'m4':0, 'm5':0, 'm6':-20 }
    pos_Shaker_bas = {'m1':-180,'m2':0, 'm3':0,'m4':0, 'm5':90, 'm6':-20 }
    pos_Looping = {'m1':0,'m2':90, 'm3':0,'m4':180, 'm5':90, 'm6':-20 }
    pos_Looping_inverse = {'m1':0,'m2':-90, 'm3':0,'m4':0, 'm5':90, 'm6':-20 }
    pos_360 = { 'm1':360,'m2':0, 'm3':0,'m4':0, 'm5':0, 'm6':0 }

    
    fast_moving = 6
    
    # fonction goto_position : Commande au robot d'utiliser les moteurs à des positions données

    poppy.goto_position(pos_initiale,fast_moving, wait=True)
    poppy.goto_position(pos_reverse,fast_moving, wait=True)
    poppy.goto_position(pos_sky_watching,fast_moving, wait=True)
    poppy.goto_position(pos_Plongeur,fast_moving, wait=True)
    poppy.goto_position(pos_Balai,fast_moving, wait=True)
    poppy.goto_position(pos_Balai_gauche,fast_moving, wait=True)
    poppy.goto_position(pos_Balai_droite,fast_moving, wait=True)
    poppy.goto_position(pos_Balai_gauche,fast_moving, wait=True)
    poppy.goto_position(pos_Shaker,fast_moving, wait=True)
    poppy.goto_position(pos_Shaker_haut,fast_moving, wait=True)
    poppy.goto_position(pos_Shaker_bas,fast_moving, wait=True)
    poppy.goto_position(pos_Shaker_haut,fast_moving, wait=True)
    poppy.goto_position(pos_Shaker_bas,fast_moving, wait=True)
    poppy.goto_position(pos_Looping,fast_moving, wait=True)
    poppy.goto_position(pos_Looping_inverse,fast_moving, wait=True)
    poppy.goto_position(pos_Looping,fast_moving, wait=True)
    poppy.goto_position(pos_360,fast_moving, wait=True)    
    poppy.goto_position(pos_initiale,fast_moving, wait=True)
