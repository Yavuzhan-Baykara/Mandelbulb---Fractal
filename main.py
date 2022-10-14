from cv2 import sqrt
import ursina as urs
import sys
import math
def urswindow(point):
    app = urs.Ursina()
    urs.window.borderless = False
    urs.window.size = (1920, 1080)
    urs.window.fullscreen
    urs.window.color = urs.color.black
    urs.Entity(model = urs.Mesh(vertices = point, mode = 'point', thickness = 0.01), color = urs.color.green)
    urs.EditorCamera()
    app.run()
def cartesian(x, y, z) -> float:
    r: float = math.sqrt((x * x) + (y * y) + (z * z))
    theta: float = math.atan2(math.sqrt((x * x) + (y * y)), z)
    fi: float = math.atan2(y , x)
    return r, theta, fi 

def draw(dim, point):
    for x in range(dim):
        for y in range(dim):
            for z in range(dim):
                r, theta, fi = cartesian(x, y, z)
                point.append((r, theta, fi))


if __name__ == "__main__":
    dim = 32
    point = []
    draw(dim, point)
    urswindow(point)
    



sys.exit(0)