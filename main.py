import requests
from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import base64

class Space:

    def creategui(title, image, explanation, date):
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

        #get the image
        imageX = urlopen(image).read()
        image64 = base64.encodebytes(imageX)
        photo = PhotoImage(data=image64)

        #put the image onto a canvas
        cv = Canvas(bg='white')
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(10, 10, image=photo, anchor='nw')
        mainloop()



    # making requests to APOD API
    url = "https://api.nasa.gov/planetary/apod"
    params = {'date': '1997-10-29', 'api_key': '9nXZwpSBtQ5xCr6qDfGEZLRTUC2gh3jdkZpCFYlS'}
    response = requests.get(url, params)
    # create a python dictionary to be able to access specific responses
    image_info = response.json()
    date = image_info['date']
    title = image_info['title']
    image = image_info['hdurl']
    explanation = image_info['explanation']
    creategui(title, image, explanation, date)







if __name__ == '__main__':
    Space
