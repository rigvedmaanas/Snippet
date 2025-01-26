from customtkinter import *
from CustomtkinterCodeViewer.CTkCodeViewer import CTkCodeViewer
from PIL import Image
# NOTE: Put limit for description to 120

class Snippet(CTkFrame):
    def __init__(self, *args, width=350, height=300, title, description, code, language, **kwargs):
        super().__init__(*args, width=width, height=height, fg_color="#1D1D1D", **kwargs)
        self.pack_propagate(False)
        self.TEXTBOX3 = CTkCodeViewer(master=self, height=178, width=350, code=code, language=language, theme="material", font=CTkFont(size=16), activate_scrollbars=False, bg_color=self.master.cget("fg_color"))
        self.TEXTBOX3.pack(pady=(0, 0), fill="x")

        self.TEXTBOX3.pack_propagate(False)
        self.title = CTkLabel(master=self, text=title, justify="left", anchor="w", padx=13,
                               font=CTkFont(size=20))
        self.title.pack(pady=(10, 0), fill="x")
        self.description = CTkLabel(master=self, text=description,
                                    justify="left", anchor="w", padx=13, wraplength=340, font=CTkFont(size=16))
        self.description.pack(pady=(10, 0), fill="x")

        self.copy = CTkButton(self, text="", image=CTkImage(Image.open("Assets/copy.png")), width=30, height=30, bg_color=self.TEXTBOX3.cget("fg_color"), fg_color=self.TEXTBOX3.cget("fg_color"), hover_color="#050505")
        self.copy.place(anchor="ne", y=10, relx=1, x=-10)

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk()
root.geometry("1500x800")
root.title("Snippet")
root.configure(fg_color=['gray92', '#050505'])

Search_entry = CTkEntry(root, placeholder_text="Search", width=775, height=57, border_width=0, corner_radius=10, font=CTkFont(size=20))
Search_entry.pack(pady=(100, 0))

a = Snippet(root, title="Hello World", description="Namaskaram", code="print('Hello World')", language="python")
a.pack()

root.mainloop()

