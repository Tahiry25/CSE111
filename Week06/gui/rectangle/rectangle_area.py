import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. in tkinter, a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Rectangle")
    frm_main.pack(padx=6, pady=4, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    lbl_width = Label(frm_main, text="Width:")
    lbl_height = Label(frm_main, text="Height:")
    lbl_area = Label(frm_main, text="AREA:")

    ent_width = IntEntry(frm_main, width=10, lower_bound=1, upper_bound=999999)
    ent_height = IntEntry(frm_main, width=10, lower_bound=1, upper_bound=999999)

    btn_clear = Button(frm_main, text="Clear Input")

    lbl_width.grid(row=0, column=0)
    ent_width.grid(row=1, column=0, pady=3)

    lbl_height.grid(row=0, column=1)
    ent_height.grid(row=1, column=1, pady=3)

    lbl_area.grid(row=3, column=0, pady=3)
    lbl_area_result = Label(frm_main, width=10)
    lbl_area_result.grid(row=3, column=1, pady=3)

    btn_clear.grid(row=4, column=0, columnspan=2, pady=30, sticky="w")

    def area(event):
        try:
            w = ent_width.get()
            h= ent_height.get()
            area = w*h

            lbl_area_result.config(text=f"{area:.0f}")

        except ValueError:
            lbl_area.config(text="")

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_height.clear()
        lbl_area.config(text="")
        ent_width.focus()

    ent_height.bind("<KeyRelease>", area)
    btn_clear.config(command=clear)
    ent_width.focus()

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()