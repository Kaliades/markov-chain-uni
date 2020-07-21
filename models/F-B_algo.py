class Forward():

    def algo(self):

        T = 10  # Number of observations
        M = 2  # Number of observation symbols
        N = 3  # Number of states

        obser = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]  # len(obser) = 10
        b = [[0.5, 0.5], [0.75, 0.25], [0.25, 0.75]]  # NxM
        A = [[1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0],
             [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]]  # NxN list

        alphaold = []  # length N
        alphanew = []  # length N

        # initialization
        temp = obser[0]

        i1 = 0

        while i1 < N:
            alphaold[i1] = (1.0 / 3.0) * b[i1][temp]
            i1 += 1

        # iteration

        t = 0
        j = 0
        i2 = 0

        while