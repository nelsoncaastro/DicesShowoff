import kivy

kivy.require('1.10.0')

import os
import sys
import random
import kivy.resources
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

time = 1
bet = False
numeros = []
intentosrealizados = 0
intentosapostando = 0
intentossinapostar = 0
intentosganadosapostando = 0
intentosganadossinapostar = 0
totalganados = 0


class PopupNames(Popup):
    pass


class PopupCust(Popup):

    def betornot(self, do):
        global bet
        bet = do


class Pages(PageLayout):

    def throw(self):
        global time, intentosrealizados, intentosapostando, intentossinapostar, intentosganadosapostando, intentosganadossinapostar, totalganados
        dice = random.randint(1, 6)
        path = 'png/dice_' + str(dice) + '.png'
        if time == 1:
            self.ids.first.source = path
            numeros.append(dice)

        if time == 2:
            self.ids.second.source = path
            numeros.append(dice)

        if time == 3:
            self.ids.third.source = path
            numeros.append(dice)

        if time == 4:
            self.ids.fourth.source = path
            numeros.append(dice)

            intentosrealizados += 1
            if bet:
                intentosapostando += 1
                if numeros.__contains__(6):
                    self.ids.ganaroperder.text = 'Ganaste'
                    intentosganadosapostando += 1
                    totalganados += 1
                if not numeros.__contains__(6):
                    self.ids.ganaroperder.text = 'Perdiste'
            if not bet:
                intentossinapostar += 1
                if not numeros.__contains__(6):
                    self.ids.ganaroperder.text = 'Ganaste'
                    intentosganadossinapostar += 1
                    totalganados += 1
                if numeros.__contains__(6):
                    self.ids.ganaroperder.text = 'Perdiste'
            self.ids.labeel1.text = str(intentosrealizados)
            self.ids.labeel2.text = str(intentosapostando)
            self.ids.labeel3.text = str(intentossinapostar)
            self.ids.labeel4.text = str(intentosganadosapostando)
            self.ids.labeel5.text = str(intentosganadossinapostar)
            self.ids.labeel6.text = str(totalganados)

        time += 1

    def reset(self):
        global time
        time = 1
        path = 'png/dice_default.png'
        self.ids.ganaroperder.text = ''
        self.ids.first.source = path
        self.ids.second.source = path
        self.ids.third.source = path
        self.ids.fourth.source = path
        numeros.clear()
        PopupNames().open()


class DadosApp(App):

    def show_popup(self, dt):
        PopupNames().open()

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Clock.schedule_once(self.show_popup, 1)
        return Pages()


def resourcePath():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)
    return os.path.join(os.path.abspath("."))


if __name__ == '__main__':
    kivy.resources.resource_add_path(resourcePath())
    DadosApp().run()
