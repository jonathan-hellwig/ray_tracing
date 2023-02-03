from typing import List
import matplotlib.pyplot as plt


def render(reflectors, rays, xlim=[0,100], zlim=[0,100]):
    for reflector in reflectors:
        ax = plt.gca()
        ax.set_xlim(xlim)
        ax.set_ylim(zlim)
        ax.invert_yaxis()
        plt.plot([reflector.start[0], reflector.end[0]], [
                 reflector.start[1], reflector.end[1]], color='r')
    for ray in rays:
        if len(ray.position_history) > 1:
            for first_position, second_position in zip(ray.position_history[:-1], ray.position_history[1:]):
                plt.plot([first_position[0], second_position[0]], [first_position[1], second_position[1]],
                         '-*', color='blue')
