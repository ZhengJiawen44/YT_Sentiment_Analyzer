# 👁️‍🗨️ YT comments Analyzer 

### Description
A python package that allows you to perform sentiment analysis of comments on any Youtube video. 

- using Google API Client Library to interact with the YouTube Data API to fetch video comments.

- using regex to filter out hyperlinks, html tags and entities. Sentences with more than 65% composition of emojis are discarded.

- using VADER, a rule based model specifically fine tuned for analyzing sentiments in social media texts

for optimization purposes, the number of comments you recievce per API call is set to 100. (The maximum). This can lead to issues where the number of comments you request for is more than you have specified. 

### Installation

To install the current release

```
$ pip install YT_Sentiment
```
*Try your first YT_Sentiment program*

```
$ python
```
```python
>>> import YT_Sentiment as yts
>>> analyzer = yts("API_KEY", "VIDEO_LINK", 600)
>>> analyzer.get_analysis()
>>> <class 'list'>
```
### License
[MIT License](LICENSE)
