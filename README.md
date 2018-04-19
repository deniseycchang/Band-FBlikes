# Bands with debut album before 2000 and still widely liked nowadays (More than 10 million Facebook likes)

Presenting the Facebook likes (> 10 million) of bands who have founded before 2000.

## Motivation
I was interested in the bands who have founded for decades and still widely liked. So I look for the bands with debut album before the year 2000 (not included), and also having more than 10 million Facebook likes currently. 

## Files
- `Band_debutYr.csv`: The names and the debut album year of selected bands.
- `FBlikes_Scraping.py`: Scraping Facebook fan pages to get current Facebook likes of bands.
- `FBlikes.csv`: Name, debut album year and Facebook likes of selected bands.
- `Plot_Band-vs-FBlikes.py`: Using the data from `FBlikes.csv` to plot the figure of bands versus the Facebook likes.
- `Band_FBlikes.png`: Horizontal bar graph on Bands versus Facebook likes

## Tools
* Python: WebScraping, data type conversion.
* MatPlotLib: Visualization

## Methodology
* Band selection: Top 100 artists of all time from Rolling Stone + my knowledge to pick bands. The list is stored in `Band_debutYr.csv`.
* Web Scraping: Scraping the Facebook fan page for the number of Facebook likes since it is dynamic.
  - The facebook fan page is "https://www.facebook.com/" + [band name] + "/". No space or "/" included in [band name].
  - Since the number of likes is right before the words “people like”, search the string “people like” and count few characters before to get the number.
