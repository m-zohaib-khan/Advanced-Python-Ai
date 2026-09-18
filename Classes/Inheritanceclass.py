# import the parent class:
from first_class import llms

class chatbot(llms):

# constructor:
    def __init__(self, model, query):
        llms.__init__(self,query)
        self.model = model


#  chat method:
    def chat(self):
        if self.model == "openai":
            print("You are using OpenAI model.")
            self.openai()
        elif self.model == "claude":
            print("You are using Claude model.")
            self.claude()
        elif self.model == "ollama":
            print("You are using Ollama model.")
            self.ollama()
        else:
            print("Unknown model: " + self.model)


# create the objects:
obj1 = chatbot("openai", "What is the capital of France?")
obj2 = chatbot("claude", "What is the capital of Germany?")
obj3 = chatbot("ollama", "What is the capital of Japan?")

# call the methods:
# obj1.chat()
# obj2.chat()
obj3.chat()
