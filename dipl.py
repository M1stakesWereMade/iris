import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Загружаем данные
iris = sns.load_dataset('iris')

# Функция для визуализации с помощью Matplotlib
def visualize_matplotlib(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data['sepal_length'], data['sepal_width'], c=data['species'].astype('category').cat.codes, cmap='viridis')
    plt.title('Matplotlib: Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.colorbar(ticks=[0, 1, 2], label='Species')
    plt.clim(-0.5, 2.5)
    plt.show()

# Функция для визуализации с помощью Seaborn
def visualize_seaborn(data):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=data, x='sepal_length', y='sepal_width', hue='species', palette='viridis')
    plt.title('Seaborn: Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.show()

# Функция для визуализации с помощью Plotly
def visualize_plotly(data):
    fig = px.scatter(data, x='sepal_length', y='sepal_width', color='species', title='Plotly: Sepal Length vs Sepal Width')
    fig.show()

# Запуск визуализаций и замер времени
start_time = time.time()
visualize_matplotlib(iris)
print("Matplotlib time: %s seconds" % (time.time() - start_time))

start_time = time.time()
visualize_seaborn(iris)
print("Seaborn time: %s seconds" % (time.time() - start_time))

start_time = time.time()
visualize_plotly(iris)
print("Plotly time: %s seconds" % (time.time() - start_time))
