from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import qns
from kivy.properties import NumericProperty, StringProperty


class MyQuizScreen(ScreenManager):
    pass


class MyQuiz(Screen):
    quiz_number = NumericProperty()
    next_question = StringProperty()
    quiz = qns.Quizzes


class FinalScore(Screen):
    score = NumericProperty(0)


class MyThirdApp(App):
    pass


if __name__ == "__main__":
    MyThirdApp().run()