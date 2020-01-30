import speech_recognition as sr 
#the following name is only used as an example 
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
 with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
                         r.adjust_for_ambient_noise(source) 
    print "Say Something"
    #listens for the user's input 
    audio = r.listen(source) 
          
    try: 
        text = r.recognize_google(audio) 
        print "you said: " + text 
      
    #error occurs when google could not understand what was said 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google  
                                 Speech Recognition service; {0}".format(e)) 
