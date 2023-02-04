from typing import List
import matplotlib.pyplot as plt


def render(reflectors, rays, xlim=[0, 100], zlim=[0, 100]):
    plt.rcParams['figure.figsize'] = [10, 10]
    for reflector in reflectors:
        plt.plot([reflector.start[0], reflector.end[0]], [
                 reflector.start[1], reflector.end[1]], color='r')
    for i, ray in enumerate(rays):
        if len(ray.position_history) > 1:
            for j, (first_position, second_position) in enumerate(zip(ray.position_history[:-1], ray.position_history[1:])):
                if j == 0:
                    p = plt.plot([first_position[0], second_position[0]], [first_position[1], second_position[1]],
                                 '-*', label=f'Ray {i}')
                else:
                    plt.plot([first_position[0], second_position[0]], [first_position[1], second_position[1]],
                             '-*', c=p[0].get_c())

    ax = plt.gca()
    ax.set_xlim(xlim)
    ax.set_ylim(zlim)
    ax.invert_yaxis()
    plt.legend()
