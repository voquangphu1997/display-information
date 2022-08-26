import turtle as xoay
import math


khoang_cach = float(input("Nhap khoang cach: "))
tinh_tien = 1
goc = 30
toa_do_goc = [0,0]
ban_kinh = 0

while ban_kinh < khoang_cach:
    xoay.pendown()
    xoay.color("black")
    xoay.forward(tinh_tien)
    xoay.left(goc)
    tinh_tien += 1
    vi_tri = xoay.pos()
    ban_kinh = math.dist(vi_tri, toa_do_goc)

xoay.done()
