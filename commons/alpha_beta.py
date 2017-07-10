class AlphaBeta(object):
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def next_move(self, state, max_depth_override=None):
        """
        returns a maximizing action from a given state by traversing a maximum of max_depth
        """
        possible_actions = state.get_actions()
        max_depth_override = self.max_depth if not max_depth_override else max_depth_override
        if len(possible_actions) == 0:
            return None
        v = self._max_move(state, float("-inf"), float("inf"), 0, max_depth_override)
        #for move in possible_actions:
        #    if state.apply_action_copy(move).evaluate() == v:
        #       return move
        raise Exception("Logic error, fatal")

    def _min_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("inf")
        for move in state.get_actions():
            v = min(v, self._max_move(state.apply_action_copy(move), alpha, beta, depth+1, max_depth))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def _max_move(self, state, alpha, beta, depth, max_depth):
        if state.is_terminal() or depth >= max_depth:
            return state.evaluate()
        v = float("-inf")
        for move in state.get_actions():
            v = max(v, self._min_move(state.apply_action_copy(move), alpha, beta, depth+1, max_depth))
            if v >= beta:
                return v
            alpha = max(v, alpha)
        return v
