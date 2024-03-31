import tkinter as tk
from tkinter import ttk

class LocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Tracker")

        self.frame = ttk.Frame(self.root, padding="40")
        self.frame.grid(row=0, column=0)

        self.label = ttk.Label(self.frame, text="Select an item:")
        self.label.grid(row=0, column=0)

        self.drop_down_box = ttk.Combobox(self.frame, width=20, values=["Bike 1", "Bike 2", "Bike 3", "Bike 4"])
        self.drop_down_box.grid(row=0, column=1)
        self.drop_down_box.current(0)

        self.button = ttk.Button(self.frame, text="Display Coordinates", command=self.print_selection)
        self.button.grid(row=1, column=0, columnspan=2, pady=10)

    def print_selection(self):
        selected_bike = self.drop_down_box.get()
        print("Selected bike:", selected_bike)

def main():
    root = tk.Tk()
    app = LocationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
