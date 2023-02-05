import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
from urllib import request
import io
import uuid
from os import system, remove

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Descarga Youtube")
        self.minsize(1080,100)
        self.maxsize(1080,970)
        self.usuario = "hyde"
        self.pathDescarga = f"C:\\Users\\{self.usuario}\\Downloads"
        self.name_video1 = ""
        self.fecha_publicacion1 = ""
        self.img_video1 = ""
        self.vistas_video1 = ""
        #Principal
        pricipal_title = tkinter.StringVar(value="Descarga Videos de Youtube")
        self.title = customtkinter.CTkLabel(master=self,
                                            textvariable=pricipal_title,
                                            width=20,
                                            height=10,
                                            text_font=("Arial", 15,"bold"))
        self.title.grid(row=0,column=0,columnspan=2,pady=20)
        #Title Principal
        segundo_title = tkinter.StringVar(value="Ingresar el Url : ")
        self.title2 = customtkinter.CTkLabel(master=self,
                                            textvariable=segundo_title,
                                            width=220,
                                            height=20,
                                            text_font=("Arial", 15,"bold"))
        self.title2.grid(row=1,column=0,sticky="nsew")
        
        #Entry Principal
        self.entry1 = customtkinter.CTkEntry(master=self,
                                            placeholder_text="escriba la url",
                                            width=600,
                                            height=15,
                                            border_width=5,
                                            corner_radius=10)
        self.entry1.grid(row=1,column=1,sticky="nsew",ipady=5,pady=10)
        
        #ComboBox Principal
        self.comboBox1 = customtkinter.CTkComboBox(master=self,
                                                   values=["360p","720p","1080p"])
        
        self.comboBox1.grid(row=1,column=2,padx=20)
        self.comboBox1.set("720p")
        
        #Buttom Principal
        self.buttom = customtkinter.CTkButton(master=self,
                                            width=100,
                                            height=20,
                                            border_width=1,
                                            corner_radius=10,
                                            text="Verificar Video",
                                            command=self.descarga_video,
                                            text_font=("Arialh", 13),
                                            fg_color="#353535",
                                            hover_color="#212529",
                                            text_color_disabled="#212529"
                                            )
        self.buttom.grid(row=2,column=0,columnspan=3,ipadx=20,ipady=3)
        
        self.buttom3 = customtkinter.CTkButton(master=self,
                                        width=100,
                                        height=20,
                                        border_width=1,
                                        corner_radius=10,
                                        text="Descargar Video",
                                        command=self.descarga_video2,
                                        text_font=("Arialh", 13),
                                        fg_color="#353535",
                                        hover_color="#212529",
                                        text_color_disabled="#212529"
                                        )
        self.buttom3.grid(row=4,column=0,columnspan=3,ipadx=20,ipady=3,pady=30)
    def descarga_video(self):
        url = self.entry1.get()
        video = YouTube(url)
        self.name_video1 = video.title
        self.fecha_publicacion1 = str(video.publish_date)
        self.img_video1 = str(video.thumbnail_url)
        self.vistas_video1 = str(video.views)
        raw_data = request.urlopen(self.img_video1).read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        print("descargado")
        print(self.img_video1)
        
        #frame secundario
        self.frame1 = customtkinter.CTkFrame(master=self,
                                            width=1000,
                                            height=750,
                                            corner_radius=10)
        self.frame1.grid(row=3,column=0,columnspan=3,padx=60,pady=10,sticky="nsew")
        
        #Name Video
        self.name_video = tkinter.StringVar(value=f"Nombre del video: {self.name_video1[:20]}...")
        self.title3 = customtkinter.CTkLabel(master=self.frame1,
                                            textvariable=self.name_video,
                                            width=220,
                                            height=20,
                                            text_font=("Arial", 10,"bold"))
        
        self.title3.pack(padx=30,pady=20,)
        #fecha publicacion
        self.fecha_publicacion = tkinter.StringVar(value=f"Fecha de publicacion : {self.fecha_publicacion1}")
        self.title4 = customtkinter.CTkLabel(master=self.frame1,
                                            textvariable=self.fecha_publicacion,
                                            width=220,
                                            height=20,
                                            text_font=("Arial", 10,"bold"))
        
        self.title4.pack(padx=30,pady=10)
        #vistas video
        self.vistas_video = tkinter.StringVar(value=f"Vistas : {self.vistas_video1}")
        self.title5 = customtkinter.CTkLabel(master=self.frame1,
                                            textvariable=self.vistas_video,
                                            width=220,
                                            height=20,
                                            text_font=("Arial", 10,"bold"))
        
        self.title5.pack(padx=20,pady=10)
        #Buttom2 Principal
        self.buttom2 = customtkinter.CTkButton(master=self.frame1,
                                            width=50,
                                            height=20,
                                            border_width=1,
                                            text="",
                                            border_color="#353535",
                                            text_font=("Arialh", 13),
                                            fg_color="#353535",
                                            hover_color="#212529",
                                            text_color_disabled="#212529",
                                            image=image
                                            )
        self.buttom2.configure(state=tkinter.DISABLED)
        self.buttom2.pack(padx=30,pady=10)
        
        
    def descarga_video2(self):
        url = self.entry1.get()
        video = YouTube(url)
        if self.comboBox1.get() == "360p":
            try:
                video.streams.filter(res="360p").first().download(output_path=self.pathDescarga)
            except:
                print("url denegada o resolucion no existente")
        elif self.comboBox1.get() == "720p":
            try:
                video.streams.filter(res="720p").first().download(output_path=self.pathDescarga)
            except:
                print("url denegada o resolucion no existente")
        elif self.comboBox1.get() == "1080p":
            try:
                uno = video.streams.filter(resolution="1080p").first().download(self.pathDescarga,f"{uuid.uuid1()}.mp4")
                dos = video.streams.filter(only_audio=True).first().download(self.pathDescarga,f"{uuid.uuid1()}.mp4")
                system(f'ffmpeg -i {uno} -i {dos}  -c copy {self.pathDescarga}/{str(uuid.uuid1())}.mp4')
                remove(f'{uno}')
                remove(f'{dos}')
            except:
                print("url denegada o resolucion no existente")
        else:
            print("error")
            
if __name__ == '__main__':
    app = App()
    app.mainloop()