from pynput.keyboard import Controller,Key,Listener
from string import ascii_lowercase,ascii_uppercase
from win10toast import ToastNotifier
from textblob import Word
import win32console,win32gui

# Confidence based correction system
# Keyboard hooks for auto-correction
# "Is it a mistake really?" algorithm
# Processing in background capability


class Prometheus:
    def __init__(self):
        self.controller = Controller()
        self.notifier = ToastNotifier()
        self.upperLetters = [*ascii_uppercase]
        self.lowerLetters = [*ascii_lowercase]
        self.letters = []
        self.lastWord = ""
        self.lastCorrectedWord = "" 
        self.dismissable = False

    def on_press(self,key):
            # This try and except statement handles the filter that cleans 'Key' instances
            try:
                # This handles the filter that cleans 'KeyCode' instances
                if key.char in self.upperLetters or key.char in self.lowerLetters:
                    if not self.dismissable:
                        self.letters.append(key.char)
            except:pass

    def touch(self,key):
        self.controller.press(key)
        self.controller.release(key)

    def fix_word(self):
        pass

    def on_release(self,key):
        if len(self.letters) != 0:
            if key == Key.space or key == Key.enter:
                word = "".join(letter for letter in self.letters)
                self.letters = []
                #print("[+] Found word while typing : "+word)
                wordL = Word(word).spellcheck()[0][0]
                if wordL != word:
                    if word != self.lastWord and self.lastCorrectedWord != wordL:
                        self.lastWord = word
                        self.lastCorrectedWord = wordL
                        for _ in range(len([*word]) + 1):
                            self.touch(Key.backspace)
                        self.dismissable = True
                        self.controller.type(wordL)
                        self.dismissable = False
                        self.touch(Key.space) if key == Key.space else self.touch(Key.enter)
            if key == Key.backspace:
                self.letters.pop()

    def hook(self):
        self.listener = Listener(self.on_press,self.on_release)
        self.listener.start()
        self.notifier.show_toast(title="Prometheus",msg="PE and RE hooks are initialized.",threaded=True)



if __name__ == "__main__":
    corrector = Prometheus()
    corrector.hook()
    win32gui.ShowWindow(win32console.GetConsoleWindow(),0)
    #print("[+] Hooks injected.")
    corrector.listener.join() 





