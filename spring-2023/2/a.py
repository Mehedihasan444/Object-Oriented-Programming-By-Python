chatGPT=dict()
# chatGPT.update({ "Hi!": "Hi! What can I do now?"})
chatGPT["Hi!"]="Hi! What can I do now?"
chatGPT.update({"Do you know me?": "You are from Daffodil International University. You are currently studying 5th semester."})
chatGPT.update({"Thanks for your information.": "Thanks for your gratitude"})
def demo_Chatgpt(question):
    if  question in chatGPT:
            print(chatGPT[question])
    else:
        print("Sorry, I don't have information related to that question.")
userInput=input()
demo_Chatgpt(userInput)