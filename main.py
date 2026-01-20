from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

#Setting the Size of the window
Window.size = (400, 600)

#Body of the App
class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical' ,**kwargs) #Sets the orientation of the app to vertical

        self.result = TextInput(
            font_size = 45,
            size_hint_y = 0.2,
            multiline = False,
            readonly = True,
            halign = "right",
            background_color = [0.2,0.2,0.2,1],
            foreground_color = [1,1,1,1],
        )

        self.add_widget(self.result)

        #Create the buttons
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]
        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for item in row:
                button = Button(
                    text = item,
                    font_size = 32,
                    background_color = self.set_button_color(item),
                    on_press = self.button_click

                )
                grid.add_widget(button)
        
        self.add_widget(grid)

    #Various button color
    def set_button_color(self, label):
        if label in {'C', '+/-', '%'}:
            return [0.6,0.6,0.6,1]
        elif label in {'/', '*', '-', '+', '='}:
            return [1,0.65,0,1]
        return [0.3,0.3,0.3]

    #button functionality
    def button_click(self, instance):
        text = instance.text

        if text == "C":
            self.result.text =""
            pass
        elif text == "=":
            self.Calculate()
            
        elif text == "+/-":
            self.Insert_neg()
            
        elif text == "%":
            self.Calc_Percentage()
        else:
            self.result.text += text

    #Calculate
    def Calculate(self):
        try:
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error!"

    #Insert negative before a number
    def Insert_neg(self):
        if self.result.text:
            self.result.text = self.result.text[1:] if self.result.text[0] == "-" else "-" + self.result.text

    #Calculate Percentage
    def Calc_Percentage(self):
        try:
            self.result.text = str(float(self.result.text)/100)
        except ValueError:
            self.result.text = "Error!"

#The Calc Constructor
class CalculatorApp(App):
    def build(self):
        return Calculator()
    

if __name__ == "__main__":
    CalculatorApp().run()