import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Move Rows Between Treeviews")
window.geometry("600x400")

# Create two frames to hold the Treeview widgets
frame1 = tk.Frame(window)
frame1.pack(side=tk.LEFT, padx=20, pady=20)

frame2 = tk.Frame(window)
frame2.pack(side=tk.RIGHT, padx=20, pady=20)

# Define columns
columns = ("Name", "Date", "City")

# Create first Treeview table
tree1 = ttk.Treeview(frame1, columns=columns, show="headings")
tree1.heading("Name", text="Name")
tree1.heading("Date", text="Date")
tree1.heading("City", text="City")

# Create second Treeview table
tree2 = ttk.Treeview(frame2, columns=columns, show="headings")
tree2.heading("Name", text="Name")
tree2.heading("Date", text="Date")
tree2.heading("City", text="City")

# Add sample data to first table
data = [
    ("Alice", "2025-02-26", "New York"),
    ("Bob", "2025-02-25", "Los Angeles"),
    ("Charlie", "2025-02-24", "Chicago")
]

for item in data:
    tree1.insert("", tk.END, values=item)

# Pack Treeview tables
tree1.pack(expand=True, fill="both")
tree2.pack(expand=True, fill="both")

# Function to move selected row from tree1 to tree2
def move_to_tree2():
    selected_item = tree1.selection()  # Get selected row
    if selected_item:
        values = tree1.item(selected_item, "values")  # Get values
        tree2.insert("", tk.END, values=values)  # Insert into tree2
        tree1.delete(selected_item)  # Remove from tree1

# Button to move row
move_button = tk.Button(window, text="Move →", command=move_to_tree2)
move_button.pack(pady=10)

# Run the application
window.mainloop()