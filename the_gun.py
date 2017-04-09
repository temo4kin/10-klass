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
