# Matplotlib
- https://matplotlib.org/stable/index.html
- https://www.w3schools.com/python/matplotlib_getting_started.asp

### matplotlib with pandas
- https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html

### Changes to the default stype
- https://matplotlib.org/3.5.0/users/prev_whats_new/dflt_style_changes.html


```python
import matplotlib as mpl 
import matplotlib.pyplot as plt

mpl.rcParams['xtick.color'] = 'red'
mpl.rcParams['ytick.color'] = 'green'
plt.ion() # interactive mode
```