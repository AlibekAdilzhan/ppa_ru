n = 100  #heat 2D
a = 1
dx = 0.01
dt = 0.00001
eps = 0.0001
x = np.linspace(0, 1, n)

itt = 0
eps = 0.0001
t = 1000
if my_rank == 0:
    Un = [0 for i in range(n)]
    Un[-1] = 1
    Un = [Un[:][0:n//2], Un[:][n//2:n]]
    print(Un)
else:
    Un = None

Un = comm.scatter(Un, root=0)
Unp1 = [i for i in Un]

while True:

    for i in range(1, len(Unp1)-1):
        Unp1[i] = dt * a**2 * (Un[i + 1] - 2 * Un[i] + Un[i - 1]) / dx / dx + Un[i]
        #print(Unp1[i], i)
    if my_rank == 0:
        comm.send(Un[-1], dest=1)
        right = comm.recv(source=1)
        Unp1[-1] = dt * a**2 * (right - 2 * Un[-1] + Un[-2]) / dx / dx + Un[-1]
    elif my_rank == 1:
        left = comm.recv(source=0)
        comm.send(Un[0], dest=0)
        Unp1[0] = dt * a**2 * (Un[1] - 2 * Un[0] + left) / dx / dx + Un[0]

    temp1 = np.max(abs(np.array(Un) - np.array(Unp1)))
    comm.send(temp1, dest=1-my_rank)
    temp2 = comm.recv(source=1-my_rank)

    Un = [i for i in Unp1]
    if max(temp1, temp2) < eps and itt >= t:
        break
    itt += 1

Unf = comm.gather(Unp1, root=0)
print(itt)

if my_rank == 0:
    Unp1 = np.array(Unf).flatten()
    # plt.plot(x, Unp1, 'r')
    # plt.xlabel('meter')
    # plt.ylabel('Temp')
    # plt.show()
    Unp1 = np.reshape(Unp1, (-1, 2))
    color_size = 50
    colourMap = plt.cm.jet
    plt.title("2D heat equation")
    plt.contourf(Unp1, color_size, cmap=colourMap)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar()
    plt.show()