import matplotlib.pyplot as plt


def plot_guess(x,y):

    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro-', linewidth=1, label='Guess solution')
    ax.legend(loc='upper right')
    ax.set_xlabel('grid points')
    ax.set_ylabel('Guess solution')
    ax.grid(True)
    plt.show()