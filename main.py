import matplotlib.pyplot as plt
import math

def function(t, y):
    return 2.0 * t * y


def analytic(t):
    y = math.exp(t * t)
    return y


def methodOfEuler(h, yn, t):
    yNew = yn + h * function(t, yn)
    return yNew


def implicitEuler(h, yn, t):
    yn1 = methodOfEuler(h, yn, t)
    yNew = yn + h * function(t, yn1)
    while abs(yn1 - yNew) >= 1e-12:
        yn1 = yNew
        yNew = yn + h * function(t, yn1)
    return yn + h * function(t, yNew)


def trapezoidalRule(h, yn, t):
    yn1 = methodOfEuler(h, yn, t)
    yNew = yn + h / 2 * (function(t - h, yn) + function(t, yn1))
    while abs(yn1 - yNew) >= 1e-12:
        yn1 = yNew
        yNew = yn + h / 2 * (function(t - h, yn) + function(t, yn1))
    return yn + h / 2 * (function(t - h, yn) + function(t, yNew))


xEuler = [float(0)]
xTrapezod = [float(0)]
xAnalytic = [float(0)]

yEuler = [float(1)]
yTrapezod = [float(1)]
yAnalytic = [float(1)]

h = [0.1, 0.05, 0.025]

h1Fault = [float(0)]
h2Fault = [float(0)]

graphs = plt.figure(figsize=(20, 20))

for i in h:
    for j in range(len(xEuler) - 1, len(xEuler) + int(1 / i)):
        xEuler.append(xEuler[j] + i)
        yEuler.append(implicitEuler(i, yEuler[j], xEuler[j] + i))

        xAnalytic.append(xAnalytic[j] + i)
        yAnalytic.append(analytic(xAnalytic[j + 1]))

        h1Fault.append(abs(yEuler[j + 1] - yAnalytic[j + 1]))

        xTrapezod.append(xEuler[j] + i)
        yTrapezod.append(trapezoidalRule(i, yTrapezod[j], xTrapezod[j] + i))

        h2Fault.append(abs(yTrapezod[j + 1] - yAnalytic[j + 1]))

    xEuler.append(float(0))
    xTrapezod.append(float(0))
    xAnalytic.append(float(0))

    yEuler.append(float(1))
    yTrapezod.append(float(1))
    yAnalytic.append(float(1))

    h1Fault.append(float(0))
    h2Fault.append(float(0))


n1 = int(1/h[0])
n2 = int(1/h[1])
n3 = int(1/h[2])

step = graphs.add_subplot(2, 2, 1)
step.set_title("Implicit Euler")
line1, line2, line3 = step.plot(xEuler[0: n1+1], yEuler[0: n1+1], 'r',
                                xEuler[n1+2: n1+n2+3], yEuler[n1+2: n1+n2+3], 'g',
                                xEuler[n1+n2+4: len(xEuler)-2], yEuler[n1+n2+4: len(xEuler)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(2, 2, 3)
step.set_title("Trapezoidal rule")
line1, line2, line3 = step.plot(xEuler[0: n1+1], yTrapezod[0: n1+1], 'r',
                                xEuler[n1+2: n1+n2+3], yTrapezod[n1+2: n1+n2+3], 'g',
                                xEuler[n1+n2+4: len(xEuler)-2], yTrapezod[n1+n2+4: len(xEuler)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(2, 2, 2)
step.set_title("Implicit Euler fault")
line1, line2, line3 = step.plot(xEuler[0: n1+1], h1Fault[0: n1+1], 'r',
                                xEuler[n1+2: n1+n2+3], h1Fault[n1+2: n1+n2+3], 'g',
                                xEuler[n1+n2+4: len(xEuler)-2], h1Fault[n1+n2+4: len(xEuler)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(2, 2, 4)
step.set_title("Trapezoidal rule fault")
line1, line2, line3 = step.plot(xEuler[0: n1+1], h2Fault[0: n1+1], 'r',
                                xEuler[n1+2: n1+n2+3], h2Fault[n1+2: n1+n2+3], 'g',
                                xEuler[n1+n2+4: len(xEuler)-2], h2Fault[n1+n2+4: len(xEuler)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

plt.savefig("example.png")
plt.show()
