
import arcade
from rocket import Rocket
from ball import Ball

class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__( 800 , 500 , "PONG GAME 🏓")
        self.player = Rocket ( self.width - 20 , self.height // 2 , arcade.color.RED )
        self.opponent = Rocket ( 20 , self.height // 2 , arcade.color.CYAN )
        self.ball = Ball ( self )


    def on_draw ( self ) :
        arcade.start_render ()

        arcade.set_background_color ( arcade.color.DARK_GREEN )
        arcade.draw_rectangle_outline ( self.width // 2 , self.height // 2 , self.width - 14 , self.height - 14 , arcade.color.WHITE , 5 )
        arcade.draw_line ( self.width // 2 , self.height - 13 , self.width // 2 , 13 , arcade.color.WHITE , 5)

        self.player.draw ()
        self.opponent.draw ()
        self.ball.draw ()

        text = f"{self.opponent.score}  :  {self.player.score}"
        arcade.draw_text ( text , (self.width // 2) - 68 , self.height - 60 , arcade.color.LIGHT_GREEN , 40 )

        arcade.finish_render ()

    
    def on_mouse_motion ( self, x , y , dx , dy ) :
        self.player.center_y = y
        
        if self.player.center_y < 43 :
            self.player.center_y = 43
        
        if self.player.center_y > self.height - 42 :
            self.player.center_y = self.height - 42


    def on_update ( self , delta_time ) :
        self.ball.move ()
        self.opponent.move ( self.ball , self )

        if self.ball.center_y < 20  or self.ball.center_y > self.height - 20 :
            self.ball.change_y *= -1

        if arcade.check_for_collision ( self.ball , self.player) or arcade.check_for_collision ( self.ball , self.opponent ):
            self.ball.change_x *= -1 
            self.ball.speed += 0.1

        if self.ball.center_x > self.width - 25 :
            self.opponent.score += 1
            del self.ball
            self.ball = Ball ( self )
        
        if self.ball.center_x < 25 :
            self.player.score += 1
            del self.ball
            self.ball = Ball ( self )

        
game = Game ()
arcade.run ()