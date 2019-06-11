# Render this document with DrawBot3: http://www.drawbot.com/
from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W, H, M = 1344, 768, 64

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(1,0,0)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid():
    stroke(0.5)
    strokeWidth(2)
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(41):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(25):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY

# SLIDE ONE ####################################################################
newPage(W, H)
fill(0)
rect(-2, -2, W+2, H+2)
font("fonts/Blob-Black.ttf")  # Set the font
#font("Optima Bold")  # Set the font
grid() # Toggle for grid view
edge() # Toggle for safe area

#image("source/images/cli-01.png", (-19, 0), alpha=1)

fill(1)
stroke(None)
fontSize(256)
#tracking()
text("FONT BAKERY", M, M*12)
fontSize(40)
#tracking(0)
#text("Quality Assurance for Font Families", M+170, M*18)
#saveImage("fontbakery-00.png")

# PAGE ONE #####################################################################
newPage(W, H)
fill(0.1)
rect(0, 0, W, H)
#grid() # Toggle for grid view
#edge() # Toggle for safe area
#text("Foo Bard", M, M*16)
#image("source/images/cli-03.png", (65, -10), alpha=1)
#saveImage("fontbakery-01.png")

# PAGE TWO #####################################################################
newPage(W, H)
fill(0.1)
rect(0, 0, W, H)
#grid() # Toggle for grid view
#edge() # Toggle for safe area
#text("Foo Bard", M, M*16)
#image("source/images/web-01.png", (-15, -30), alpha=1)
#saveImage("fontbakery-02.png")

# PAGE THREE ###################################################################
newPage(W, H)
fill(0.1)
rect(0, 0, W, H)
#grid() # Toggle for grid view
#edge() # Toggle for safe area
#text("Foo Bard", M, M*16)
#image("source/images/cli-02.png", (100, -20), alpha=1)
saveImage("slides.pdf")

