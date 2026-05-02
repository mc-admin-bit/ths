import yaml

class Star:
    """
    表示一个星体，包含位置、速度和质量
    """
    def __init__(self, x, y, dx=0, dy=0, m=100, color=(0, 0, 0)):
        """
        :param x: x坐标
        :param y: y坐标
        :param dx: x方向的速度向量
        :param dy: y方向的速度向量
        :param m: 质量
        """
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.m = m
        self.color = color
    def move(self):
        """
        根据速度更新位置
        """
        self.x += self.dx
        self.y += self.dy

    def distance(self, other):
        """
        计算与另一个星体的距离
        :param other: 另一个星体
        :return: 距离
        """
        x = self.x - other.x
        y = self.y - other.y
        xx = x * x
        yy = y * y
        rr = xx + yy
        mindis = 100
        if(rr <= mindis ** 2):
            return 100
        r = rr ** 0.5
        del x, y, xx, yy, rr
        return r
    
    def effert(self, other, G=6.67430e-11):
        """
        计算另一个星体对当前星体的引力
        :param other: 另一个星体
        """
        r = self.distance(other)
        disX = other.x - self.x
        disY = other.y - self.y
        k = G * other.m / (r ** 3)
        ax = k * disX
        ay = k * disY
        self.dx += ax
        self.dy += ay
        del ax, ay, disX, disY, r, k
    
    def get_radius(self):
        """
        根据质量计算星体的半径
        :return: 半径
        """
        return 7

class Planet(Star):
    """
    表示一个行星，继承自Star类
    """
    def __init__(self, x, y, dx=0, dy=0, m=100, color=(0, 0, 0)):
        super().__init__(x, y, dx, dy, m, color)

    def get_radius(self):
        """
        根据质量计算行星的半径
        :return: 半径
        """
        return 3
