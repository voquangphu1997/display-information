import turtle
import math
chieu_dai = 200
chieu_rong = 50
chieu_cao = 80


nhan_screen = turtle.Screen()            
nhan_screen = turtle.Turtle()    
nhan_screen.forward(chieu_dai)                    
nhan_screen.left(0)
nhan_screen.forward(chieu_rong)                    
nhan_screen.left(90)
nhan_screen.forward(chieu_cao)                    
nhan_screen.left(90)
nhan_screen.forward(chieu_rong)
nhan_screen.left(90)
nhan_screen.forward(chieu_cao)                    
nhan_screen.left(-90)
nhan_screen.forward(chieu_dai)
nhan_screen.left(-90)
nhan_screen.forward(chieu_cao)
nhan_screen.left(-90)
nhan_screen.forward(chieu_dai + chieu_rong)
nhan_screen.left(120)
nhan_screen.forward(chieu_rong)
nhan_screen.left(120)
nhan_screen.forward(chieu_rong)
nhan_screen.left(180)
nhan_screen.forward(chieu_rong)
nhan_screen.left(120)
nhan_screen.forward(chieu_dai)
nhan_screen.left(60)
nhan_screen.forward(chieu_rong)




turtle.done()