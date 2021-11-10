import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64 
from django.contrib.auth.models import User

def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman

def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor to the beginning of the screen  
    buffer.seek(0)
    #retrieve the entire content of the 'file'
    image_png = buffer.getvalue()
    
    # encoding and decoding
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of the buffer 
    buffer.close() 

    return graph

def get_simple_plot(chart_type, *args, **kwargs): # arguments / key  word arguments
    # https://matplotlib.org/stable/tutorials/introductory/usage.html#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4)) # 10 width 4 height
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')

    if chart_type == 'bar plot':
        title = "Total Price by Day (bar)"
        plt.title(title)
        plt.bar(x, y) # x will be the date, y will be the total price grouped by date
    elif chart_type == 'line plot':
        title = "Total Price by Day (line)"
        plt.title(title)
        plt.plot(x, y)
    else:
        title = "Product Count Sold"
        plt.title(title)
        sns.countplot('name', data=data) # count of product sold by date with name 
    plt.xticks(rotation=45) # Get or set the current tick locations and labels of the x-axis. (all charts)
    # doesn't look nice right now, but will when there is a lot of records made  
    plt.tight_layout() # automatically fits the graph to the area so it looks nicer

    graph = get_image()
    return graph     