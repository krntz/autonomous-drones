import logging

from entities.boids.boid import Boid, BoidTypes
from entities.boids.rules import fly_towards_center, match_velocity

logger = logging.getLogger(__name__)


class StandardBoid(Boid):
    def __init__(self,
                 uid,
                 flight_zone,
                 separation,
                 alignment,
                 cohesion,
                 visual_range):

        super().__init__(uid, flight_zone, separation)

        self.alignment = alignment
        self.cohesion = cohesion

        self.visual_range = visual_range

        self._type = BoidTypes.STANDARD

    def update(self, delta_time):
        """
        Takes the positions of all boids in the swarm, converts them to distances
        to the current boid, and figures out how to change the position
        for the next time step
        """

        logger.debug(f"Running rules for boid with id {self.uid}")

        fly_towards_center(self, self.detected_boids, delta_time)
        match_velocity(self, self.detected_boids, delta_time)

        logger.debug(
            f"New velocity for boid with id {self.uid}: {self.velocity}")

        super().update(delta_time)
