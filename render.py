from typing import List
import matplotlib.pyplot as plt


def render(reflectors, rays):
    for reflector in reflectors:
        print(reflector.start)
        print(reflector.end)
        ax = plt.gca()
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])
        ax.invert_yaxis()
        plt.plot([reflector.start[0], reflector.end[0]], [
                 reflector.start[1], reflector.end[1]], color='r')
    for ray in rays:
        if len(ray.position_history) > 1:
            for first_position, second_position in zip(ray.position_history[:-1], ray.position_history[1:]):
                plt.plot([first_position[0], second_position[0]], [first_position[1], second_position[1]],
                         '-*', color='blue')
