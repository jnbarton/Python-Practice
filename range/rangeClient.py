from range.rangeOutput import RangeOutput
from range.rangePrinter import RangePrinter

class RangeClient(object):
    """Client for creating/printing range object."""

    def execute():
        lowerBound = int(input("Insert lower bounds: "))
        upperBound = int(input("Insert upper bounds:"))

        answer = input("Want to print odd or even numbers? ")
        even = False

        if (answer.upper() == "EVEN"):
            even = True

        if (not even):
            rangeObj = RangeOutput.get_odd(lowerBound, upperBound)
            RangePrinter.print_range(rangeObj)
        else:
            rangeObj = RangeOutput.get_even(lowerBound, upperBound)
            RangePrinter.print_range(rangeObj)

