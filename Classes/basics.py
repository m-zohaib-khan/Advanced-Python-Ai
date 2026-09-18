class llms:

    token_size=100

# constructor:
    def __init__(self, query):
        self.query=query

# methods:
    def openai(self):
        print("i am openai, you asked me: " + self.query)

    def claude(self):
        print("i am claude, you asked me: " + self.query)

    def ollama(self):
        print("i am ollama, you asked me: " + self.query)


# main code:
if __name__=="__main__":

    # create the object:
    obj1=llms("What is the capital of France?")
    obj1.claude()



