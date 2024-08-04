from comments import ytComments
from score import sentimentScore
class analyzer:
    """
    Takes <limit> number of comments from the specified video using the api defined in <api> and performs sentiment analysis on them.

    Parameters:

    video_link [string]: the full https link of the youtube video copied from the address bar
    api [string]: The youtube developer api key used to get comments from youtube
    limit [int]: The upper bound of the number of comments to analyze. it always overflows by 100 no matter the value...

    Returns:
 
    list[{"positive":[list], "negative":[list], "neutral:[list]"}, polarity [list]] a list containing all the positive, negative, neutral comments and the polarities of each comment.
    """

    def __init__(self, api, video_link, limit = 600) -> None:
            self.LINK = video_link
            self.LIMIT = limit
            self.API_KEY = api
            
    def get_analysis(self):

        relevant_comments = ytComments.getComments(self.LINK, self.API_KEY, self.LIMIT)

        polarityList = []
        positive_comments = []
        negative_comments = []
        neutral_comments = []

        for items in relevant_comments:
            polarity = sentimentScore.getSentimentScore(items)
            polarityList.append(polarity)
            if polarity["compound"] > 0.05:
                positive_comments.append(items)
            elif polarity["compound"] < -0.05:
                negative_comments.append(items)
            else:
                neutral_comments.append(items)

        return [positive_comments, negative_comments, neutral_comments, polarityList]
    





