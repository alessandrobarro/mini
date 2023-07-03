import numpy as np
import tkinter as tk

theta = None

def initialize():
    global theta

    print('*---------------------------------------------------------------*\n')
    print('Linear regression ML model by @alebarro [Stanford CS229/STATS229]\n')
    print('*---------------------------------------------------------------*\n')
    print('[STATUS] Initialization')
    n = int(input('[SETTINGS] Number of training examples: '))
    d = int(input('[SETTINGS] Number of features: '))
    create_matrix_window(n, d+1)

def run_model(dataset):
    global theta
    t_input = input('[SETTINGS] N of iterations (default: 1000): ')
    if t_input == '':
        t = 1000
    else:
        t = int(t_input)
    alpha_input = input('[SETTINGS] GD step size (default: 0.000001): ')
    if alpha_input == '':
        alpha = 0.000001
    else:
        alpha = float(alpha_input)
    print('[WARNING] Data set successfully deployed')
    x = dataset[:, 0:-1]
    x = np.c_[np.ones(x.shape[0]), x]
    y = dataset[:, -1]
    theta = np.zeros(x.shape[1])
    theta, cost_history = gradientDescent(x, y, theta, alpha, t)
    print(f"[WARNING] Optimized parameters: {theta}")
    print(f"[WARNING] Cost history: {cost_history}")

    print('\n')
    print('[STATUS] Please select an option')
    print('[1] Make a prediction')
    print('[2] Close')
    selection = input('>>> ')

    while selection != '1' and selection != '2':
        print('[WARNING] Please select a valid option')
        selection = input('')

    if selection == '1':
        x_input = input('[SETTINGS] New example (x1 x2 ... xd): ')
        x = np.array([1.0] + [float(xi) for xi in x_input.split()])
        x = x.reshape(1, -1)
        print(f"[WARNING] The expected value of y is: {hypothesis(theta, x)}")

    elif selection == '2':
        quit()

def hypothesis(theta, x):
    return np.dot(x, theta)

def squared_loss(theta, x, y): 
    return (1/y.size) * np.sum((hypothesis(theta, x) - y) ** 2)

def d_squared_loss(theta, x, y):
    return (2/y.size) * np.dot(x.T, (hypothesis(theta, x) - y))

def gradientDescent(x, y, theta, alpha, t):
    cost_history = []

    for _ in range(t):
        theta = theta - alpha * d_squared_loss(theta, x, y)
        cost_history.append(squared_loss(theta, x, y))

    return theta, cost_history

def create_matrix_window(rows, cols):
    window = tk.Tk()
    window.title("LR [STATS229]")
    window.geometry('400x270')

    entry_objects = np.empty((rows, cols), dtype = object)

    for j in range(cols):
        if j == cols - 1:
            label = tk.Label(window, text = "Y")
        else:
            label = tk.Label(window, text = f"X{j+1}")
        label.grid(row = 0, column = j)
        for i in range(1, rows + 1):
            entry = tk.Entry(window, width = 10)
            entry.grid(row = i, column = j)
            entry_objects[i - 1, j] = entry

    def get_matrix():
        matrix = np.zeros((rows, cols), dtype=float)
        for i in range(rows):
            for j in range(cols):
                matrix[i, j] = float(entry_objects[i, j].get())
        return matrix

    def deploy():
        dataset = get_matrix()
        run_model(dataset)

    button = tk.Button(window, text = 'Deploy', command = deploy)
    button.grid(row = rows + 1, column = 0, columnspan = cols)

    window.mainloop()

initialize()