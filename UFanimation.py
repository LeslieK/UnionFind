import matplotlib.pyplot as plt
from matplotlib import animation
from collections import deque
import randomGrid as RG
import WeightedQuickUF as UF


def createFigure(N):
    """initializes base figure"""
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect=True, autoscale_on=True)
    ax.set_xlim(0, N - 1)
    ax.set_ylim(0, N - 1)
    ax.grid(True)
    ax.hold(True)
    line, = ax.plot([], [], linewidth=2, color='red', marker='.')
    return fig, ax, line


def init():
    """set initial value of line"""
    line.set_data([], [])
    return line,


def animate(i):
    """connecting sites in a grid"""
    #resize = False
    # set line to new data
    pairx, pairy = connections.popleft()
    rowx = pairx[0]
    colx = pairx[1]
    rowy = pairy[0]
    coly = pairy[1]
    x = []
    y = []
    x.append(rowx)
    y.append(colx)
    x.append(rowy)
    y.append(coly)
    line.set_data(x, y)
    return line,


def generateConnections(N, algo):
    """
    generates connections for a NxN grid
    """
    st = RG.randomGrid(N)
    uf = UF.algo_dict[algo](N * N)
    connections = deque()
    while uf.count() > 1:
        cell1, cell2 = st.pop()
        site1 = cell1[0] * N + cell1[1]
        site2 = cell2[0] * N + cell2[1]
        if uf.connected(site1, site2):
            continue
        else:
            uf.union(site1, site2)
            connections.append((cell1, cell2))
    return connections, len(connections)


####################################################
if __name__ == "__main__":
    N = raw_input("Enter N [default: 5]: ")
    if N is '':
        N = 5
    else:
        N = int(N)
    algo = raw_input("Enter algo [default: WQUH]: ")
    if algo is '':
        algo = "WQUH"

    fig, ax, line = createFigure(N)

    connections, size = generateConnections(N, algo.upper())

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=size, repeat=False, interval=500,
                                   blit=True)

    #anim.save('uf.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()
