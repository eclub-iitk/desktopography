#import opencv
import pyautogui
import webbrowser
webbrowser.open("http://localhost:8888/",new=2)

for i in range(5):
    #pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
    pyautogui.moveTo(825, 780-80*i, 2, pyautogui.easeOutQuad)
    pyautogui.click(x=825,y=780-80*i)
