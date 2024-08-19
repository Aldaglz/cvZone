import tkinter as tk # Python 3.x Version
from PIL import Image, ImageTk
import cv2
import imutils

print ("Librerias leidas...")
#Initialize a window
root = tk.Tk() 
root.geometry("1028x768+200+10")
root.title("S.T.A.R Technologies") # It printed name to the window
root.resizable(width=False, height=False)
fondo=tk.PhotoImage(file="S.T.A.R.png")
fondo1= tk.Label(root, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)


video= None

def video_stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

def iniciar():
    global video
    ret, frame = video.read()
    if ret == True:
        frame = imutils.resize(frame, width=470)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img= Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=img)
        etiq_de_video.configure(image=image)
        etiq_de_video.image = image
        etiq_de_video.after(1, iniciar)
    else:
        video.release()

def quitar():
    global video
    #etiq_de_video.place_forget()
    video.release()








#Colores
fondo_boton = "#fdfcff"

#Botones
BotonInicio = tk.Button(root, text="Iniciar Video", bg=fondo_boton, relief="flat",
                  cursor="hand2",command=video_stream, width=15, height=2, font=("Calisto MT",12, "bold")) 
BotonInicio.place(x=125,y=680)

BotonFinalizar = tk.Button(root, text="Apagar Video", bg=fondo_boton, relief="flat",
                  cursor="hand2", command=quitar, width=15, height=2, font=("Calisto MT",12, "bold")) 
BotonFinalizar.place(x=750,y=680)

#Etiqueta

etiq_de_video = tk.Label(root, bg="black")
etiq_de_video.place(x=17,y=135)

#Active window
root.mainloop()