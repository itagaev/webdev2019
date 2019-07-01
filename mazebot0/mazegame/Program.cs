using System;
using pp2.lecture8.mazegame.gameobjects;
namespace pp2.lecture8.mazegame
{

    public enum GameState
    {
        START, PLAYING, WIN, LOST, PAUSE
    }

    public enum GameAction
    {
        START, MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT, PAUSE, UNKNOWN
    }

    public class Program
    {
        static GameAction KeyToGameAction(ConsoleKeyInfo keyInfo)
        {

            ConsoleKey key = keyInfo.Key;
            switch (key)
            {
                case ConsoleKey.UpArrow: return GameAction.MOVE_UP;
                case ConsoleKey.DownArrow: return GameAction.MOVE_DOWN;
                case ConsoleKey.LeftArrow: return GameAction.MOVE_LEFT;
                case ConsoleKey.RightArrow: return GameAction.MOVE_RIGHT;
                case ConsoleKey.Escape: return GameAction.PAUSE;
                case ConsoleKey.Enter: return GameAction.START;
                default: return GameAction.UNKNOWN;
            }

        }
        static void Main(string[] args)
        {

            //1.To Load the map by level
            //2.To move person by this map
            //3.When person finds exit new map must be loaded

            GameState state = GameState.START;
            GameSession session = new GameSession();
            GameAction action = GameAction.UNKNOWN;

            state = session.play(action);
            int currentLevel = 1;
            int maxLevel = 3;

            //game loop
            while (state != GameState.LOST)
            {
                Person person = session.getPerson(); // берем все обьекты с карты
                Wall currentWall = session.getWall();
                Exit currentExit = session.getExit();
                
                action = KeyToGameAction(Console.ReadKey()); // получаем данные от нажатой клавиши

                if (action == GameAction.MOVE_UP)
                    person.move(0, -1);
                if (action == GameAction.MOVE_DOWN)
                    person.move(0, 1);
                if (action == GameAction.MOVE_LEFT)
                    person.move(-1, 0);
                if (action == GameAction.MOVE_RIGHT)
                    person.move(1, 0);  // смотря на какую клавишу нажал пользватель мы меняем точку Person

                state = session.play(action);

                if (person.IsWallCollision(currentWall)) // мы проверям на столкновение со стеной
                {
                    Console.Clear();
                    Console.SetCursorPosition(50, 10);
                    Console.WriteLine("YOU ARE LOST!!!");
                    Console.ReadKey();
                    Console.Clear();
                    currentLevel = 1;
                    session = new GameSession();
                    session.LoadMap(currentLevel);
                    state = session.play(action); // перезагрузка игры
                }
                if (person.getHead().X == currentExit.getPosition().X && person.getHead().Y == currentExit.getPosition().Y)
                {
                    Console.Clear();
                    currentLevel++;
                    if(currentLevel == maxLevel + 1)
                    {
                        Console.Clear();
                        Console.SetCursorPosition(50, 10);
                        Console.WriteLine("WIN!!!");
                        Console.ReadKey();
                        Console.Clear();
                        currentLevel = 1;
                    }
                    session = new GameSession();
                    person.ClearLocations();
                    session.setLevel(currentLevel);
                    session.LoadMap(currentLevel);
                    state = session.play(action);
                }
            }
            
        }
    }
}
