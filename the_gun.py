# Игра "Пушка"
def__init__(self,b):
    """
    Создаёт шарик в случайном месте игрового холста cavans,
    при этом шарик не выходит за границы холста
    ну или снаряд (при == False)
    """
    if b:
        self._R = randint(Ball.minimal_radius, Ball.maximal_radius)
        self._x = randint(0, screen_width-1-2 * self._R)
        self._y = randint(0, screen_height-1-2 * self._R)
        self._color = choice(available_colors)
        self.Vx = randint(-2,+2)
        self._Vy = randint(-2,+2)
        while self._Vx == 0 and self._Vy == 0:
            self._Vx = randint(-2,+2)
            self._Vy = randint(-2,+2)

class Gun:
   def_init_(self):
     self._x=0
     self._y=screen_height
     self._1=gun_len
     self._a=pi / 4
     self._x=self._x+self._1*cos(self._a)
     self._1y=self._y-self._1*sin(self._a)
     self._avatar=canvas.create_line(self._x, self._y
                           self._1x, self,_1y, width=3)
    def shoot(self):
      """
      получаем сняряд, запускаем его и возвращаем дял запоминания в список снарядов
      """
