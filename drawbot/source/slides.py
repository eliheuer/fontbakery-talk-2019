
#  BBBBBBD*    *BBBBBBBBD      DBBBD*   DBBD  *BBD  *BBD *BBBBBBBBD     DBBBBBD*   DBBBBBBBBBD*
# *BBB* *BBB*  DBBD   DBBD   *BBD*DBB*  DBB*   BBD   BBD DBBD   BBB*   BBBD**DBB* *BD**BBB**DD
# *BBD   *BBB* BBB   *BBB*  *BBD   *BB* DBB*  *BBD   BBD BBB  *DBB*   BBB*    DBB*     BBD
# DBB*    *BBD BBBDDBBBD   *BBB**DDDBBD *BB*  DBBD  *BB* BBBDBBBBD   *BBD     *BBD    *BBD
# DBB*    *BBD BBBBDDBBD   DBBBBBDDBBBB  BBB  BBBB* DBD  BBB*   DBB* DBBD      BBB    DBBD
# DBBD    DBBD BBB*  *BBB* DBBD     DBB  *BBDBBDBBBBBB   BBB    *BBB DBBB*    DBBB    DBBB
# *BBBDDDBBBB  BBBD   DBBB DBBD    *BBB   DBBB*  BBBB    BBBBDDDBBBD  DBBBBBBBBBB*    *BBB*
#  DDDDDDD**   *DDD   *DDD *DDD*   DDD*    DD*    DD     *DDDDDDDD*    *DDDDDDD*       DDD*

# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/

# 🌍 GIT URL: https://github.com/eliheuer/fontbakery-talk-2019

# ######   #####   ###   ## #######    ######     ####   ###  ##  ####### ####### ###  ###
# ###     ##   ##  ####  ##   ###      ### ###   ##  ##  ### ##   ###     ###  ### ###   ##
# ###### ##     ## ## ## ##   ###      ######   ###  ##  ######   #####   ########  ######
# ###    ##     ## ##  ####   ###      ###  ## ######### ###  ##  ##      ### ##      ###
# ###    ######### ##   ###   ###      ###  ## ###    ## ###  ### ####### ###  ###   ###
# ###     #######  ##    ##   ###      ######   ###  ##  ###  ### ####### ###   ###   ###

# ✅ Quality Assurance for Font Families

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W, H, M = 1344, 768, 64

# Set variation 
fontVariations(wght=700)

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(0.5)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid():
    stroke(0.5)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(19):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(10):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY


# BASIC_PAGE ##################################################################
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # LOAD BASIC FONT
    # Fonts
    font("fonts/BlobGX.ttf")
    # Set axis from font
    for axis, data in listFontVariations().items():
        print((axis, data))
    #font("fonts/Blob-Black.ttf")  # Set the font
    #font("fonts/a.ttf")  # Set the font
    # Set variation 
    fontVariations(wght=500)




new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area

fill(1)
stroke(None)
fontSize((M*4)-8)
text("FONT BAKErY", M+8, (M*8)+10)
fontSize(M)
text("QUALITY ASSURANCE FOr FONT FAMILIES", (M)+8, (M*7)+10)

step = 100
fontSize(M*4)
stroke(0)
for i in range(20):
    fontVariations(wght=step)
    text("F", (M-300)+(step*3), (M*4)+(4)-(step/2))
    step +=20
    if i == 3:
        image("images/cli-02.png", (30, -450), alpha=1)
    else:
        pass




new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area

fill(1)
stroke(None)
fontSize(M)
e = 8
text("ELI HEUEr",    (M)+e, (M*10)+e)
text("FONT ENGINEEr", (M)+e, (M*9)+e)
#text("ELIHEUEr",   (M)+e, (M*6)+e)

step = 100
fontSize(M*8)
stroke(0)
#for i in range(20):
#    fontVariations(wght=step)
#    text("I", (M-100)+(step*3), (M*4)+(4)-(step/2))
#    step +=20
    #if i == 3:
        #image("images/cli-01.png", (400, 200), alpha=1)
    #else:
    #    pass


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/thaw.jpg", (400, 200), alpha=1)


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/multi-bg-sm.jpg", (M+100, 0), alpha=1)


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/jacobinmag-sm.jpg", (100, 100), alpha=1)


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/unix.jpg", (-300, -430), alpha=1)


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/TruFont.png", (0, 0), alpha=1)

new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/emacs-02.png", (0, 0), alpha=1)


new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
text("LIBRE GRAPHICS MEETING",    (M)+e, (M*10)+e)
image("images/saar_big-sm.jpg", (300, 100), alpha=1)





saveImage("slides.pdf")

