import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Sales by Item')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Item')
    plt.ylabel('Price')
    plt.tight_layout()
    graph = get_graph()

    return graph

def get_pie_chart(labels, sizes):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Sales Distribution')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    graph = get_graph()
    
    return graph

def get_bar_chart(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Monthly Sales')
    plt.bar(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.tight_layout()
    graph = get_graph()
    
    return graph

def get_scatter_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Price Comparison')
    plt.scatter(x, y)
    plt.xlabel('Product')
    plt.ylabel('Price')
    plt.tight_layout()
    graph = get_graph()
    
    return graph

def get_horizontal_bar(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Top Products')
    plt.barh(x, y)
    plt.xlabel('Sales')
    plt.ylabel('Product')
    plt.tight_layout()
    graph = get_graph()
    
    return graph

def get_donut_chart(labels, sizes):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 3))
    plt.title('Category Breakdown')
    # Create a circle at the center
    circle = plt.Circle((0,0), 0.70, fc='white')
    plt.pie(sizes, labels=labels, wedgeprops={'edgecolor': 'white'})
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.axis('equal')
    plt.tight_layout()
    graph = get_graph()
    
    return graph
