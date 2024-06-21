# --Python Project To Generate User-Defined length Password--

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import string
import random

class PasswordGeneratorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label to prompt user to enter password length
        self.label = Label(text='Enter the length of the password:')
        self.layout.add_widget(self.label)

        # Text input for password length
        self.length_input = TextInput(multiline=False, input_filter='int', foreground_color=[0,0,1,1])
        self.layout.add_widget(self.length_input)

        # Button to generate password
        self.generate_button = Button(text='Generate Password', background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        self.generate_button.bind(on_press=self.generate_password)
        self.layout.add_widget(self.generate_button)

        # Label to display the generated password
        self.result_label = Label(text=' ', color=(1, 1, 1, 1))
        self.layout.add_widget(self.result_label)

        return self.layout

    def generate_password(self, instance):
        try:
            length = int(self.length_input.text)
            if length <= 0:
                self.result_label.text = 'Please enter a positive integer.'
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.text = f'Generated Password: {password}'
        except ValueError:
            self.result_label.text = 'Invalid input. Please enter a number.'

if __name__ == '__main__':
    PasswordGeneratorApp().run()
