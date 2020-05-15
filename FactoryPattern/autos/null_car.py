class NullCar(object):
    def start(self, car_name):
        self.car_name = car_name
        print('Unknown car "%s."' % self.car_name)

    def stop(self):
        pass