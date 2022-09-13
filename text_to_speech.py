from gtts import gTTS

text = input("Enter text: ")

myobj = gTTS(text=text, slow=False)

myobj.save("text.mp3")
