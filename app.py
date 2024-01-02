from tkinter import *
from tkinter import ttk, messagebox
import googletrans

languages = googletrans.LANGUAGES
lang_list = list(languages.values())

root = Tk()
root.title("Python Translator")

w = 1060
h = 380
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))

root.geometry(f"{w}x{h}+{x}+{y}")
root.configure(bg="white")
root.resizable(0,0)

def translate_text():
    try:
        # Get text area text and selected options
        text = text_area1.get(1.0, END)
        select1 = selecter_lang1.get()
        select2 = selecter_lang2.get()

        # Check if the text is empty
        if len(text) != 1:
            # Translate the text using the googletrans library
            translator = googletrans.Translator()
            translated_words = translator.translate(text, src=select1, dest=select2)

            # Updates the text area with the translated text.
            text_area2.delete(1.0, END)
            text_area2.insert(END, translated_words.text)
        else:
            messagebox.showerror("Translator", "No text to translate.")

    except Exception as e:
        messagebox.showerror("Translator", f"An error occurred while trying to translate the text. \n Error: {e}!")

#icon
image_icon = PhotoImage(file="./img/icon.png")
root.iconphoto(False, image_icon)

#Img
img = PhotoImage(file="./img/translate.png")
img_label = Label(root, image=img, width=130, height=130, bg='white')
img_label.place(x=465, y=80)

selecter_lang1 = ttk.Combobox(root, values=lang_list, font=("Times New Roman", 12), state="r")
selecter_lang1.place(x=125, y=45)
selecter_lang1.set("Select a language...")

f1 = Frame(root, bg="#A0CCF7", bd=5)
f1.place(x=10, y=75, width=440, height=210)

text_area1 = Text(f1, font=("Times New Roman", 13), bg="white", relief="flat", wrap="word")
text_area1.place(x=0, y=0, width=430, height=200)
text_area1.insert(END, "Enter Text...")

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text_area1.yview)
text_area1.configure(yscrollcommand=scrollbar1.set)

f2 = Frame(root, bg="#A0CCF7", bd=5)
f2.place(x=610, y=75, width=440, height=210)

text_area2 = Text(f2, font=("Times New Roman", 13), bg="white", relief="flat", wrap="word")
text_area2.place(x=0, y=0, width=430, height=200)
text_area2.insert(END, "Translation")

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text_area1.yview)
text_area2.configure(yscrollcommand=scrollbar2.set)

selecter_lang2 = ttk.Combobox(root, values=lang_list, font=("Times New Roman", 12), state="r", style="info.TCombobox")
selecter_lang2.place(x=750, y=45)
selecter_lang2.set("Select a language...")

translate = Button(root, text="Translate", font=("Times New Roman", 12), cursor="hand2", bd=5, bg="#248CF3", fg="white", activebackground="#68AFF5", activeforeground="white", command=translate_text)
translate.place(x=500, y=210)

root.mainloop()