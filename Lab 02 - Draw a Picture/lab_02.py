import arcade
height = 600
width = 600

arcade.open_window(width, height, "My project")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

arcade.draw_circle_filled(width/2, height/3, 90, arcade.color.WHITE)
arcade.draw_circle_filled(width/2, height/2, 60, arcade.color.WHITE)
arcade.draw_circle_filled(width/2, (height/3)*1.8, 40, arcade.color.WHITE)
arcade.draw_point(width/2+20, (height/3)*1.8+10, arcade.color.BLACK,  5)
arcade.draw_point(width/2-20, (height/3)*1.8+10, arcade.color.BLACK, 5)
arcade.draw_line(width/2-20, (height/3)*1.8, width/2+20, (height/3)*1.8, arcade.color.BLACK, 5)

arcade.finish_render()
arcade.run()
