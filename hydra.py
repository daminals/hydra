# hydra.py
import tkinter as tk
class Hydra():	
	def __init__(self):
		Window = self.Window = tk.Tk()
		Window.title("Hydra Virus")
		text = tk.Label(Window, text='Cut off a head, two more grow in its place \n\n\n\n\n\n\n\n')
		text.pack()
		def on_close():
			self.Window.destroy()
			for i in range(2):
				a = Hydra()

		Window.protocol("WM_DELETE_WINDOW", on_close)
hydra = Hydra()
hydra.Window.mainloop()
