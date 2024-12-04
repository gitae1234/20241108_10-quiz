#1 Linechart

import matplotlib.pyplot as plt
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

x = [1,2,3,4,5]
y = [10,15,13,18,20]

plt.plot(x,y, marker='o', linestyle='-', color='b', label='temperature')

plt.title('Daily temperature trend')

plt.xlabel('Time (hour)')
plt.ylabel('Temperature (C)')

plt.legend()

plt.grid(True)

output_path = os.path.join(output_dir, "Linechart.png")
plt.savefig(output_path)

plt.savefig("./results/Linechart.png")


#2.Barchart

import matplotlib.pyplot as plt
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

categories = ['Apple','Banana','Orange','Strawberry','Grape']
values = [25,30,15,20,35]

plt.clf()
plt.bar(categories, values, color='skyblue')

plt.title('Fruit Sales')

plt.xlabel('Fruit')
plt.ylabel('Sales')

output_path = os.path.join(output_dir, "Barchart.png")
plt.savefig(output_path)
plt.close()

plt.savefig("./results/Barchart.png")


#3 Histogramchart

import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

data = np.random.randn(1000)

plt.clf()
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

plt.title('Histogram Chart')

plt.xlabel('Values')
plt.ylabel('Frequency')

plt.savefig("./results/Histogramchart")


#4 Piechart

import matplotlib.pyplot as plt
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

labels = ['English', 'Math', 'Science', 'History']
sizes = [45,30,15,10]

plt.clf()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue','lightgreen','lightcoral','lightsalmon'])

plt.title('Subjects Distribution')

plt.savefig("./results/Piechart.png")


#5 Scatterchart

import matplotlib.pyplot as plt
import random
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

x = [random.uniform(0,100) for _ in range(1000)]
y = [random.uniform(0,100) for _ in range(1000)]

plt.clf()

plt.scatter(x,y, label='Random Data Points', color='green', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend()

plt.savefig("./results/Scatterchart.png")


#6 Scatterchart_2

import matplotlib.pyplot as plt
import random
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

x = [random.uniform(0,100) for _ in range(200)]
y = [2 * val + 1 + random.uniform(-10,10) for val in x]

plt.clf()

plt.scatter(x,y, label='Scatter Plot', color='blue', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend()

plt.savefig("./results/Scatterchart_2.png")


#7 Scatterchart_withline

import matplotlib.pyplot as plt
import random
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

x = [random.uniform(0,100) for _ in range(200)]
y = [2 * val + 1 + random.uniform(-10,10) for val in x]

plt.clf()

plt.scatter(x,y, label='Scatter Plot', color='blue', marker='o', s=30, alpha=0.5)

x_line = range(101)
y_line = [2 * val + 1 for val in x_line]
plt.plot(x_line, y_line, label='y = 2x+1', color='r')

plt.title('Scatter Plot Example')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend()

plt.savefig("./results/Scatterchart_with_line.png")


#8 Boxplot
import matplotlib.pyplot as plt
import random
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

data = [random.gauss(0,1) for _ in range(100)]
outliers=[10,-10]

plt.clf()

plt.boxplot(data+outliers,vert=False, patch_artist=True)

plt.title('Boxplot Example with Outliers')

plt.xlabel('Values')

plt.xticks(range(-15,16,5))

plt.savefig("./results/Boxplot.png")


#9 Heatmap
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = "./results"
os.makedirs(output_dir, exist_ok=True)

data=np.random.rand(10,10)

plt.clf()

heatmap=plt.imshow(data, cmap='YlGnBu', aspect='auto')

plt.colorbar(heatmap)

plt.title('Heatmap Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.savefig("./results/Heatmap.png")
