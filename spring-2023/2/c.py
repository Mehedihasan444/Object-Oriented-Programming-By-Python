chatGPT=dict()
# chatGPT.update({ "Hi!": "Hi! What can I do now?"})
chatGPT["Hi!"]="Hi! What can I do now?"
chatGPT.update({"Do you know me?": "You are from Daffodil International University. You are currently studying 5th semester."})
chatGPT.update({"Thanks for your information.": "Thanks for your gratitude"})
print(chatGPT)
chatGPT["Do you know me?"]=chatGPT["Do you know me?"].replace("5th", "7th")
print(chatGPT)
