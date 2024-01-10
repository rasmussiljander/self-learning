"""Vehicle: 
        A vehicle has mass, size, and steering attributes, it is set in a world and has a very real location. These are all
        initialliy set in the __init__method.
        
        The vehicle also needs movement patterns that are essential in deriving it as autonomous object. These include seek,
        arrive, path following, obstacle avoidance, etc."""

from vector import Vector
from path import Path


class Vehicle:
    """Vehicle Class for handling the individual vehicles"""

    def __init__(self, max_force_to_mass, max_speed, direction, path, size, world):
        self.fm = max_force_to_mass
        self.max_speed = max_speed
        self.direction = direction

        self.x = path[0][0]
        self.y = path[0][1]
        self.sf = path
        self.target = path[1]

        self.size = size
        self.world = world
        self.velocity = self.direction.set_magn(self.max_speed)

    def arrive(self):
        """Arrive method:
        a) Vehicle tries to get to its finish point as quickly as possible --> target location is set.

            target = finish.

        b)Then we need to change the heading of the vehicle be calculating a steer vector. The steer vector is the
        difference between the desired (straight from start -> finish) and the velocity vector.

            steer = desired - velocity

        c) Then we add the steer to velocity to achieve new, better heading.

            velocity = velocity + steer

        d) Lastly, we need to map the speed of the vehicle so that it is at full stop when at target. This can, conveniently,
        be mapped as max speed/map_distance * distance to point:
            speed = (max_speed/map_distance)* distance , map_distance = 150

        """

        # a)
        target = Vector(self.target[0], self.target[1])
        loc = Vector(self.x, self.y)

        # b)
        desired = target.sub(loc)
        distance = desired.get_magn()  # finding distance from location to finish
        desired = desired.set_magn(self.max_speed)

        steer = desired.sub(self.velocity)
        steer = self.get_steer_vector()

        # c)
        self.velocity = self.velocity.add(steer)

        # d)
        speed = self.max_speed - (self.max_speed / 150) * (150 - distance)
        self.velocity = self.velocity.set_magn(speed)

        update = loc.add(self.velocity)

        self.x = update.x
        self.y = update.y

        v0 = self.velocity.get_unit()
        self.direction = v0
        return self.direction

    def seek(self, destination):
        """Seek: Vehicle tries to get to target location.
        Same logic as in arrive (below) but there is no mapping of velocity"""
        target = Vector(destination[0], destination[1])
        loc = Vector(self.x, self.y)

        desired = target.sub(loc)

        desired = desired.set_magn(self.max_speed)

        steer = desired.sub(self.velocity)
        steer = steer.set_limit(self.fm)

        self.velocity = self.velocity.add(steer)
        self.velocity = self.velocity.set_limit(self.max_speed)

        update = loc.add(self.velocity)

        self.x = update.x
        self.y = update.y

        v0 = self.velocity.get_unit()
        self.direction = v0

    def get_steer_vector(self):
        """GET STEER VECTOR
        Returns the steer vector that is applied to the car."""
        target = Vector(self.target[0], self.target[1])
        loc = Vector(self.x, self.y)

        desired = target.sub(loc)
        desired = desired.set_magn(self.max_speed)

        steer = desired.sub(self.velocity)
        return steer.set_limit(self.fm)

    def check_danger(self):
        """CHECK DANGER
        Checking if the vehicle is about to crash into another car."""
        list = self.world.get_vehicles()
        index = list.index(self)
        self_location = Vector(self.x, self.y)
        predict_vec = self.velocity.set_magn(20)
        prediction = self_location.add(predict_vec)
        danger_coors = []
        for i in range(len(list)):
            if i != index:
                other_location = Vector(list[i].x, list[i].y)
                diff = prediction.sub(other_location)

                if diff.get_magn() < 50:
                    danger_coors.append(other_location)

        return danger_coors

    def escape(self, coors):
        """ESCAPE
        Method for calculating escape coordinates and seeking them."""
        sum_loc = Vector(0, 0)
        self_location = Vector(self.x, self.y)
        for i in range(len(coors)):
            sum_loc = sum_loc.add(coors[i])

        avg_loc = sum_loc.mult(1 / len(coors))
        escape_dir = self_location.sub(avg_loc).get_unit()
        escape_loc = self_location.add(escape_dir.mult(50))
        self.seek([escape_loc.x, escape_loc.y])

    def path_following(self):
        """PATH FOLLOWING
        Method for the whole movement pattern of the vehicle. Two steps: a) Find location in relation to path b) act accrodingly
        """
        # a)
        self.path = Path(self.sf[0], self.sf[1])  # Making path vector (from start to finish)'''
        loc = Vector(self.x, self.y)

        # b)
        dis = self.path.finish.sub(loc)

        if dis.get_magn() <= 150:
            self.arrive()
        else:
            coors = self.check_danger()
            if len(coors) > 0:
                self.escape(coors)
            else:
                self.seek([self.target[0], self.target[1]])
