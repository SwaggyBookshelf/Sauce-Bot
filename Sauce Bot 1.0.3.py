from PIL import ImageDraw
import PIL.Image
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from collections import Counter
import webbrowser
import functools
#uncomment for compiling
#import pyi_splash



config = open("preferences.config", "rt")
lines = config.readlines()

for line in lines:
    
    if line.split(" : ")[0] == "default path":
        defaultDirectory = line.split(" : ")[1].split("//")[0].lstrip(" ")
        
    if line.split(" : ")[0] == "hentai website":
        website = line.split(" : ")[1].split("//")[0].lstrip(" ")
        
    if line.split(" : ")[0] == "textbox click":
        highlight = int(line.split(" : ")[1].split("//")[0].lstrip(" "))



def Open():

    filename = filedialog.askopenfilename (initialdir = defaultDirectory,
                                           filetypes = (('Lossless Image', '*.png *.tiff *.tif *.bmp'),
                                                        ('Image', '*.png *.jpg *.jepg *.jpe *.jfif *.exif *.tiff *.tif *.webp *.bmp *.bid *.rle *.gif'),
                                                        ('All', '*.*')))
    if filename == "":
        return

    img  = PIL.Image.open(filename)

    img_rgb = img.convert('RGB')
    width, height = img.size
    red, green, blue = [], [], []
    rgb = []

    for i in range(0,width):
        for j in range(0,height):
            
            r, g, b = img_rgb.getpixel((i, j))
            rgb.append(str(r).zfill(2)+str(g).zfill(2)+str(b).zfill(2))
            
    occurence_count = Counter(rgb) 
    avg_rgb = occurence_count.most_common(1)[0][0]

    sauce=str(int(avg_rgb[0:2]+avg_rgb[2:4]+avg_rgb[4:6]))
    webbrowser.open(website+sauce)
    return



def Create():
    
    if rgb.get().isnumeric() == False:
        return
    
    want_hexadec = wanthex.get()
    red_green_blue = rgb.get()
    want_message = wantmessage.get()
    custom_message = message.get()

    red_green_blue = red_green_blue.zfill(6)
    
    red = int (red_green_blue [0:2])
    green = int (red_green_blue [2:4])
    blue = int (red_green_blue [4:6])

    message_final, hexadec, extra_lines = str(), str(), 0

    if want_hexadec:

        hexadec = "#" + hex(red).zfill(4) + hex(green).zfill(4) + hex(blue).zfill(4)
        hexadec = hexadec.replace("0x","")
                
    if want_message:
        if len(custom_message) > 13:
            
            loop, looped = 0, 0
            message_components = list(custom_message.split(" "))
            
            for word_no in range(len(message_components)):
                if len(message_final)-loop*13+len(message_components[word_no]) < 14:
                    message_final += (message_components[word_no]+" ")

                else:    
                    while_loop=0
                    while len(message_components[word_no])-int(while_loop)*12 > 13:
                        
                        message_final += "\n"*looped+message_components[word_no][0+12*while_loop:12+12*while_loop]+"-"
                        loop += 1
                        while_loop += 1
                        looped=1
                        
                    message_final += "\n"+message_components[word_no][0+12*while_loop:]+" "
                    loop += 1
                    looped = 1
                    
            if loop+want_hexadec > 5:
                extra_lines = int(loop+want_hexadec-5)
                
        else:
            message_final = custom_message
            
    img = PIL.Image.new("RGB", (100, 100+extra_lines*15), color = (red, green, blue))
    text = PIL.ImageDraw.Draw(img)
    text.text((10, 10), hexadec.upper()+"\n"*want_hexadec+message_final, fill = (255-red, 255-green, 255-blue))
    SaveFile (img)
    return



def SaveFile(image):
    filename = filedialog.asksaveasfilename (initialdir = defaultDirectory,
                                      defaultextension = '.png',
                                      filetypes = (('PNG', '*.png'),
                                                   ('JPEG', '*.jpg *.jepg *.jpe *.jfif *.exif'),
                                                   ('TIFF', '*.tiff *.tif'),
                                                   ('WebP', '*.webp')))
    if filename == "":
        return
    
    image.save(filename)
    return



def ClearBox(event):
    event.widget.delete (0, "end")
    
    if highlight == 0:
        event.widget.unbind ("<FocusIn>")
        return
    
    if highlight == 1:
        event.widget.unbind ("<FocusIn>")
        event.widget.bind ("<FocusIn>", HighlightBox)
        return
    
    return



def HighlightBox(event):
    event.widget.focus_set()
    event.widget.select_range(0,"end")



def ResetBox(event, string):
    if event.widget.get().strip("    ") == "":
        
        event.widget.delete(0, "end")
        event.widget.insert(0, string)
        event.widget.unbind ("<FocusIn>")
        event.widget.bind ("<FocusIn>", ClearBox)



#uncomment for compiling
#pyi_splash.close()

window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title('Sauce Bot')
window.wm_iconbitmap('n.ico')

frame1=Frame(window)
frame1.pack(side=TOP)

frame2=Frame(window)
frame2.pack(side=TOP)

Sauce = StringVar(frame1, value='Sauce')
rgb = tk.Entry(frame1, width=37, textvariable=Sauce)
rgb.bind("<FocusIn>", ClearBox)
rgb.bind("<FocusOut>", functools.partial(ResetBox, string="Sauce"))
rgb.pack(side=TOP)

wanthex=IntVar()
Checkbutton(frame1, text="Include hex", variable=wanthex).pack(side=LEFT)

wantmessage=IntVar()
Checkbutton(frame1, text="Custom message", variable=wantmessage).pack(side=LEFT)

MES = StringVar(frame1, value="Message")
message = tk.Entry(frame2, width=37, textvariable=MES)
message.bind("<FocusIn>", ClearBox)
message.bind("<FocusOut>", functools.partial(ResetBox, string="Message"))
message.pack(side=TOP)

Create=Button(frame2, text="Create", width=15, command=Create)
Open=Button(frame2, text="Open", width=15, command=Open)

Create.pack(side=tk.LEFT)
Open.pack(side=tk.LEFT)

window.mainloop() 
