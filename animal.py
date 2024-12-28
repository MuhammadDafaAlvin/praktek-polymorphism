import tkinter as tk

class Animal:
    def make_sound(self):
        return "Some sound"
    
class Bird(Animal):
    def make_sound(self):
        return "Tweet"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Miaw"

class Cow(Animal):
    def make_sound(self):
        return "Mooo"
    
def show_sound(animal):
    tk.label_result.config(text=animal.make_sound())
    
root = tk.Tk()
root.title("Polymorphism in Tkinter")

tk.label_result = tk.Label(root, text="Klik salah satu tombol untuk menampilkan suara", font=("Arial", 16))
tk.label_result.pack()

btn_bird = tk.Button(root, text="Tweet", command=lambda: show_sound(Bird()))
btn_bird.pack()

btn_dog = tk.Button(root, text="Woof", command=lambda: show_sound(Dog()))
btn_dog.pack()

btn_cat = tk.Button(root, text="Miaw", command=lambda: show_sound(Cat()))
btn_cat.pack()

btn_cow = tk.Button(root, text="Mooo", command=lambda: show_sound(Cow()))
btn_cow.pack()

root.mainloop()