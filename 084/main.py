from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont


def open():
    x = openfilename()
    name = x.split("/")[-1]
    img = Image.open(x)
    (width, height) = (img.width // 2, img.height // 2)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = img.convert('RGBA')
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("Arial Unicode.ttf", 80)
    txt = text.get()
    textwidth, textheight = d.textsize(txt, fnt)
    width, height = img.size
    x = width / 2 - textwidth / 2
    y = height - textheight - 300
    fname = f'wm{name}'
    t = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(t)
    d.text((x, y), txt, fill=(255, 255, 255, 125), font=fnt)
    watermarked = Image.alpha_composite(img, t)
    watermarked.save(fname)
    img = Image.open(fname)
    img = ImageTk.PhotoImage(img)
    panel = Label(w, image=img)
    panel.image = img
    panel.grid(row=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='Open')
    return filename


def focus(event):
    text.selection_range(0, END)


# Create window
w = Tk()
w.title("Apply Watermark")
w.minsize(width=200, height=100)
w.config(padx=20, pady=20)
# Set the resolution of window
w.geometry("1024x768")

# Allow Window to be resizable
w.resizable(width=True, height=True)

text = Entry(borderwidth=1, relief=SUNKEN, width=100)
text.grid(column=0, row=0)
text.insert(END, "HiTekRedneck.io")
text.bind("<FocusIn>", focus)
# Create a button and place it into the window using grid layout
btn = Button(w, text='open image', command=open).grid(
    row=1, columnspan=2)



w.mainloop()