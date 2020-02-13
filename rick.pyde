baubleColor=0
def setup():
    size(500,500) 
    frameRate(10)
       
def draw():
#Background
    r=(mouseX+mouseY)%256
    g=(mouseX-mouseY)%256
    b=(mouseX*mouseY)%256
    background(r,g,b)
    if mousePressed:
        background(0)
    ellipseMode(CENTER)
    rectMode(CORNER)
    strokeWeight(3)
    
    if mousePressed!=True:
        #background Balls
        ballCount=int(random(10,20))
    #how many I want
        currentCount=0
    #how many I have
        while currentCount<ballCount:
    #While I still want more
            currentCount=currentCount+1
    #add one ball to the current count
            ballSize=int(random(min(width,height)/8,min(width,height)/4))
            posX=int(random(0,width))
            posY=int(random(0,height))
            ballRed=int(random(0,255))
            ballGreen=int(random(0,255))
            ballBlue=int(random(0,255))
            fill(ballRed,ballGreen,ballBlue)
            ellipse(posX,posY,ballSize,ballSize)

#body
    stroke(150,0,0)
    fill(150,0,0)
    quad(125,200,355,200,325,400,150,400)

#Eyes
    
    stroke(0)
    fill(255)
    if mousePressed:
        fill(255,0,0)
    eye1=ellipse(180,275,40,40)
    eye2=ellipse(290,275,40,40)
#Pupils
    fill(0)
    pupil1=ellipse(175,275,20,25)
    pupil2=ellipse(295,275,20,25)

#floor
    stroke(0)
    fill(0)
    rect(0,440,500,60)

#legs
    stroke(150,0,0)
    fill(150,0,0)
    mxf=mouseX/4
    leg1=rect(150,400,30,40+min(mxf%80,80-mxf%80))
    leg2=rect(295,400,30,00+max(mxf%80,80-mxf%80))
    
#arms
   # stroke(150,0,0)
    #fill(150,0,0)
    arm1=rect(75,constrain(300-(mouseY-300),275,325),80,30)#min(max(275,300-(mouseY-300)),325),80,30)
    arm2=rect(320,constrain(mouseY,275,325),80,30)#min(max(275,mouseY),325),80,30)
    

#antennas
    stroke(150,0,0)
    antenna1=line(200,200,150,150)
    antenna2=line(290,200,350,100)
#baubles
    global baubleColor
    if(mousePressed!=True):
        baubleColor=min((2*mouseX+mouseY)%512,511-(2*mouseX+mouseY)%512)
    stroke(150,0,150)
    fill(baubleColor,0,baubleColor)
    if baubleColor>127:
        ellipse(150,150,20,20)
        ellipse(350,100,25,25)
    else:
        ellipse(150,150,10,10)
        ellipse(350,100,10,10)
        
    
    #mouth
    stroke(0)
    line(175,320,295,320)
    
    #fang
    stroke(255)
    fill(255)
    triangle(200,323,225,323,210,350)
    if mousePressed:
        stroke(255,0,0)
        fill(255,0,0)
        triangle(210,350,215,341,205,337)
    
    #secret eyebrows
    if mousePressed:
        stroke(0)
        eyebrow1=line(160,235,200,255)
        eyebrow2=line(275,255,315,235)
    
