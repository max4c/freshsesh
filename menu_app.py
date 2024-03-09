import subprocess
import rumps
from formula_manager import FormulaManager

class FreshSeshApp(rumps.App):
    def __init__(self,formula_manager):
        super(FreshSeshApp, self).__init__("")
        self.icon = "fs.png"
        self.formula_manager = formula_manager
        self.menu = self._create_menu()

    def _create_menu(self):
        return ["FreshSesh AI", "Manage Formulas", *self._create_formula_menu()]
    
    def _create_formula_menu(self):
        # Shorten formulas and create menu items for them
        formulas = self.formula_manager.list_formulas()

        menu = {}
        
        # Add "Recap Formulas" as a separator in the menu
        menu["Formulas"] = None
        
        for formula in formulas:
            display_formula = formula.split("FOR PROJECT ")[-1] + " FOR " + formula.split("OF MY ")[-1].split(" FOR")[0].lower()
            menu[display_formula] = self._run_formula(formula)
        return menu

    def _run_formula(self, formula):
        def callback(_):
            # Run the formula here
            print(f"Running formula: {formula}")
        return callback

    def refresh_menu(self):
        self.status_bar_app.remove_menu('Formulas')
        formula_menu = self._create_formula_menu()
        self.status_bar_app.add_menu('Formulas', formula_menu)

    @rumps.clicked("Manage Formulas")
    def manage_formulas(self, _):
        # substitute '/path/to/your/gui.py' with actual path to your gui.py file
        subprocess.run(['python3', 'gui.py'])

if __name__ == "__main__":
    formula_manager = FormulaManager() 
    FreshSeshApp(formula_manager).run()
