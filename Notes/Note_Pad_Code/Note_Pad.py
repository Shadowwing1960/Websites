from guizero import App, TextBox, PushButton, Box, Combo, Text
import os
import os.path
import shutil


# Code For Notepad
def note_pad():
    # function for reading
    def open_file():
        fp = r"C:/Users/HP Admin/PycharmProjects/Websites/Notes/Notes_Storage/"
        new_path = fp + file_name.value + ".txt"
        if os.path.exists(new_path):
            with open(new_path, "r") as f:
                editor.value = f.read()
        else:
            print("Files does not exist")

    # function for writing files in save Folder
    def save_file():
        ns = r"C:/Users/HP Admin/PycharmProjects/Websites/Notes/Notes_Storage"
        with open(file_name.value + ".txt", "w") as f:
            f.write(editor.value)
            f.close()
            fl = r"C:/Users/HP Admin/PycharmProjects/Websites"
            for file in os.listdir(fl):
                if file.endswith('.txt'):
                    shutil.move(file, ns)

    # function for deleting files
    def delete_file():
        fp = r"C:/Users/HP Admin/PycharmProjects/Websites/Notes/Notes_Storage/"
        new_path = fp + file_name.value + ".txt"
        if os.path.exists(new_path):
            os.remove(new_path)
        else:
            print("Files does not exist")

    def exit_app():
        app.destroy()
        print("You have exited successfully")

    # App itself
    app = App(title="Notepad")

    file_controls = Box(app, align="top", width=1980, height=35)

    file_name = TextBox(file_controls, text="Notes", width=45, align="left")

    PushButton(file_controls, text="Exit", command=exit_app, align="right")

    PushButton(file_controls, text="Save", command=save_file, align="right")

    PushButton(file_controls, text="Open", command=open_file, align="right")

    PushButton(file_controls,
               text="Delete",
               command=delete_file,
               align="right")

    editor = TextBox(app, multiline=True, height="fill", width="fill")

    # Function to update Background
    def update_bg():
        app.bg = bg_combo.value

    # Function to update text
    def update_text():
        app.text_color = text_combo.value

    # Colors and box for buttons
    box = Box(app, align="bottom")
    colors = ["Black", "White", "Red", "Green", "Blue", "yellow"]
    app.text_color = "White"
    app.bg = "Black"

    # Text and Combo
    Text(box, text="←[Background color]", align="right")
    bg_combo = Combo(box,
                     align="right",
                     options=colors,
                     selected=app.bg,
                     command=update_bg)

    Text(box, text="[Text color]→", align="left")
    text_combo = Combo(box,
                       align="left",
                       options=colors,
                       selected=app.text_color,
                       command=update_text)

    # Displaying App
    app.display()
