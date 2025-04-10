
import matplotlib.pyplot as plt
#Temperature change values from the databse rounded to 3dp
input_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
Afghanistan = [0.777, 0.062, 2.744, -5.232, 1.868, 3.629, -1.432, 0.389, -2.298, 0.804, -1.487, -1.305, -2.951, -1.184, -0.490, 0.409, -3.014, -0.663, 0.141, -0.393, 0.724, 0.678, 0.524, -0.058, 0.435, 0.332, 0.655, 0.150, -1.108, 0.634, 0.018] 
Albania     = [0.180, 1.414, -1.783, -2.319, 0.635, -1.501, -1.887, -2.290, -0.868, 1.797, 2.397, 1.629, 0.244, 0.743, -0.648, -0.057, 1.238, 0.183, -0.528, -1.577, -2.543, 0.336, 0.610, 1.098, -0.933, 0.668, -0.167, 2.543, -0.697, -0.972, -0.491]

fig, ax = plt.subplots()
ax.plot(input_values, Afghanistan, 'mD:')
ax.plot(input_values, Albania, 'ro--')

plt.xlabel("Year")
plt.ylabel("Temperature Change")
plt.title("Comparing the temperate change in Afghanistan and Albania in January from 1961-1991")

ax.set_xticks(input_values)
ax.set_yticks(range(-6, 5))

plt.grid(True)
plt.show()