# 👁️‍🗨️ YT comments Analyzer 

### Description
A python package that allows you to perform sentiment analysis of comments on any Youtube video. 

- using Google API Client Library to interact with the YouTube Data API to fetch video comments.

- using regex to filter out hyperlinks, html tags and entities. Sentences with more than 65% composition of emojis are discarded.

- using VADER, a rule based model specifically fine tuned for analyzing sentiments in social media texts

for optimization purposes, the number of comments you recievce per API call is set to 100. (The maximum). This can lead to issues where the number of comments you actually recieve is more than you have specified. 

#### Why this package?
Youtube has very few filters for their comments. You often have to scroll very far to see negative comments. Also, since the dislike count has been removed since 2021, you cannot effectively view how well someone's video is doing. With this package you can retrieve up to 12000 comments and separate them into positive, neutral, and negative categories for further analysis.
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

