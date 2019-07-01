using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using pp2.lecture8.mazegame.gameobjects;

namespace pp2.lecture8.mazegame
{
    public class GameSession
    {
        private Wall wall;
        private Exit exit;
        private Person person;
        private int level = 1;

        public void setLevel(int level)
        {
            this.level = level;
        }

        public GameSession() // инициализация всез обьектов
        {
            wall = new Wall('#');
            exit = new Exit('X');
            person = new Person('P');
        
            LoadMap(level); // функция для инициализации уровня
        }
        public Exit getExit()
        {
            return this.exit;
        }
        public Person getPerson()
        {
            return this.person;
        }

        public Wall getWall()
        {
            return this.wall;
        }

        public GameState play(GameAction action)
        {
            render(); // рисовки map

            return GameState.PLAYING;
        }

        private void render()
        {
            wall.Clear();
            exit.Clear();
            person.Clear();

            wall.Draw();
            exit.Draw();
            person.Draw();
        }

        public void LoadMap(int level)
        {
            Console.Clear();
            string filePath = string.Format("Levels/Level{0}.txt", level);
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            StreamReader sr = new StreamReader(fs); // открываем поток к файлу для чтения

            bool isPersonLoaded = false;
            bool isExitLoaded = false;
            int x = 0, y = 0;

            person.ClearLocations(); // очистка всех обьектов(locations)
            exit.ClearLocations();
            wall.ClearLocations();
            Console.SetCursorPosition(50, 0);
            Console.WriteLine("Your Level: " + this.level);

            while (!sr.EndOfStream) // заполняем locations всех объектов
            {
                string line = sr.ReadLine();
                for (x=0;x<line.Length;x++)
                {
                    if (line[x] == wall.GetLebel())
                    {
                        wall.AddPoint(new Point(x, y));
                    } else if (line[x] == person.GetLebel() && !isPersonLoaded)
                    {
                       person.AddPoint(new Point(x, y));
                       isPersonLoaded = true;
                    } else if (line[x] == exit.GetLebel() && !isExitLoaded)
                    {
                        exit.AddPoint(new Point(x, y));
                        isExitLoaded = true;
                    }
                }

                y++;
            }

            sr.Close();
            fs.Close();

        }

    }
}
