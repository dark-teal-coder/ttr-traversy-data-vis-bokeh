## `figure` to create plots
## `output_file` to name the HTML file to generate
## 'show' to generate and output HTML files
import imp
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
## 
from bokeh.models.tools import HoverTool
import pandas as pd

## Data
# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]
## Read in CSV data file with Pandas
df = pd.read_csv('cars.csv')

## Create ColumnDataSource from DataFrame
# car = df['Car']
# hp = df['Horsepower']
source = ColumnDataSource(df)

## Name the output HTML file
output_file('index.html')

## Create a list for `y_range` in `figure()`
cars_list = source.data['Car'].tolist()

## Add a plot
p = figure(
	y_range=cars_list,
	plot_width=800,
	plot_height=600,
	title = 'Cars with Top Horsepower',
	x_axis_label = 'Horsepower',
	# y_axis_label = 'Y Axis',
	## No graph tool displayed
	# tools=''
	## Add some graph tools
	tools='pan, box_select, zoom_in, zoom_out, save, reset'
)

## Render glyph
## Add a line graph
# p.line(x, y, legend='Test', line_width=2)
## Add a horizontal bar chart
p.hbar(
	y='Car',
	right='Horsepower',
	left=0,
	height=0.4,
	color='green',
	fill_alpha=0.5,
	source=source
	)

## Add Tooltips
## When hovering over each bar, car name, price, horsepower and image of the car will be shown
hover = HoverTool()
hover.tooltips = """
<div>
	<h3>@Car</h3>
	<div><strong>Price: </strong>@Price</div>
	<div><strong>Horsepower: </strong>@Horsepower</div>
	<div><img src="@Image" alt="Car image" width="200" /></div>
</div>
"""
## Show tools
p.add_tools(hover)

## Show the plot
## Each call will open up a new tab in the browser
show(p)
## Open the output HTML file and refresh it after each run
# save(p)