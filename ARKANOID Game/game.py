
import arcade

class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__( 600 , 800 , "ARKANOID GAME 🧱⚾")

    def on_draw ( self ) :
        arcade.start_render ()

        arcade.set_background_color ( arcade.color.BLUE )

        arcade.finish_render ()


game = Game ()
arcade.run ()