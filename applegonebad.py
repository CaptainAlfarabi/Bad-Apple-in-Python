import cv2
import pygame


cap = cv2.VideoCapture("bad apple.mp4") # Display video, no audio


if (cap.isOpened() == False):  # Debug thingy
    print("Error opening video file")


pygame.init() # initialize pygame


pygame.mixer.music.load("bad apple.mp3") # loading in audio file.


pygame.mixer.music.play()  # playing the audio after it was loaded in


while(cap.isOpened()):
    ret, frame = cap.read() # reads each frame and returns boolean value 'ret' indicating if frame was succesfully read and frame itself
    if ret == True:
        
        cv2.imshow("Frame", frame) # displays image on screen. here, being used to display frames of video.
        
        if cv2.waitKey(25) & 0xFF == ord('q'): # I have no idea.
            break
    else:
        break

pygame.mixer.music.stop() # Stops playing audio.

cap.release()
cv2.destroyAllWindows()
