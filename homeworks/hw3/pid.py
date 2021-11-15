#!/usr/bin/env python


class PID:

    # TODO: Complete the PID class. You may add any additional desired functions

    def __init__(self, Kp, Ki=0.0, Kd=0.0):
        # TODO: Initialize PID coefficients (and errors, if needed)
        # pass
        self.K_p = Kp
        self.K_i = Ki
        self.K_d = Kd
        self.P = 0.0
        self.I = 0.0
        self.D = 0.0

    def UpdateError(self, cte):
        # TODO: Update PID errors based on cte
        # pass
        self.D = float(cte) - self.P
        self.P = float(cte)
        self.I += float(cte)
        print("P: ", self.P, "I: ", self.I, "D: ", self.D)

    def TotalError(self):
        # TODO: Calculate and return the total error
        return self.K_p * self.P + self.K_i * self.I + self.K_d * self.D