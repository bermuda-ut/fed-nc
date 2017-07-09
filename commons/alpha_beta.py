class AlpaBeta(object):
    def __init__(self, max_depth):
        self.max_depth = depth

    def next_move(self, state, max_depth_override=self.depth):
        """
        returns a maximizing action from a given state by traversing a maximum of max_depth
        """
        possible_actions = state.get_actions()
        if len(possible_actions) == 0:
            return None
        best_move = possible_actions[int(random.random()*len(possible_actions-1))]
        best_v = float('-inf')
        for move in state.get_actions():
            v = _min_move(state.apply_action(move), float("-inf"), float("inf"), 1, max_depth_override)
            if v > best_v:
                best_move = move
                best_v = v
        return best_move

    def _min_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("inf")
        for move in state.get_actions():
            v = min(v, _max_move(state.apply_action(move), alpha, beta, depth+1, max_deptha))
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    def _max_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("-inf")
        for move in state.get_actions():
            v = max(v, _min_move(state.apply_actions(move), alpha, beta, depth+1, max_depth))
            if v >= beta:
                return v
            alpha = max(v, alpha)
        return v
