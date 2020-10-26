import requests
from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import base64
import io
from PIL import Image, ImageTk


class Space:

    def creategui(title, image, explanation, date, extension):
        """Creates a GUI that displays the image for your birthday"""
        root = Tk()

        Label(root, text = title, font = ('Arial', 32)).pack(side = TOP, pady = 10)
        Label(root, text = explanation, font = ('Arial', 12)).pack(side = BOTTOM, pady = 10)
        # dimensions for the image
        w = 700
        h = 1000
        x = 80
        y = 100
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        if extension == 'gif':
            # get the image for gifs
            imageX = urlopen(image).read()
            image64 = base64.encodebytes(imageX)
            photo = PhotoImage(data=image64)

            label = Label(root, image=photo)
            label.pack(padx=5, pady=5)
            mainloop()
        else:
            imageX = urlopen(image)
            # create an image file object
            imageF = io.BytesIO(imageX.read())
            # use PIL to open image formats like .jpg  .png  .gif  etc.
            pil_img = Image.open(imageF)
            # convert to an image Tkinter can use
            tk_img = ImageTk.PhotoImage(pil_img)
            # put the image on a typical widget
            label = Label(root, image=tk_img)
            label.pack(padx=5, pady=5)
            mainloop()

    # making requests to APOD API
    url = "https://api.nasa.gov/planetary/apod"
    params = {'date': '1997-10-29', 'api_key': '9nXZwpSBtQ5xCr6qDfGEZLRTUC2gh3jdkZpCFYlS'}#'DEMO_KEY'}
    response = requests.get(url, params)
    # create a python dictionary to be able to access specific responses
    image_info = response.json()
    date = image_info['date']
    title = image_info['title']
    image = image_info['hdurl']
    explanation = image_info['explanation']
    # variable to hold the file extension to determine
    extension = image[-3:]
    creategui(title, image, explanation, date, extension)







if __name__ == '__main__':
    Space
