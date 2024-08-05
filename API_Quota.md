One API call using the 
```python
youtube.commentThreads.list()
```
function costs 1 unit, with each call returning 100 comments. 
According to the Official [YouTube Quota website](https://developers.google.com/youtube/v3/determine_quota_cost), one API has 10,000 free quotas by default. This means you can theoretically perform sentiment analysis on 1,000,000 YouTube comments. I have only tested this upto 20,000 comments however.
