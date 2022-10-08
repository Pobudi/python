from PIL import Image as Pil_image, ImageTk as Pil_imageTk, ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog


def browse_files():
    global image, width_scale, right_value, img_name
    img_name = filedialog.askopenfilename(initialdir=".",
                                          title="Select a File",
                                          filetypes=(("jpeg files", "*.jpg"),
                                                     ("all files", "*.*")))
    image = Pil_image.open(img_name)
    # 0 - width, 1 - height
    if image.size[0] >= image.size[1]:
        image = image.resize((400, int(image.size[1]/image.size[0]*400)))
    else:
        image = image.resize((int(image.size[1]/image.size[0]*400), 400))
    photo = Pil_imageTk.PhotoImage(image=image)
    photo_preview.configure(image=photo, width=400, height=400)
    photo_preview.image = photo

    width_scale = Scale(container1, orient=HORIZONTAL, length=image.size[0], command=move_horizontal, to=image.size[0])
    width_scale.grid(row=0, column=0)

    right_value = IntVar()
    length_scale = Scale(container1, length=image.size[1], command=move_vertical, to=image.size[1], showvalue=0, variable=right_value)
    right_label = Label(container1, textvariable=right_value)
    length_scale.grid(row=1, column=1)
    right_label.grid(row=1, column=2)


def draw(xcor, ycor):
    global watermark_img
    watermark_img = image.copy()
    draw = ImageDraw.Draw(watermark_img)
    font = ImageFont.truetype("arial.ttf", int(font_var.get()))
    draw.text((xcor, ycor), watermark, (255, 255, 255), font=font)
    watermark_tk = Pil_imageTk.PhotoImage(image=watermark_img)
    photo_preview.configure(image=watermark_tk)
    photo_preview.watermark_tk = watermark_tk


def get_text():
    global watermark
    watermark = text_input.get(1.0, "end-1c")
    draw(width_scale.get(), right_value.get())


def move_horizontal(val):
    draw(width_scale.get(), right_value.get())


def move_vertical(val):
    draw(width_scale.get(), right_value.get())


def save():
    dir_name = filedialog.askdirectory(initialdir=".", title="Select a Directory")
    watermark_img.save(f"{dir_name}/water_{img_name.split('/')[-1]}")


window = Tk()
window.title("Watermark")
window.geometry("600x600")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

container1 = Frame(window)
container1.grid(column=0, row=0)

container2 = Frame(window)
container2.grid(column=0, row=1)

photo_preview = Label(container1)

button_explore = Button(container2, text="Browse Files", command=browse_files, width=20)
button_save = Button(container2, text="Save", command=save, width=20)
button_exit = Button(container2, text="Exit", command=exit, width=20)

text_input = Text(container2, height=1, width=20)
get_input = Button(container2, text="Put on photo", command=get_text)
font_var = StringVar(value=12)
font_size = Spinbox(container2, textvariable=font_var, from_=1, to=60, width=5)

photo_preview.grid(column=0, row=1)

text_input.grid(column=0, row=1, padx=10)
get_input.grid(column=1, row=1)
font_size.grid(column=2, row=1, padx=(10, 0))
button_explore.grid(column=0, row=2, pady=10)
button_save.grid(column=0, row=3)
button_exit.grid(column=0, row=4, pady=10)

window.mainloop()
