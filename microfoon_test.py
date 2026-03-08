import speech_recognition as sr

r = sr.Recognizer()

print('Beschikbare microfoons:')
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'{i}: {name}')

mic_index = 0
