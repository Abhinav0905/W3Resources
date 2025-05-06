class SphereVolumeCalculator():

    def _take_input(self):
        radius = float(input("Enter the radius of the sphere: "))
        return radius
    
    def sphere_volume(self):
        abc = self._take_input()
        volume = (4/3) * 3.1417 * (abc**3)
        return volume
    
if __name__ == "__main__":
    obj = SphereVolumeCalculator()
    vol = obj.sphere_volume()
    print(vol)