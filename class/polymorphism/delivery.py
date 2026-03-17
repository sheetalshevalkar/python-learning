class Delivery:
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def deliver(self):
        print("Delivering by bike")
class DroneDelivery(Delivery):
    def deliver(self):
        print("Delivering by drone")
class TruckDelivery(Delivery):
    def deliver(self):
        print("Delivering by truck")
        
list_of_deliveries = [BikeDelivery(), DroneDelivery(), TruckDelivery()]
for delivery in list_of_deliveries:
    delivery.deliver()