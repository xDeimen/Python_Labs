class module_ds:
    def __init__(self, x, y, z, u, w):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.w = w

    def f(x, y, z, u, w):
        if ((type(x) == int) and (type(y) == str) and (type(z) == float) and
                (type(u) == list) and (type(w) == bool)):
            return [x, y, z, u, w]
        else:
            return "Eroare"

    def suma(Q, K):
        result = []
        for i in range(len(Q)):
            if type(Q[i]) != type(K[i]):
                return "Eroare"
            if isinstance(Q[i], list):
                if len(Q[i]) != len(K[i]):
                    return "Eroare"
                result.append([Q[i][j] + K[i][j] for j in range(len(Q[i]))])
            else:
                result.append(Q[i] + K[i])
        return result

