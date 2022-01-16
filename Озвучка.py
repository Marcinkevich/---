import pyttsx3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
engine = pyttsx3.init()
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', ru_voice_id)

engine.say('')
engine.runAndWait()

engine.runAndWait()

class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name) 
		vl = BoxLayout(orientation='vertical')
		btn = Button(text='Озвучить')
		btn.on_press = self.Voice
		self.txt = TextInput()
		btnHome = Button(text="Домашние фразы")
		btnStreet = Button(text="Уличные фразы")
		btnSOS = Button(text="SOS",
			font_size ="20sp", 
            background_color =(1, 0, 0, 1))
		btnSOS.on_press = lambda : self.Say('SOS')   

		vl.add_widget(self.txt)
		vl.add_widget(btn)
		vl.add_widget(btnHome)
		vl.add_widget(btnStreet)
		vl.add_widget(btnSOS)
		

		self.add_widget(vl)

		btnHome.on_press = self.toHome
		btnStreet.on_press = self.toStreet

	def Voice(self):
		global engine
		t = self.txt.text
		engine.say(t)
		engine.runAndWait()

	def toHome(self):
		self.manager.transition.direction = 'left' 
		self.manager.current = 'home'

	def toStreet(self):
		self.manager.transition.direction = 'left' 
		self.manager.current = 'street'

	def Say(self, text):
		global engine
		engine.say(text)
		engine.runAndWait()


class HomeScr(Screen):
	def __init__(self, name='home'):
		super().__init__(name=name) 
		v1 = BoxLayout(orientation='vertical')
		btnDrink = Button(text='Хочу пить')
		btnDrink.on_press = lambda : self.Say('Хочу пить')
		btnDamn = Button(text='Иди к чёрту!')
		btnDamn.on_press = lambda : self.Say('Иди к чёрту!')
		btnK = Button(text='Переключиться на Уличные фразы')
		btnK.on_press = lambda : self.Say('Переключиться на Уличные фразы')
		btnK.on_press = self.toStreet
		btnS = Button(text='Переключиться на Начальный экран')
		btnS.on_press = lambda : self.Say('Переключиться на Начальный экран')
		btnS.on_press = self.next

		v1.add_widget(btnS)
		v1.add_widget(btnDrink)
		v1.add_widget(btnDamn)
		v1.add_widget(btnK)
		self.add_widget(v1)

	def Say(self, text):
		global engine
		engine.say(text)
		engine.runAndWait()

	def toStreet(self):
		self.manager.transition.direction = 'left' 
		self.manager.current = 'street'

	def next(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first'

		
class StreetScr(Screen):
	def __init__(self, name='street'):
		super().__init__(name=name) 
		v1 = BoxLayout(orientation='vertical')
		btnDeath = Button(text='Убейте меня!')
		btnDeath.on_press = lambda : self.Say('Убейте меня!')
		btnH = Button(text='Пошли домой!')
		btnH.on_press = lambda : self.Say('Пошли домой!')
		btnR = Button(text='Переключиться на Домашние фразы')
		btnR.on_press = lambda : self.Say('Переключиться на Домашние фразы')
		btnR.on_press = self.toHome
		btnS = Button(text='Переключиться на Начальный экран')
		btnS.on_press = lambda : self.Say('Переключиться на Начальный экран')
		btnS.on_press = self.next

		v1.add_widget(btnS)

		v1.add_widget(btnDeath)
		v1.add_widget(btnH)
		v1.add_widget(btnR)
		self.add_widget(v1)

	def Say(self, text):
		global engine
		engine.say(text)
		engine.runAndWait()

	def toHome(self):
		self.manager.transition.direction = 'right' 
		self.manager.current = 'home'

	def next(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first'

		
class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(FirstScr())
		sm.add_widget(HomeScr())
		sm.add_widget(StreetScr())
		return sm

app = MyApp()
app.run()