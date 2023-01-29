class View:
    """Création des vues"""

    def show_menu_1(self):
        print(
            "\n-------------------------------\n"
            "Menu 1:\n"
            "-------------------------------\n"
            "11 - Sous-menu 11 \n"
            "12 - Sous-menu 12 \n"
            "13 - Sous-menu 13 \n"
            "14 - Revenir à l'accueil\n"
            "15 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix
    
    def show_menu_11(self):
        print(
            "\n-------------------------------\n"
            "Menu 11:\n"
            "-------------------------------\n"
            "111 - Sous-menu 111 \n"
            "112 - Sous-menu 112 \n"
            "113 - Revenir au menu precedent \n"
            "114 - Revenir à l'accueil\n"
            "115 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix

    def show_menu_12(self):
        print(
            "\n-------------------------------\n"
            "Menu 12:\n"
            "-------------------------------\n"
            "121 - Sous-menu 121 \n"
            "122 - Sous-menu 122 \n"
            "123 - Revenir au menu precedent \n"
            "124 - Revenir à l'accueil\n"
            "125 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix

    def show_menu_13(self):
        print(
            "\n-------------------------------\n"
            "Menu 13:\n"
            "-------------------------------\n"
            "131 - Sous-menu 131 \n"
            "132 - Sous-menu 132 \n"
            "133 - Revenir au menu precedent \n"
            "134 - Revenir à l'accueil\n"
            "135 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix


    def show_menu_2(self):
        print(
            "\n-------------------------------\n"
            "Menu 2:\n"
            "-------------------------------\n"
            "\n21 - Sous-menu 21 \n"
            "22 - Sous-menu 22 \n"
            "23 - Sous-menu 23 \n"
            "24 - Revenir à l'accueil\n"
            "25 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix
    
    def show_menu_3(self):
        print(
            "\n-------------------------------\n"
            "Menu 3:\n"
            "-------------------------------\n"
            "31 - Sous-menu 31 \n"
            "32 - Sous-menu 32 \n"
            "33 - Sous-menu 33 \n"
            "34 - Revenir à l'accueil\n"
            "35 - Quitter\n"
        )
        choix = input("Entrez votre choix :")
        return choix

    def show_principal_menu(self):
        print(
            "\nMenu Principal:\n"
            "-------------------------------\n"
            "1 - Menu 1 \n"
            "2 - Menu 2 \n"
            "3 - Menu 3 \n"
            "4 - Quitter \n"
            "\nIl est possible d'accéder directement à un sous-menu en tapant son numéro\n"
        )
        choix = input("Entrez votre choix :")
        return choix