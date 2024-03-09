import subprocess
import rumps

class FreshSeshApp(rumps.App):
    def __init__(self):
        super(FreshSeshApp, self).__init__("")
        self.icon = "fs.png"
        self.menu = self._create_menu()

    def _create_menu(self):
        return ["FreshSesh AI", "Manage Formulas"]
    

    @rumps.clicked("Manage Formulas")
    def manage_formulas(self, _):
        # substitute '/path/to/your/gui.py' with actual path to your gui.py file
        subprocess.run(['python3', 'gui.py'])

if __name__ == "__main__":
    FreshSeshApp().run()
