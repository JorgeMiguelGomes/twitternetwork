# Twitter Network
The Code necessary to extract tweets from the Twitter API and produce a csv file that can be imported on Gephi to visualize a network


![Map_Biden_Deprem](https://user-images.githubusercontent.com/34355337/220284819-265b65c1-0753-4d36-a114-dcbe95878ce8.png)


# What you need

## Create a virtual environment 

`mkdir your_project`

`cd your_project`

`virtualenv --python=python3 .`

## Activate your virtual environment 

`source /bin/activate`

## Install the libraries required

`pip3 install -r requirements.txt`


# You are ready to go

Run `python3 fetch.py` (this might take a while depending on what you are fetching)
Run `python3 edges.py`

# Open Gephi 

## Import CSV produced by edges.py

File -> Import Spreadhsheet...

## Run some stats

In the Statistics, in the Context Tab, run **Modularity** and **Statistical Inference**

## Start building your visualization

In the **Overview** tab, under Appearance, select **Nodes** and **Partition** and click **Apply**

Choose a Layout and click **Run**

## Notes

When running the layout, your graph might go out of canvas. Don't worry. 

You can stop the run, and choose "Contraction" and run that, and it will zoom out. 

The same applies if your visualization is too small. Click "Expansion" and it will zoom in


## Tips

Experiment. Experiment. Experiment. The more data you have the more complex your visuazliation might look. Use the overview to detect important information (and make screenshots of it)









