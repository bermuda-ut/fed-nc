class AlphaBeta(object):
    def __init__(self, max_depth=float("inf")):
        """
        :param max_depth: max depth to use for all moves made by alpha beta
        """
        self.max_depth = max_depth

    def next_move(self, state, max_depth_override=None):
        """
        returns a maximizing action from a given state by traversing a maximum of max_depth
        :param state: a game state
        :param max_depth_override: overrides the original set max depth for this move only [default=original max_depth]
        """
        possible_actions = state.get_actions()
        maximum_depth = self.max_depth if max_depth_override is None else max_depth_override

        best_move = None
        v = float("-inf")
        alpha = float("-inf")
        beta = float("inf")
        for move in possible_actions:
            ret_val = self._min_move(state.apply_action(move), alpha, beta, 0, maximum_depth)
            if ret_val > v:
                v = ret_val
                best_move = move
            alpha = max(alpha, v)

        return best_move

    def _min_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("inf")
        for move in state.get_actions():
            v = min(v, self._max_move(state.apply_action(move), alpha, beta, depth+1, max_depth))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def _max_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("-inf")
        for move in state.get_actions():
            v = max(v, self._min_move(state.apply_action(move), alpha, beta, depth+1, max_depth))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
