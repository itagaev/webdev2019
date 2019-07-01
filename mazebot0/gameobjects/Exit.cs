namespace pp2.lecture8.mazegame.gameobjects
{
    public class Exit: GameObject
    {
        public Exit(char label): base(label) { } // от передает label который пришел извне GameObject

        public Point getPosition()
        {
            return locations[0];
        }

    }

}
