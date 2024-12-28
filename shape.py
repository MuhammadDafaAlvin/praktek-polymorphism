import tkinter as tk

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
def calculate_area():
    try:
        shape_type = shape_type_var.get()
        if shape_type == "Rectangle":
            length = float(length_entry.get())
            width = float(width_entry.get())
            shape = Rectangle(length, width)
        elif shape_type == "Circle":
            radius = float(radius_entry.get())
            shape = Circle(radius)
        else:   
            result_label.config(text="Invalid shape type!")
            return
        
        area = shape.area()
        perimeter = shape.perimeter()
        result_label.config(text=f"Area: {area}\nPerimeter: {perimeter}")

    except ValueError:
        result_label.config(text="Invalid input!")

def reset_shape():
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    radius_entry.delete(0, tk.END)
    tk.result_label.config(text="")
    
root = tk.Tk()
root.title("Shape Calculator")

shape_type_var = tk.StringVar(value="Rectangle")
rectangle_button = tk.Radiobutton(root, text="Rectangle", variable=shape_type_var, value="Rectangle")
rectangle_button.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)
width_entry = tk.Entry(root)
width_entry.pack(pady=5)

circle_button = tk.Radiobutton(root, text="Circle", variable=shape_type_var, value="Circle")
circle_button.pack(pady=5)

radius_entry = tk.Entry(root)
radius_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_area)
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_shape)
reset_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()