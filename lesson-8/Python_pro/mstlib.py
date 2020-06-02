import matplotlib.pyplot as plot
import numpy


def f1(x):
    return x * 2 - numpy.cos(x)


def f2(x):
    return x ** 3 - numpy.sqrt(x)


def f3(x):
    return numpy.sin(x) - numpy.cos(2 * x)


arr1 = numpy.arange(-5.0, 5.0, 0.1)
arr2 = numpy.arange(0.0, 5.0, 0.02)
arr3 = numpy.arange(-5.0, 5.0, 0.01)

plot.figure(1)
plot.subplot(211)
plot.plot(arr1, f1(arr1))
plot.title(' x*2 - cos(x)')

plot.subplot(212)
plot.plot(arr2, f2(arr2))
plot.title('x**3 - sqrt(x)')

plot.figure(2)
plot.subplot(211)
plot.plot(arr3, f3(arr3))
plot.title('sin(x)-cos(2*x)')

plot.show()
