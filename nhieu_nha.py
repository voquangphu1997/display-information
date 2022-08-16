import turtle
import math
canh = 50
canh_2 = canh * 1.2
canh_3 = canh_2 * 1.2
khoang_canh = 20
nhan_screen = turtle.Screen()            
nhan_screen = turtle.Turtle()
nhan_screen.pensize(2)

#nha 1
nhan_screen
nhan_screen.forward(canh)                    
nhan_screen.left(90)
nhan_screen.forward(canh)                    
nhan_screen.left(90)
nhan_screen.forward(canh)                    
nhan_screen.left(90)
nhan_screen.forward(canh)                    
nhan_screen.left(90)
#cua chinh
nhan_screen.penup()
nhan_screen.goto(canh * 2/3, 0)
nhan_screen.pendown()
nhan_screen.color("red")                   
nhan_screen.left(90)
nhan_screen.forward(canh * 2/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh * 1/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh * 2/3)                    
nhan_screen.left(90)
#mai nha
nhan_screen.penup()
nhan_screen.goto(canh, canh) 
nhan_screen.pendown()
nhan_screen.color("green")                   
nhan_screen.left(135)
nhan_screen.forward(canh * math.sqrt(2)/2)                    
nhan_screen.left(90)
nhan_screen.forward(canh * math.sqrt(2)/2) 
nhan_screen.left(135)        


#nha 2
nhan_screen.penup()
nhan_screen.goto(canh + khoang_canh, 0)
nhan_screen.pendown()
nhan_screen.color("black")              
nhan_screen.forward(canh_2)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2)                    
nhan_screen.left(90)
#cua chinh
nhan_screen.penup()
nhan_screen.goto(canh + khoang_canh + canh_2 * 2/3, 0)
nhan_screen.pendown()
nhan_screen.color("red")                   
nhan_screen.left(90)
nhan_screen.forward(canh_2 * 2/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2 * 1/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2 * 2/3)                    
nhan_screen.left(90)
#mai nha
nhan_screen.penup()
nhan_screen.goto(canh + khoang_canh + canh_2, canh_2) 
nhan_screen.pendown()
nhan_screen.color("green")                   
nhan_screen.left(135)
nhan_screen.forward(canh_2 * math.sqrt(2)/2)                    
nhan_screen.left(90)
nhan_screen.forward(canh_2 * math.sqrt(2)/2) 
nhan_screen.left(135)


#nha 3
nhan_screen.penup()
nhan_screen.goto(canh + canh_2 + 2 * khoang_canh, 0)
nhan_screen.pendown()
nhan_screen.color("black")             
nhan_screen.forward(canh_3)
nhan_screen.left(90)
nhan_screen.forward(canh_3)
nhan_screen.left(90)
nhan_screen.forward(canh_3)                    
nhan_screen.left(90)
nhan_screen.forward(canh_3)                    
nhan_screen.left(90)
#cua chinh
nhan_screen.penup()
nhan_screen.goto(canh + canh_2 + 2 * khoang_canh + canh_3 * 2/3, 0)
nhan_screen.pendown()
nhan_screen.color("red")                   
nhan_screen.left(90)
nhan_screen.forward(canh_3 * 2/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh_3 * 1/3)                    
nhan_screen.left(90)
nhan_screen.forward(canh_3 * 2/3)                    
nhan_screen.left(90)
#mai nha
nhan_screen.penup()
nhan_screen.goto(canh + canh_2 + 2 * khoang_canh + canh_3, canh_3) 
nhan_screen.pendown()
nhan_screen.color("green")                   
nhan_screen.left(135)
nhan_screen.forward(canh_3 * math.sqrt(2)/2)                    
nhan_screen.left(90)
nhan_screen.forward(canh_3 * math.sqrt(2)/2) 
nhan_screen.left(135)


turtle.done()