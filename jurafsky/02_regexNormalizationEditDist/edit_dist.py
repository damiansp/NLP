import numpy as np

class EditDistance():
    def __init__(self, word1, word2, sub_cost=2, add_cost=1, del_cost=1):
        self.word1 = [c for c in '#' + word1]
        self.word2 = [c for c in '#' + word2]
        self.n1 = len(self.word1)
        self.n2 = len(self.word2)
        self.costs = {'sub': sub_cost,
                      'del': del_cost,
                      'add': add_cost}
        self.steps = {'dia': np.array([-1, -1]),
                      'non': np.array([-1, -1]),
                      'sub': np.array([-1, -1]),
                      'add': np.array([ 0, -1]), 
                      'del': np.array([-1,  0])}
        self._create_matrices()
        self.get_cost()

    def set_words(self, *words):
        print(words)
        self.word1 = [c for c in '#' + words[0]]
        self.word2 = [c for c in '#' + words[1]]
        self.n1 = len(self.word1)
        self.n2 = len(self.word2)
        self._create_matrices()
        self.cost = self.get_cost()

    def get_cost(self):
        try:
            return self.cost
        except AttributeError:
            self.cost = self.matrix[self.n1 - 1, self.n2 - 1]
            return self.cost

    def print_matrix(self):
        if self.matrix is None:
            self.matrix = self._create_matrix()
        print(self.matrix)

    def align(self):
        out1 = ''
        out2 = ''
        self.actions = self._get_action_seq()
        for a in self.actions:
            if a in ['fin', 'sub', 'non']:
                out1 += self.word1.pop(0)
                out2 += self.word2.pop(0)
            elif a == 'add':
                out1 += '-'
                out2 += self.word2.pop(0)
            else:
                out1 += self.word1.pop(0)
                out2 += '-'
        self.alignment = (out1[1:], out2[1:]) # omit initial '#'
        print('%s\n%s' % (out1[1:], out2[1:]))

    def print_seq(self):
        print(self.actions[1:])

    def _create_matrices(self):
        self.matrix = self._init_matrix()
        self.action_matrix = np.array(['unk'] * self.n1 * self.n2)\
                               .reshape([self.n1, self.n2])
        self.action_matrix[0, :] = ['fin'] + ['add'] * (self.n2 - 1)
        self.action_matrix[:, 0] = ['fin'] + ['del'] * (self.n1 - 1)
        for i in range(1, self.n1):
            for j in range(1, self.n2):
                (self.matrix[i, j],
                 self.action_matrix[i, j]) = self._get_cell_value(i, j)
                

    def _init_matrix(self):
        matrix = np.zeros([self.n1, self.n2])
        matrix[:, 0] = range(self.n1)
        matrix[0, :] = range(self.n2)
        return matrix

    def _get_cell_value(self, i, j):
        prev_cells = self._get_prev_cells(i, j)
        min_prev = prev_cells['dia']
        optimal_action = 'dia'
        for cell in ['add', 'del']:
            if prev_cells[cell] < min_prev:
                min_prev = prev_cells[cell]
                optimal_action = cell
        diag_action = 'non' if self.word1[i] == self.word2[j] else 'sub'
        diag_cost = 0 if diag_action == 'non' else self.costs['sub']
        values = {'dia': prev_cells['dia'] + diag_cost,
                  'del':  prev_cells['del']  + self.costs['del'],
                  'add':  prev_cells['add']  + self.costs['add']}
        min_value = values['dia']
        for cell in ['add', 'del']:
            val = values[cell]
            if val < min_value:
                min_value = val
        if optimal_action == 'dia':
            optimal_action = diag_action
        return min_value, optimal_action

    def _get_prev_cells(self, i, j):
        cells = {}
        for step, action in self.steps.items():
            prev_loc = np.array([i, j]) + action
            cells[step] = self.matrix[prev_loc[0], prev_loc[1]]
        return cells
    
    def _get_action_seq(self):
        i, j = self.n1 - 1, self.n2 - 1
        action = self.action_matrix[i, j]
        action_seq = [action]
        while action != 'fin':
            i += self.steps[action][0]
            j += self.steps[action][1]
            action = self.action_matrix[i, j]
            action_seq.append(action)
        return action_seq[::-1]

# Test
edit = EditDistance('slap', 'happy')
cost = edit.get_cost()
print('Minimum edit cost:', cost)
edit.print_matrix()
print('Action matrix:\n', edit.action_matrix)
edit.align()
edit.print_seq()

edit.set_words('mystery utopia', 'blustery dsytopia')
cost = edit.get_cost()
print('Minimum edit cost:', cost)
edit.align()
edit.print_seq()
