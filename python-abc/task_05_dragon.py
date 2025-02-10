class SwimMixin:
    """Provides swimming ability."""

    def swim(self):
        """Enables swimming."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability."""

    def fly(self):
        """Enables flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly."""

    def roar(self):
        """Roars loudly."""
        print("The dragon roars!")
