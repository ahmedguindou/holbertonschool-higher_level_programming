class Fish:
    """Represents a fish with swimming ability and water habitat."""

    def swim(self):
        """Prints a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message indicating the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying ability and sky habitat."""

    def fly(self):
        """Prints a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message indicating the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that can both swim and fly."""

    def fly(self):
        """Prints a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message indicating
        that the flying fish has a dual habitat."""
        print("The flying fish lives both in water and the sky!")
