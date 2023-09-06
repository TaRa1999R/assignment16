
import arcade
from brik import Brik

class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__( 500 , 750 , "ARKANOID GAME 🧱⚾")
        self.background = arcade.load_texture ("ARKANOID Game/images/background.png")
        self.game_over = arcade.load_texture ("ARKANOID Game/images/game over.png")
        self.win = arcade.load_texture ("ARKANOID Game/images/win.png")
        self.mode = None
        self.brik = Brik ( self , self.width // 2)


    def on_draw ( self ) :
        arcade.start_render ()

        if self.mode == "game_over" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.game_over )

        elif self.mode == "win" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.win )

        else :
            arcade.set_background_color ( arcade.color.SILVER )
            arcade.draw_lrwh_rectangle_textured ( 5 , 5 , self.width - 10 , self.height - 50 , self.background )
            arcade.draw_rectangle_outline ( self.width //2 , self.height - 22 , self.width - 10 , 36 , arcade.color.BLACK , 2 )
            self.brik.draw ()

        arcade.finish_render ()


    def on_mouse_motion ( self , x , y , dx , dy ) :
        ...


    def on_key_press ( self , symbol , modifiers ) :
        ...


    def on_key_release ( self , symbol , modifiers ) :
        ...


    def on_update ( self , delta_time ) :
        ...

game = Game ()
arcade.run ()