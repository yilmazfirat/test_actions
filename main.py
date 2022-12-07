import pandas as pd
import numpy as np
import hvplot.pandas as hvplot
import holoviews
import panel as pn

def add(x, y):
    """add function"""
    return x+y

z = add(3, 4)

dict = {
'x': [1,3,4,9],
'y': [2,6,8,18]
}

df = pd.DataFrame(dict,columns=['x','y'])
linear_plot= df.hvplot.scatter('x','y')

if __name__=="__main__":
    pn.Column(linear_plot).show()
