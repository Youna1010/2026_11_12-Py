import tkinter
import random

img = [None]*14
card = [0]*26
face = [0]*26

def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 6) * 120 + 90
        y = int(i / 6) * 125 + 75
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        elif face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])

def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
        face[i] = 0
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]

def click(e):
    x = int((e.x - 30) / 120)
    y = int((e.y - 12) / 125)
    if 0 <= x and x <= 5 and 0 <= y and y <= 4:
        n = x + y * 6
        if n >= 26:
            return
        if face[n] == 0:
            face[n] = 1
        else:
            face[n] = 0
        draw_card()

def resize_image(photo, target_w=100, target_h=115):
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
root.title("6-4: クリックしてカードをめくる")
root.resizable(False, False)
root.bind("<Button>", click)

cvs = tkinter.Canvas(width=780, height=650, bg="#1E1E1E")
cvs.pack()

for i in range(14):
    path = "中間テスト課題/神経衰弱（オリジナル）/card/" + str(i) + ".png"
    src = tkinter.PhotoImage(file=path)
    img[i] = resize_image(src, 100, 115)

shuffle_card()
draw_card()
root.mainloop()