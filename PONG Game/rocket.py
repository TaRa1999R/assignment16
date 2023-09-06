
import arcade

class Rocket ( arcade.Sprite ) :

    def __init__ ( self , x , y , color ) :
        super().__init__()
        self.width = 10
        self.height = 60
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.color = color
        self.speed = 4
        self.score = 0


    def draw ( self ) :
        arcade.draw_rectangle_filled ( self.center_x , self.center_y , self.width , self.height , self.color )


    def move ( self , ball , game ) :
        if ball.center_x < game.width // 2 :
            
            if self.center_y < ball.center_y :
                self.change_y = 1
            
            elif self.center_y > ball.center_y :
                self.change_y = -1 
            
            elif self.center_y == ball.center_y :
                self.change_y = 0

            self.center_y += self.change_y * self.speed
            
            if self.center_y < 43 :
                self.center_y = 43

            if self.center_y > game.height - 42 :
                self.center_y = game.height - 42