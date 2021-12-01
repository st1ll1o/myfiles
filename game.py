import tkinter as tk
import os
import random
import time
import secprot


def shuffle(example):
	random.shuffle(example)

root = tk.Tk()
root.title("Mygame")
root.resizable(0,0)
root.wm_attributes('-topmost', 1)
canvas = tk.Canvas(root,width=500,height=400,highlightthickness=0)
canvas.pack()
root.update()


class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas = canvas
        self.paddle = paddle
        self.color = color
        self.score = score
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.ball_id,245,100)
        possible_coords = [-2,-1,1,2]
        shuffle(possible_coords)
        self.x = possible_coords[0]
        self.y = -2
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
		#if ball hits the bottom it marks
        self.isBallHitBottom = False


    def hit_paddle(self,pos): #FIXME: idk whats wrong here
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:		
            if pos[3]>= paddle_pos[1] and pos[3]<=paddle_pos[3]:
                self.score_hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3]>=self.canvas_h:
            self.isBallHitBottom = True
            canvas.create_text(250,120, text='Вы проиграли', font=("Courier",30), fill='red')

        if self.hit_paddle(pos) == True:
            self.y = -2
            if pos[0] <=0:
                self.x=2
        if pos[2]>=self.canvas_w:
            self.x= -2


class Paddle:
	def __init__(self,canvas,color):
		self.canvas=canvas
		self.p_id=canvas.create_rectangle(0,0,100,10,fill=color)
		self.p_possible_coords = [40,60,90,120,150,180,200]

		shuffle(p_possible_coords)
		self.startPoint_x=p_possible_coords[0]

		self.canvas.move(self.p_id, self.startPoint_x,300)
		self.x=0

		self.canvas_w=self.canvas.winfo_width()


		#Event master
		self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
		self.canvas.bind_all('<KeyPress-Left>',self.turn_left)

		self.started=False

		self.canvas.bind_all('<KeyPress-Return>',self.start_game) #or Enter

		def turn_right(self,event):
			self.x=2

		def turn_left(self,event):
			self.x=-2

		def start_game(self,event):
			self.started

		def draw(self):
			self.canvas.move(self.p_id, self.x,0)
			pos=self.canvas.coords(self.p_id)
			if pos[0] <=0:
				self.x=0

			elif pos[2] >=self.canvas_w:
				self.x=0



class Score:
    def __init__(self,canvas,color):
        self.score=0
        self.canvas=canvas
        self.s_id=canvas.create_text(450,10, text=self.score,font=('Courier',15),fill=color)
        
        

    def hit(self):
        self.score+=1
        self.canvas.itemconfig(self.id,text=self.score)
    


secprot.SCP()
score=Score(canvas,'green')
paddle=Paddle(canvas, 'white')
ball=Ball(canvas,paddle,score,'red')

while not ball.isBallHitBottom:
	if paddle.started==True:
		ball.draw()
		paddle.draw()
        root.update_idletasks()
        root.update()

    root.mainloop()



