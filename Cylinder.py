from tkinter import messagebox
import sys


class Cylinder:
    def __int__(self, radius = 0.0, height = 0.0):
        self.__radius = radius
        self.__height = height

    @property
    def radius(self):
        print("radius getter")
        return self.__radius

    @property
    def height(self):
        print("height getter")
        return self.__height

    @radius.setter
    def radius(self, radius):
        print("radius setter")
        self.__radius = radius

    @   height.setter
    def height(self, height):
        print("height setter")
        self.__height = height


    @staticmethod
    def is_number(user_input):
        try:
            i = float(user_input)
            if i > 0:
                return True
        except ValueError:
            return False

    def get_user_input_radius(self, user_input):
        if self.is_number(user_input):
            self.radius = float(user_input)
        else:
            if messagebox.showerror("Viga", "Raadius on vigane. Raadius peab olema positiivne arv."):
                sys.exit(1)

    def get_user_input_height(self, user_input):
        if self.is_number(user_input):
            self.height = float(user_input)
        else:
            if messagebox.showerror("Viga", "Kõrgus on vigane. Kõrgus peab olema positiivne arv."):
                sys.exit(1)


