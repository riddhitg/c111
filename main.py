import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics 
import csv
import random
import pandas as pd

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data],["Math score"], show_hist = False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_deviation = statistics.stdev(mean_list)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#finding the mean of the first data(student who got tablet with learnig material)
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("mean of sample 1: ", mean_of_sample1)
fig = ff.create_distplot([mean_list],["student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0,0.17], mode = "lines", name = "mean")) 
fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1],y = [0,0.17], mode = "lines", name = "mean of sample 1")) 
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 3 end"))
fig.show()

#finding the mean of the second data(student who got extra classes)
df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2: ", mean_of_sample2)
fig = ff.create_distplot([mean_list],["student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0,0.17], mode = "lines", name = "mean")) 
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2],y = [0,0.17], mode = "lines", name = "mean of sample 2")) 
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 3 end"))
fig.show()

#finding the mean of the third data(student who got math worksheets)
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample 3: ", mean_of_sample3)
fig = ff.create_distplot([mean_list],["student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0,0.17], mode = "lines", name = "mean")) 
fig.add_trace(go.Scatter(x = [mean_of_sample3, mean_of_sample3],y = [0,0.17], mode = "lines", name = "mean of sample 3")) 
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end],y = [0,0.17], mode = "lines", name = "standard deviation 3 end"))
fig.show()

#finding the Z score of the first data
z_score1 = (mean-mean_of_sample1)/std_deviation
print("the Z score for sample 1 is: ", z_score1)
#finding the Z score of the second data
z_score2 = (mean-mean_of_sample2)/std_deviation
print("the Z score for sample 2 is: ", z_score2)
#finding the Z score of the third data
z_score3 = (mean-mean_of_sample3)/std_deviation
print("the Z score for sample 3 is: ", z_score3)