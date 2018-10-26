from turtle import *
#画背景
color('red', 'red')
begin_fill()
while True:
    forward(288)
    right(90)
    forward(192)
    right(90)
    if abs(pos()) < 1:
        break
end_fill()
#画大星星
penup()
setposition(19.2,-38.4)
pendown()
color('yellow', 'yellow')
begin_fill()
while True:
    forward(57.6)
    right(144)
    if round(xcor())== 19 and round(ycor())== -38:
        break
end_fill()
# 画四个小星星
penup()
setposition(86.4,-24)
pendown()
left(60)
color('yellow', 'yellow')
begin_fill()
while True:
    forward(19.2)
    right(144)
    if round(xcor())== 86 and round(ycor())== -24:
        break
end_fill()
penup()
setposition(108,-40)
pendown()
right(30)
color('yellow', 'yellow')
begin_fill()
while True:
    forward(19.2)
    right(144)
    if round(xcor())== 108 and round(ycor())== -40:
        break
end_fill()
penup()
setposition(108,-65)
pendown()
right(30)
color('yellow', 'yellow')
begin_fill()
while True:
    forward(19.2)
    right(144)
    if round(xcor())== 108 and round(ycor())== -65:
        break
end_fill()
penup()
setposition(86,-80)
pendown()
right(30)
color('yellow', 'yellow')
begin_fill()
while True:
    forward(19.2)
    right(144)
    if round(xcor())== 86 and round(ycor())== -80:
        break
end_fill()
penup()
setposition(0,0)
pendown()
 
done()
