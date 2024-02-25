import arcade
height = 600
width = 600

def snowman(x, y, size=1):
    arcade.draw_circle_filled(x,y, 90*size, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+70*size, 60*size, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+130*size, 40*size, arcade.color.WHITE)
    arcade.draw_point(x+20*size, y+140*size, arcade.color.BLACK, 5*size)
    arcade.draw_point(x-20*size, y+140*size, arcade.color.BLACK, 5*size)
    arcade.draw_line(x-20*size, y+130*size, x+20*size, y+130*size, arcade.color.BLACK, 5*size)


arcade.open_window(width, height, "My project")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

snowman(width/6, height/4, 0.05)
snowman(width/1, height/4, 1.1)
snowman(width/3, height/1, 1.2 )

arcade.draw_circle_filled(width/2, height/3, 90, arcade.color.WHITE)
arcade.draw_circle_filled(width/2, height/2, 60, arcade.color.WHITE)
arcade.draw_circle_filled(width/2, (height/3)*1.8, 40, arcade.color.WHITE)
arcade.draw_point(width/2+20, (height/3)*1.8+10, arcade.color.BLACK,  5)
arcade.draw_point(width/2-20, (height/3)*1.8+10, arcade.color.BLACK, 5)
arcade.draw_line(width/2-20, (height/3)*1.8, width/2+20, (height/3)*1.8, arcade.color.BLACK, 5)

arcade.finish_render()
arcade.run()
