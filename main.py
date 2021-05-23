import gui

try:
    main_window = gui.Gui()
    main_window.run()
except Exception as e:
    from voice_recognition import VoiceRecognition
    voice_mode = VoiceRecognition()
    voice_mode.run()
