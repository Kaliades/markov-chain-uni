class Forward:

    def algo(self):

        T = 10  # Number of observations
        M = 2  # Number of observation symbols
        N = 3  # Number of states

        obser = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]  # len(obser) = 10
        b = [[0.5, 0.5], [0.75, 0.25], [0.25, 0.75]]  # NxM
        A = [[1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0],
             [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]]  # NxN list

        alphaold = [0, 0, 0]  # length N
        alphanew = [0, 0, 0]  # length N

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
        k = 0
        print("Before the loooooooooooooooooooooooopssssssss")
        while t <= T - 2:
            temp = obser[t + 1]
            while j < N:
                sum = 0.0
                while i2 < N:
                    sum += alphaold[i2]*A[i2][j]
                    i2 += 1
                alphanew[j] = sum * b[j][temp]
                j += 1
            while k < N:
                alphaold[k] = alphanew[k]
                k += 1
            t += 1
        print("I've fINISHED the looooooooop!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # probability
        P = 0.0
        i3 = 0
        while i3 < N:
            P += alphanew[i3]
            i3 += 1
        print("P = " + str(P))

#testforward = Forward()

#testforward.algo()