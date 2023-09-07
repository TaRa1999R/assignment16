
import arcade

class Brik ( arcade.Sprite ) :

    def __init__ ( self , game , x ) :
        super().__init__()
        self.width = 40
        self.height = 20
        self.center_x = x
        self.center_y = game.height - 195
        self.change_x = 0
        self.change_y = 0
        self.coler_list = [ arcade.color.GREEN , arcade.color.YELLOW , arcade.color.DARK_ORANGE , arcade.color.RED , arcade.color.DARK_VIOLET , arcade.color.CYAN ]

    def draw ( self , height) :
        for color in self.coler_list :
            arcade.draw_rectangle_filled ( self.center_x , self.center_y , self.width , self.height , color )
            self.center_y += 25
        self.center_y = height - 195
            