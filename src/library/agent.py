import numpy as np


class Agent:

    """All files that are re-used in various steps of the project.

    """

    def __init__(self, typ, initial_location, n_neighbours, require_same_type):
        self.type = typ
        self.location = np.asarray(initial_location)
        self._n_neighbours = n_neighbours
        self._require_same_type = require_same_type

    def _draw_new_location(self):
        self.location = np.random.uniform(size=self.location.shape)

    def _get_distance(self, other):
        """Return the Euclidean distance between self and other agent."""
        return np.linalg.norm(self.location - other.location)

    def _happy(self, agents):
        """True if sufficient number of nearest neighbours are of the same type."""
        # Create a sorted list of pairs (d, agent), where d is distance from self
        distances = [(self._get_distance(other), other) for other in agents if not self == other]
        distances.sort()
        # Extract the types of neighbouring agents
        neighbour_types = [other.type for d, other in distances[:self._n_neighbours]]
        # Count how many neighbours have the same type as self
        n_same_type = sum(self.type == nt for nt in neighbour_types)
        return n_same_type >= self._require_same_type

    def move_until_happy(self, agents):
        """If not happy, then randomly choose new locations until happy."""
        while not self._happy(agents):
            self._draw_new_location()