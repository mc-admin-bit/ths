"""三体问题模拟"""
# 这个程序模拟了三体问题，其中恒星和行星类在star.py中定义。程序从一个YAML配置文件加载初始条件，并使用Pygame Zero进行图形显示和更新。
# 所有所需库: pgzrun, logging, pyyaml, os, sys

from star import Star, Planet
import pgzrun
import logging
import yaml
import os, sys

# 设置当前工作目录为脚本所在目录，确保能够正确加载资源文件
os.chdir(sys.path[0])
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 全局变量
WIDTH = 900
HEIGHT = 600
TITLE = "Three Body Simulation"
stars = []
planets = []
trajectory_length = 100
star_trajectory = True
planet_trajectory = True
start_flag=True
camera_speed = 2

def init_stars():
    """从配置文件加载星体和行星的数据"""
    global stars, planets, trajectory_length, star_trajectory, planet_trajectory, camera_speed
    with open('stars.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        stars = []
        planets = []

        trajectory_length = data.get('trajectory_length', 100)
        star_trajectory = data.get('star_trajectory', True)
        planet_trajectory = data.get('planet_trajectory', True)
        camera_speed = data.get('camera_speed', 2)

        for item in data["stars"]:
            star = Star(item['pos'][0], item['pos'][1], item['vel'][0], item['vel'][1], item['mass'], tuple(item['color']), trajectory_length)
            stars.append(star)

        for item in data["planets"]:
            planet = Planet(item['pos'][0], item['pos'][1], item['vel'][0], item['vel'][1], item['mass'], tuple(item['color']), trajectory_length)
            planets.append(planet)

def format_star():
    """更新星体和行星的位置，并记录调试信息"""
    if start_flag:
        logging.debug(f"Updated stars: {[{'x': p.x, 'y': p.y} for p in stars]}")
        logging.debug(f"Updated planets: {[{'x': p.x, 'y': p.y} for p in planets]}")

def on_key_down(key):
    global start_flag
    """处理键盘输入，重新加载星体和行星的数据"""
    if key == keys.SPACE: # type: ignore
        start_flag = not start_flag
        logging.info(f"Start flag set to {start_flag}")

def update():
    """计算星体和行星之间的引力，并更新它们的位置"""
    if start_flag:
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
    if keyboard.K_UP: # type: ignore
        for star in stars:
            star.y += camera_speed
            for t in star.traj.points:
                t.y += camera_speed
        for planet in planets:
            planet.y += camera_speed
            for t in planet.traj.points:
                t.y += camera_speed
    if keyboard.K_DOWN: # type: ignore
        for star in stars:
            star.y -= camera_speed
            for t in star.traj.points:
                t.y -= camera_speed
        for planet in planets:
            planet.y -= camera_speed
            for t in planet.traj.points:
                t.y -= camera_speed
    if keyboard.K_LEFT: # type: ignore
        for star in stars:
            star.x += camera_speed
            for t in star.traj.points:
                t.x += camera_speed
        for planet in planets:
            planet.x += camera_speed
            for t in planet.traj.points:
                t.x += camera_speed
    if keyboard.K_RIGHT: # type: ignore
        for star in stars:
            star.x -= camera_speed
            for t in star.traj.points:
                t.x -= camera_speed
        for planet in planets:
            planet.x -= camera_speed
            for t in planet.traj.points:
                t.x -= camera_speed


def draw():
    """绘制星体和行星"""
    screen.fill((0, 0, 0)) # type: ignore
    for star in stars:
        screen.draw.filled_circle((int(star.x), int(star.y)), star.get_radius(), star.color) # type: ignore
        if star_trajectory:
            for point in star.traj.points:
                screen.draw.filled_circle((int(point.x), int(point.y)), 1, star.traj.color) # type: ignore
    for planet in planets:
        screen.draw.filled_circle((int(planet.x), int(planet.y)), planet.get_radius(), planet.color) # type: ignore
        if planet_trajectory:
            for point in planet.traj.points:
                screen.draw.filled_circle((int(point.x), int(point.y)), 1, planet.traj.color) # type: ignore
init_stars()
clock.schedule_interval(format_star, 1) # type: ignore
pgzrun.go()