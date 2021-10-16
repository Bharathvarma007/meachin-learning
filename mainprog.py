from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
a = pd.read_csv('cand.csv')    # readind csv using pandas
font = ImageFont.truetype('arial.ttf',25) #setting fonts
f1 = ImageFont.truetype('arial.ttf',18)
for index,j in a.iterrows():        #for itterates through each colum
    img = Image.open('cer.jpg')     #opening the image on to which we write
    draw = ImageDraw.Draw(img)      #writing on the image
    #--------coord(x,y)---text to be written from respective colum----color----font--
    draw.text(xy=(175,253),text='{}'.format(j['NAME']),fill=(128,128,128),font=font)
    draw.text(xy=(154,355),text='{}'.format(j['DATE']),fill=(128,128,128),font=f1)
    draw.text(xy=(350,359),text='{}'.format(j['SIG']),fill=(128,128,128),font=f1)
    img.save('pictures/{}.jpg'.format(j['NAME']))#saving the images
