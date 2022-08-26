import turtle as tur
tur.bgcolor("black")
tur.speed(100)
vong = 0
color_ = ['pink', 'blue', 'green', 'yellow','orange','red']
tur.color(color_[vong])
angle_ = 10
radius_ = 100
time_ = 0
while time_ < 6:
    while vong < 6:
        tur.color(color_[vong])
        count = 0
        while count < 2:
            tur.circle(radius_,90)
            tur.circle(radius_/2,90)
            count += 1
        vong += 1
        tur.right(angle_)
    time_ += 1
    vong = 0
tur.hideturtle()
tur.done()

