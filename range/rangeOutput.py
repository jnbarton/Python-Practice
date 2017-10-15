
class RangeOutput():
    """Output a range object."""

    def get_even(lowerBound, upperBound):
        if lowerBound % 2 == 0:
            return range(lowerBound, upperBound, 2)
        else:
            print("Lower bound must be an even number.");

    def get_odd(lowerBound, upperBound):
        if lowerBound % 2 == 1:
            return range(lowerBound, upperBound, 2)
        else:
            print("Lower bound must be an odd number.");



