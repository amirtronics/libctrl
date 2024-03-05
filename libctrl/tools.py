class Gains:
    def __init__(self):
        self.kp = 0
        self.ki = 0
        self.kd = 0

class PidController:
    def __init__(self, _gains, _sample_time, _anti_windup=None):
        
        self.gains = Gains()
        self._setGains(_gains)
        self._ts = _sample_time
        self._sum = 0
        self._prev_error = 0
        self._antiWindupActivation = _anti_windup


    def _setGains(self, _gains_list):
        self.gains.kp = _gains_list[0]
        self.gains.ki = _gains_list[1]
        self.gains.kd = _gains_list[2]

    def _antiWindup(self, val):
        if val > 50:
            return 50
        elif val < -50:
            return -50
        else:
            return val


    def _cmd_sat(self, val):
        if val > 100:
            return 100
        elif val < -100:
            return -100
        else:
            return val

    def _integral(self, error):
        self._sum = self._sum + error*self._ts

        if self._antiWindupActivation is None:
            return self._sum
        else:
            return self._antiWindup(self._sum)

    def _derivateive(self, error):
        derivative = (error-self._prev_error)/self._ts
        self._prev_error = error
        return 0
    
    def compute(self, error):
        _contorlSignal = self.gains.kp*error + \
            self.gains.ki*self._integral(error) + \
            self.gains.kd*self._derivateive(error)
        return self._cmd_sat(_contorlSignal)
