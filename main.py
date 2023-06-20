import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_chart_example(x_ser, y_ser):
    
    plt.plot(x_ser, y_ser,
             label="population",
             c="green",
             lw=5) 
    plt.plot(x_ser, y_ser * 2,
             label="population x2",
             c="purple",
             ls="--") 
    plt.ylabel("population (in millions)")
    plt.xlabel("City Class")
    plt.title("Chinese Population Analysis")
    
    plt.savefig("line.png")

def scatter_chart_example(x_ser, y_ser):
    
    plt.figure()
    plt.scatter(x_ser,
                y_ser,
                s=300, 
                marker="x") 
    plt.savefig("scatter.png")

def bar_chart_example(x_ser, y_ser):
    plt.figure()
    plt.bar(x_ser, y_ser)
    plt.savefig("bar.png")

def pie_chart_example(values_ser, labels_ser):
    plt.figure()
    plt.pie(values_ser,
            labels=labels_ser,
            autopct="%1.1f%%") 
    plt.savefig("pie.png")

def histogram_chart_example(values_ser1,
                            values_ser2):
    plt.figure()
    
    plt.hist(values_ser1,
             bins=30,
             alpha=0.5) 
    plt.hist(values_ser2,
             bins=30,
             alpha=0.5)
    plt.ylabel("Count (Frequency) of each X-axis Bin")
    plt.savefig("histogram.png")

df = pd.read_csv("merged.csv")
print(df)

grouped_by_class = df.groupby("class")
class_pop_ser = grouped_by_class["population"].sum()
print(class_pop_ser)

line_chart_example(class_pop_ser.index, 
                   class_pop_ser) 

scatter_chart_example(class_pop_ser.index,
                      class_pop_ser)


bar_chart_example(class_pop_ser.index,
                  class_pop_ser)


pie_chart_example(class_pop_ser, 
                  class_pop_ser.index)


mean = 100
stdev = 25 
num_datapoints = 1000

rand_data1 = np.random.normal(mean,
                              stdev,
                              num_datapoints)

rand_data2 = np.random.normal(mean,
                              stdev / 2,
                              num_datapoints)
histogram_chart_example(rand_data1,
                        rand_data2)
