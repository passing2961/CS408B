from rasa_nlu.model import Interpreter

interpreter = Interpreter.load('./models/current/nlu')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))
    
# asking question
ask_question("안녕하세요")
ask_question("안녕")
ask_question("월정리에 친구랑 쉴만한 곳 있어?")    