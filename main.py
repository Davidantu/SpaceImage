import requests
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from urllib.request import urlopen
import io
from PIL import Image, ImageTk
from time import strptime


class Space:

    def __init__(self, title, image, explanation, date):
        self.title = title
        self.image = image
        self.explanation = explanation
        self.date = date

    @staticmethod
    def askBirthday():
        """Creates a window to ask for the users birthday"""

        def close_window():
            """Checks to make sure all of the fields were filled out before closing"""
            if m.get() == 'Month' or y.get() == 'Year' or d.get() == 'Date':
                messagebox.showerror('Error', 'Please fill out all fields').center(450,100)
            else:
                root.destroy()

        root = Tk()
        root.title('Space Image')
        root.geometry("500x500+450+150")

        Label(root, text="Date must be between Jun 16, 1995 and today's date", foreground='red', font=('Futura', 15)).pack(side=BOTTOM, pady=10)

        label1 = Label(root, text="Birthday", font =('Futura', 25))
        label1.pack(side=TOP,padx = 100)

        # creating lists for the drop down menu
        year = list(range(1994, 2021))
        month = [
            '',
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Dec'
        ]
        date = list(range(0,31))

        y = StringVar()
        m = StringVar()
        d = StringVar()

        dropdownY = OptionMenu(root, y, *year)
        dropdownY.config(width=8)
        y.set('Year')
        dropdownY.place(x=320, y=90)

        dropdownD = OptionMenu(root, d, *date)
        dropdownD.config(width=8)
        d.set('Date')
        dropdownD.place(x=200, y=90)

        dropdownM = OptionMenu(root, m, *month)
        dropdownM.config(width=8)
        m.set('Month')
        dropdownM.place(x=80, y=90)

        Button(root, text='Submit', width=10, command = close_window).pack(side=BOTTOM)

        nasa = ImageTk.PhotoImage(file="Images/nasa-logo-web-rgb.png")
        panel = Label(root, image=nasa)
        panel.pack(padx=10, pady=80)
        root.mainloop()

        mon = strptime(m.get(), '%b').tm_mon
        # format the month number to be 2 digits
        if mon in range(1,9):
            mon = str(mon)
            mon = '0' + mon
        # combine the date
        officialDate = y.get() + '-' + str(mon) + '-' + d.get()

        return officialDate

    def zellersCongruence(self, birthDate):
        """Uses Zeller's Congruence Algorithm to determine the day of the week in which you were born
        based on the Gregorian calendar"""

        # holds all of the potential days of the week
        potentialDays = {
            0: "Saturday",
            1: "Sunday",
            2: "Monday",
            3: "Tuesday",
            4: "Wednesday",
            5: "Thursday",
            6: "Friday"
        }
        year = int(birthDate[:4])
        if int(birthDate[5]) != 0:
            month = int(birthDate[5:7])
        else:
            month = int(birthDate[6:7])
        if len(birthDate) == 10:
            day = int(birthDate[8:10])
        elif len(birthDate) == 9:
            day = int(birthDate[8:9])

        # Jan and Feb are looked at as months 13 and 14
        if month == 1:
            month = 13
            year = year - 1

        if month == 2:
            month = 14
            year = year - 1

        # q is the day of the month
        q = day
        # m is the month
        m = month
        # k is the century
        k = year % 100
        # j is the zero-based century
        j = year // 100

        # plug in values to Zeller's Congruence formula
        # h is the day of the week
        h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        return potentialDays[h]

    def creategui(self):
        """Creates a GUI that displays the image for your birthday"""
        root = Tk()
        root.title('Astronomy Picture of the Day')
        Label(root, text = self.title, font = ('Futura', 25)).pack(side = TOP, pady = 10)
        Label(root, text = 'You were born on a ' + self.date, foreground = 'blue', font = ('Futura', 20)).pack(side = TOP, pady = 10)
        t = Text(root, height = 5, width = 150, font = ('Futura', 16))
        t.pack(side = BOTTOM, pady = 15)
        t.insert(tkinter.END, self.explanation)
        # dimensions for the image
        root.geometry("1000x1000+200+100")

        imageX = urlopen(self.image)
        # create an image file object
        imageF = io.BytesIO(imageX.read())
        # use PIL to open image formats like .jpg  .png  .gif  etc.
        pil_img = Image.open(imageF)
        pil_img.thumbnail((600,600), Image.LANCZOS)
        # convert to an image Tkinter can use
        tk_img = ImageTk.PhotoImage(pil_img)

        # put the image on a label
        label = Label(root, image=tk_img)
        label.pack(padx=5, pady=5)
        root.mainloop()


# making requests to APOD API
bday = Space.askBirthday()
url = "https://api.nasa.gov/planetary/apod"
params = {'date': '', 'api_key': 'DEMO_KEY'}
params['date'] = bday
response = requests.get(url, params)

# create a python dictionary to be able to access specific responses
image_info = response.json()
date1 = image_info['date']
title1 = image_info['title']
image1 = image_info['hdurl']
explanation1 = image_info['explanation']
spaceX = Space(title1, image1, explanation1, date1)
spaceX.date = spaceX.zellersCongruence(bday)
spaceX.creategui()






if __name__ == '__main__':
    Space
