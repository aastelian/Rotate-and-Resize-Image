from pil import Image, ImageTk
import tkinter as tk
import time


class App:
    
    def __init__(self):
        
        self.im_width = 0
        self.im_height = 0
        self.max_sized = False
        
        self.n = 0
        self.max_angle = 360
        self.ws = tk.Tk()
        self.ws.geometry("500x500")
        
        
        self.img = Image.open("1.jpg")
        self.img_resized = self.img.resize((300,300)).convert("RGBA")
        
        self.c = tk.Canvas(self.ws,height=500,width=500)
        self.c.place(x=0,y=0)
        self.bg_canv = ImageTk.PhotoImage(Image.open("bg.jpg").resize((500,500)))
        self.c.config(highlightthickness = 0)
        self.c.create_image(250,250,image = self.bg_canv)
        
        # self.rotate_animation()
        self.change_dimension_image()
        
        self.ws.mainloop()

    # def rotate_animation(self):
        # if self.n <= self.max_angle:
            # try:
                # self.image = self.img_resized.rotate(self.n,expand=1)
                # self.rotated_image_canvas = ImageTk.PhotoImage(self.image)
                # self.c.delete("all")
                # self.image_canv_id=self.c.create_image(250,250,image=self.rotated_image_canvas)
                # self.n += 1
                
            # except:
                # pass
            # self.c.after(10,self.rotate_animation)
            
    def change_dimension_image(self):
    
        if self.im_width < 400 and self.max_sized == False:
            try:
                self.c.delete(self.id)
            except:
                pass
            
            self.im_width += 1
            self.im_height += 1
            self.changed_image_non_rotated = self.img_resized.resize((self.im_width,self.im_height))
            self.changed_image = self.changed_image_non_rotated.rotate(self.n,expand=1)
            self.img = ImageTk.PhotoImage(self.changed_image)
            self.id = self.c.create_image(250,250,image = self.img)
            self.n += 1
            
           
            
           
        elif self.im_width == 400 and self.max_sized == False:
        
            try:
                self.c.delete(self.id)
            except:
                pass
            
            self.im_width -= 1
            self.im_height -= 1
            self.changed_image_non_rotated = self.img_resized.resize((self.im_width,self.im_height))
            self.changed_image = self.changed_image_non_rotated.rotate(self.n,expand=1)
            self.img = ImageTk.PhotoImage(self.changed_image)
            self.id = self.c.create_image(250,250,image = self.img)
            self.max_sized = True
            self.n += 1
            
        elif self.im_width < 400 and self.im_width > 1 and self.max_sized == True:
            try:
                self.c.delete(self.id)
            except:
                pass
            
            self.im_width -= 1
            self.im_height -= 1
            self.changed_image_non_rotated = self.img_resized.resize((self.im_width,self.im_height))
            self.changed_image = self.changed_image_non_rotated.rotate(self.n,expand=1)
            self.img = ImageTk.PhotoImage(self.changed_image)
            self.id = self.c.create_image(250,250,image = self.img)
            self.n += 1
            
        elif self.im_width == 1 and self.max_sized == True:
            try:
                self.c.delete(self.id)
            except:
                pass
            
            self.im_width += 1
            self.im_height += 1
            self.changed_image_non_rotated = self.img_resized.resize((self.im_width,self.im_height))
            self.changed_image = self.changed_image_non_rotated.rotate(self.n,expand=1)
            self.img = ImageTk.PhotoImage(self.changed_image)
            self.id = self.c.create_image(250,250,image = self.img)
            self.max_sized = False
            self.n += 1
            
        self.c.after(5,self.change_dimension_image)
        

App()







