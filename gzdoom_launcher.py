from tkinter import Tk, Button, Radiobutton, StringVar, Label
import os
import subprocess

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("GZDoom WAD Selector")
        
        self.pwad_path = "/home/daniel/.var/app/org.zdoom.GZDoom/.config/gzdoom/wads"
        self.iwad_path = "/home/daniel/.var/app/org.zdoom.GZDoom/.config/gzdoom"

        self.selected_pwad = StringVar()
        self.selected_iwad = StringVar()

        self.pwad_list = self.get_wads(self.pwad_path, True)
        self.iwad_list = self.get_wads(self.iwad_path, False)
        
        self.setup_pwad_selector(self.pwad_list)
        self.setup_iwad_selector(self.iwad_list)
        self.setup_start_button()
    
    def get_wads(self, wad_path, getting_pwads):
        self.wad_folder = os.scandir(wad_path)
        self.wad_list = []
        for entry in self.wad_folder:
            if not entry.is_file():
                continue
            if entry.name.lower().endswith(".wad") or (entry.name.lower().endswith(".pk3") and getting_pwads == True):
                self.wad_list.append(entry.name)
        self.wad_folder.close()
        return self.wad_list
    
    def setup_pwad_selector(self, pwad_list):
        self.pwad_label = Label(text="select pwad:")
        self.pwad_label.pack()
        for i, pwad in enumerate(pwad_list):
            r = Radiobutton(text = pwad[:-4], value = pwad, variable = self.selected_pwad)
            r.pack()
    
    def setup_iwad_selector(self, iwad_list):
        self.iwad_label = Label(text="select iwad:")
        self.iwad_label.pack()
        for i, iwad in enumerate(iwad_list):
            r = Radiobutton(text = iwad[:-4], value = iwad, variable = self.selected_iwad)
            r.pack()
    
    def setup_start_button(self):
        self.b = Button(text="start GZDoom", command=self.run_doom)
        self.b.pack()
    
    def run_doom(self):
        print(f"-file wads/{self.selected_pwad.get()}", f"-iwad {self.selected_iwad.get()}")
        subprocess.run(["flatpak", "run", "org.zdoom.GZDoom", "-file", f"wads/{self.selected_pwad.get()}", "-iwad", self.selected_iwad.get()])
        window.quit()



window = Window()
window.mainloop()
