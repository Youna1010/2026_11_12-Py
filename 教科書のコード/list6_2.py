import tkinter

img = [None]*14
card = [0]*26

def draw_card():
    for i in range(26):
        x = (i%7)*120+60
        y = int(i/7)*168+84
        cvs.create_image(x, y, image=img[card[i]])

def shuffle_card():
    for i in range(26):
        card[i] = 1+i%13

def resize_image(photo, target_w=120, target_h=168):
    w, h = photo.width(), photo.height()
    z = max(1, (w + target_w - 1) // target_w, (h + target_h - 1) // target_h)
    sub = photo.subsample(z, z)
    to_x = max(0, (target_w - sub.width()) // 2)
    to_y = max(0, (target_h - sub.height()) // 2)
    new_img = tkinter.PhotoImage(width=target_w, height=target_h)
    new_img.tk.call(new_img, 'copy', sub, '-zoom', 1, 
                   '-from', 0, 0, min(sub.width(), target_w), min(sub.height(), target_h), 
                   '-to', to_x, to_y)
    return new_img

root = tkinter.Tk()
root.title("神経衰弱")
root.resizable(False, False)
cvs = tkinter.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    src = tkinter.PhotoImage(file="card/"+str(i)+".png")
    img[i] = resize_image(src, 120, 168)
shuffle_card()
draw_card()
root.mainloop()