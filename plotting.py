from motionDetector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource as cds

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = df

p = figure(x_axis_type="datetime", height=100, width=500, sizing_mode='scale_width', title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start:", "@Start_string"), ("End:", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("GraphOfMotionTime.html")
show(p)