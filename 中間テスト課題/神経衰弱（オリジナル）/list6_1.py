import tkinter

img = [None]*14

def draw_card():
    cvs.delete("all")
    for i in range(14):
        x = (i % 7) * 120 + 75
        y = int(i / 7) * 150 + 100
        cvs.create_image(x, y, image=img[i])

def resize_image(photo, target_w=100, target_h=130):
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
root.title("6-1: 画像ファイルを扱う")
root.resizable(False, False)

cvs = tkinter.Canvas(width=900, height=400, bg="#252526")
cvs.pack()

for i in range(14):
    path = "中間テスト課題/神経衰弱（オリジナル）/card/" + str(i) + ".png"
    src = tkinter.PhotoImage(file=path)
    img[i] = resize_image(src, 100, 130)

draw_card()
root.mainloop()