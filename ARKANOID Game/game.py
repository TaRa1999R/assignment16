
import arcade

class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__( 500 , 700 , "ARKANOID GAME 🧱⚾")
        self.background = arcade.load_texture ("ARKANOID Game/images/background.png")
        self.game_over = arcade.load_texture ("ARKANOID Game/images/game over.png")
        self.win = arcade.load_texture ("ARKANOID Game/images/win.png")
        self.mode = None


    def on_draw ( self ) :
        arcade.start_render ()

        if self.mode == "game_over" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.game_over )

        elif self.mode == "win" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.win )

        else :
            arcade.set_background_color ( arcade.color.BLUE )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.background)


        arcade.finish_render ()


game = Game ()
arcade.run ()