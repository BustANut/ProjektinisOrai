from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from WeatherAPI import weather


class BoxLayout1(AnchorLayout):
    pass


class OraiApp(App):
    def build(self):
        self.icon = "images/Weather_Icon.png"
        pass

    def on_click(self):
        if self.root.ids.textinput.text == '':
            pass
        elif self.root.ids.textinput.text.title() == self.root.ids.my_label.text:
            pass
        else:
            textinput = self.root.ids.textinput
            my_label = self.root.ids.my_label
            temperature = self.root.ids.temperature
            weather_type = self.root.ids.weather_type
            pressure = self.root.ids.pressure
            humidity = self.root.ids.humidity
            feels_like = self.root.ids.feels_like
            if weather(str(textinput.text)) == "404":
                textinput.text = "Nėra tokio miesto"
            else:
                my_label.text = str(textinput.text.title())
                temperature.text = str(str(weather(str(textinput.text))[1])) + "°"
                weather_type.text = str(str(weather(str(textinput.text))[0]))
                pressure.text = "Slėgis: " + str(str(weather(str(textinput.text))[2])) + " Pa"
                humidity.text = "Drėgmė: " + str(str(weather(str(textinput.text))[3])) + "%"
                feels_like.text = "Jaučiasi kaip: " + str(str(weather(str(textinput.text))[4])) + "°"
                textinput.text = ""


OraiApp().run()
