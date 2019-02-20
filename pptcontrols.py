import pyautogui
from firebase import firebase
firebase = firebase.FirebaseApplication('https://ppts-65b0d.firebaseio.com/', None)
check1=-1
while True:
    
    result=(firebase.get('/ppts/ppt', None))
    check=(firebase.get('/ppts/check', None))
    print (result)
    print (check)
    if (check!=check1):
        if (result=="1"):
            pyautogui.press('f5')
        if (result=="2"):
            pyautogui.press('left')
        if (result=="3"):
            pyautogui.press('right')
        if (result=="4"):
            pyautogui.press('esc')
        check1=check
