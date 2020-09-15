import PIL
from PIL import Image,ImageFont,ImageDraw
import facebook
import random
import os
import schedule
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from colorama import Fore, Back, Style
import string

def job():
    # PARTEA CARE SE REFERA LA DESENAREA PLANETEI

    space=Image.new('RGBA',(1200,675),color=(random.randint(0,40), random.randint(0,40), random.randint(0,40))) # -> culoarea universului
    space.save('space.bmp')

    # Ia poza cu spatiul creata
    import matplotlib.cbook as cbook
    image_file = cbook.get_sample_data('C:/Users/Tiberiu/Desktop/NoBotsSky/space.bmp')
    img = plt.imread(image_file)

    # PLANETE + STELE creare

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    ax.imshow(img)

    size_of_planet=random.choice([100,500,1000,1500,2000,2500,3000,4000,7000,7250,7500,7750,8000,8250,8500,8750,9000,9500,10000,10500,11000,11500,12000,12000,12500,13000,30000,40000,45000,50000])
    plt.scatter(600, 337, color=(random.random(), random.random(), random.random()), s=size_of_planet)

    ok=11
    while ok >= 10:
        plt.scatter(random.randint(1, 1200), random.randint(1, 675), c='white')
        plt.scatter(random.randint(1,1200), random.randint(1,675), c='white')
        plt.scatter(random.randint(1, 1200), random.randint(1, 675), c='white')
        plt.scatter(random.randint(1, 1200), random.randint(1, 675), c='white')
        ok=random.randint(5,30)

    # PARTEA CARE SE REFERA LA COSTUMIZAREA SPATIULUI - sateliti naturali

    while ok <= 6:
        sizeaux = random.choice([100,500,1000,1500,2000])
        plt.scatter(random.randint(450, 750), random.randint(230, 440), color=(random.random(), random.random(), random.random()), s=sizeaux)
        ok = random.randint(5, 9)

    # Salveaza imaginea
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                        hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig("spaceYplanet.png", bbox_inches='tight', pad_inches=0)

    # PARTEA CARE SE REFERA LA COSTUMIZAREA PLANETEI

    msg = 'New system discovered: '

    # texturi
    ok = random.randint(0,3)
    if size_of_planet > 6500 and size_of_planet <= 13000 and ok >= 1:
        ok=random.randint(1,10)
        if ok < 10:
            img_rand_texture = random.choice(os.listdir("C:/Users/Tiberiu/Desktop/nobotssky/textures"))
            foreground1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/textures/" + img_rand_texture).convert("RGBA")
            background1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/spaceYplanet.png").convert("RGBA")

            size_of_planet2 = int(size_of_planet / 65)

            foreground1 = foreground1.resize((size_of_planet2, size_of_planet2), Image.ANTIALIAS)

            img_w, img_h = foreground1.size
            bg_w, bg_h = background1.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            background1.paste(foreground1, offset, foreground1)
            background1.save("spaceYplanet.png")
        else:
            img_rand_texture = random.choice(os.listdir("C:/Users/Tiberiu/Desktop/nobotssky/texturesrare"))
            msg = 'New ULTRA RARE system discovered: '
            foreground1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/texturesrare/" + img_rand_texture).convert("RGBA")
            background1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/spaceYplanet.png").convert("RGBA")

            size_of_planet2 = int(size_of_planet / 65)

            foreground1 = foreground1.resize((size_of_planet2, size_of_planet2), Image.ANTIALIAS)

            img_w, img_h = foreground1.size
            bg_w, bg_h = background1.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            background1.paste(foreground1, offset, foreground1)
            background1.save("spaceYplanet.png")

    #altele

    ok=random.randint(1,26)
    if ok >= 20 and size_of_planet <= 15000 and size_of_planet > 2000: # inele

        img_rand_texture = random.choice(os.listdir("C:/Users/Tiberiu/Desktop/nobotssky/rings"))

        foreground1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/rings/" + img_rand_texture).convert("RGBA")
        background1 = Image.open("C:/Users/Tiberiu/Desktop/nobotssky/spaceYplanet.png").convert("RGBA")

        size_of_planet2 = int(size_of_planet / 25)
        foreground1 = foreground1.resize((size_of_planet2, size_of_planet2), Image.ANTIALIAS)

        img_w, img_h = foreground1.size
        bg_w, bg_h = background1.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

        background1.paste(foreground1, offset, foreground1)
        background1.save("spaceYplanet.png")


    # Resize a imaginii
    img2 = Image.open('C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet.png')

    height= 360
    width= 640

    new_width = 1200
    new_height = int(new_width * height / width)

    new_height = 675
    new_width = int(new_height * width / height)

    img2 = img2.resize((new_width, new_height), Image.ANTIALIAS)
    img2.save('spaceYplanet2.png')

    # PARTEA CARE GENEREAZA SI PUNE NUMELE

    img3 = Image.open("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet2.png")
    font_type=ImageFont.truetype("C:/Windows/Fonts/lucon.ttf",35)
    draw = ImageDraw.Draw(img3)

    random_name = random.choice(open("names.txt").readlines())
    while random_name.strip() is "":
        random_name = random.choice(open("names.txt").readlines())
    random_name = random_name.strip()

    name=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + random_name

    ok=random.randint(0,10)
    if ok >= 7:
        name = name + " " + str(random.randint(1,9))

    draw.text(xy=(795,502),text= name,fill="white",font=font_type) #<-- RANDOM

    img3.save("spaceYplanet3.png")

    # PARTEA CARE PUNE NAVETA SPATIALA

    background = Image.open("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet3.png")
    foreground = Image.open("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceship.png")

    background.paste(foreground, (0, 0), foreground)
    background.save("memev1.png")

    # PARTEA CARE SE REFERA LA POSTAREA PE FACEBOOK
    # """
    access_token = 'Not today, bud.'
    graph = facebook.GraphAPI(access_token)
    msg = msg + name
    post_id = graph.put_photo(image = open("C:/Users/Tiberiu/Desktop/NoBotsSky/memev1.png", 'rb'), message= msg)["post_id"]
    print('Poza a fost postata!')

    comment_msg = "Jason, the engineer who witnessed Nobotsky’s recent message, has brought the original team back to the base, to realise what they have missed. It is speculated that Nobotsky has entered a black hole, that sent him to the far edge of the Pinwheel galaxy, thus adding millions of light-years between Earth and the previously registered location of Nobotsky. To our delight, on its journey, our bot has captured tons of images, describing the various planets he discovered. Sadly, not all of the planets fit the criteria of life sustainability, but that does not stop Nobotsky.  Jason, after working tirelessly, has connected Nobotsky to the World Wide Web, to show the world what he is finding, with no delay."
    graph.put_comment(object_id=post_id, message=comment_msg)
    
    comment_msg = "20 years ago, Nobotsky started his journey through the galaxy, seeking a special planet, one that would accommodate human life. In the year 2016, the base has received its last message, simply saying:”NO!”. Today, after 4 years of total silence, one of the last members of the team that launched Nobotsky checked his computer. To his surprise, he has received an image from our mighty bot, a picture he is now proud to share with us."
    graph.put_comment(object_id = post_id, message = comment_msg)
    # """

    # PARTEA CARE SE REFERA LA STERGEREA IMAGINII - DONE

    try:
        os.remove("C:/Users/Tiberiu/Desktop/NoBotsSky/memev1.png")
    except:
        pass
    try:
        os.remove("C:/Users/Tiberiu/Desktop/NoBotsSky/space.bmp")
    except:
        pass
    try:
        os.remove("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet.png")
    except:
        pass
    try:
        os.remove("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet2.png")
    except:
        pass
    try:
        os.remove("C:/Users/Tiberiu/Desktop/NoBotsSky/spaceYplanet3.png")
    except:
        pass

    print ('Ciclu efectuat!')
    # background.show()
    plt.close('all')

# PARTEA CARE SE REFERA LA POSTAREA LA UN ANUMIT INTERVAL DE TIMP

schedule.every(20).minutes.do(job).run()
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        pass
