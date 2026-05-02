"""三体问题模拟"""
# 这个程序模拟了三体问题，其中恒星和行星类在star.py中定义。程序从一个YAML配置文件加载初始条件，并使用Pygame Zero进行图形显示和更新。
# 所有所需库: pgzrun, logging, yaml, os, sys

from star import Star, Planet
import pgzrun
import logging
import yaml
import os, sys

# 设置当前工作目录为脚本所在目录，确保能够正确加载资源文件
os.chdir(sys.path[0])
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 全局变量
WIDTH = 800
HEIGHT = 600
TITLE = "Three Body Simulation"
stars = []
planets = []

def init_stars():
    """从配置文件加载星体和行星的数据"""
    global stars, planets
    with open('stars.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        stars = []
        planets = []

        for item in data["stars"]:
            star = Star(item['pos'][0], item['pos'][1], item['vel'][0], item['vel'][1], item['mass'], tuple(item['color']))
            stars.append(star)

        for item in data["planets"]:
            planet = Planet(item['pos'][0], item['pos'][1], item['vel'][0], item['vel'][1], item['mass'], tuple(item['color']))
            planets.append(planet)

def format_star():
    """更新星体和行星的位置，并记录调试信息"""
    logging.debug(f"Updated stars: {[{'x': p.x, 'y': p.y} for p in stars]}")
    logging.debug(f"Updated planets: {[{'x': p.x, 'y': p.y} for p in planets]}")

def update():
    """计算星体和行星之间的引力，并更新它们的位置"""
    for star in stars:
        for other in stars:
            if star != other:
                star.effert(other)
    for planet in planets:
        for star in stars:
            planet.effert(star)
        for other in planets:
            if planet != other:
                planet.effert(other)

    for star in stars:
        star.move()
    for planet in planets:
        planet.move()

def draw():
    """绘制星体和行星"""
    screen.fill((0, 0, 0)) # type: ignore
    for star in stars:
        screen.draw.filled_circle((int(star.x), int(star.y)), star.get_radius(), star.color) # type: ignore
    for planet in planets:
        screen.draw.filled_circle((int(planet.x), int(planet.y)), planet.get_radius(), planet.color) # type: ignore

init_stars()
clock.schedule_interval(format_star, 1) # type: ignore
pgzrun.go()