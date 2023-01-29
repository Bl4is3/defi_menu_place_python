from views.view import View

class Controller:
    def __init__(self):
        self.view = View()
    
    def run(self):
        choix = self.view.show_principal_menu()
        while True:
            if choix == "1":
                choix = self.view.show_menu_1()
            elif choix == "11":
                choix = self.view.show_menu_11()
            elif choix in ("111", "112"):
                choix = self.view.show_menu_11()
            elif choix == "113":
                choix = self.view.show_menu_1()
            elif choix == "12":
                choix = self.view.show_menu_12()
            elif choix in ("121", "122"):
                choix = self.view.show_menu_12()
            elif choix == "123":
                choix = self.view.show_menu_2()
            elif choix in ("13", "131", "132"):
                choix = self.view.show_menu_13()
            elif choix == "133":
                choix = self.view.show_menu_3()
            elif choix in ("2", "21", "22", "23"):
                choix = self.view.show_menu_2()
            elif choix in ("3", "31", "32", "33"):
                choix = self.view.show_menu_3()
            elif choix in ("4", "15","115", "125", "135", "25", "35"):
                return False
            else:
                choix = self.view.show_principal_menu()
