
class BifurcationDiagramGenerator:
    def __init__(self, x_iterator, initial_values_iterator, converge):
        self.x_iterator = x_iterator
        self.initial_values_iterator = initial_values_iterator
        self.converge = converge

    def run(self):
        results = []
        for x in self.x_iterator():
            for initial_value in self.initial_values_iterator():
                converged = self.converge(x, initial_value)  # can be list or np.array ?
                r = list(map(lambda c: [x, c], converged))
                results = results + r
                
        x_var = [x[0] for x in results]
        y_var = [x[1] for x in results]
        return x_var, y_var
