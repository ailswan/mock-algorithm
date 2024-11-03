# 355. Design Twitter

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
# and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
# Each call to this function will be made with a unique tweetId.

# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
# Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.

# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.


class Node:
    def __init__(self, val, next, prev) -> None:
        self.val = val
        self.next = next
        self.prev = prev



class Twitter:
    class Node:
        def __init__(self):
            self.followee = set()
            self.tweet = list()

    def __init__(self):
        self.time = 0
        self.recentMax = 10
        self.tweetTime = dict()
        self.user = dict()
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user:
            self.user[userId] = Twitter.Node()
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user:
            return list()
        ans = self.user[userId].tweet[-10:][::-1]
        for followeeId in self.user[userId].followee:
            if followeeId in self.user:
                opt = self.user[followeeId].tweet[-10:][::-1]
                i, j, combined = 0, 0, list()
                while i < len(ans) and j < len(opt):
                    if self.tweetTime[ans[i]] > self.tweetTime[opt[j]]:
                        combined.append(ans[i])
                        i += 1
                    else:
                        combined.append(opt[j])
                        j += 1
                combined.extend(ans[i:])
                combined.extend(opt[j:])
                ans = combined[:10]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.Node()
            self.user[followerId].followee.add(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user:
                self.user[followerId].followee.discard(followeeId)

 
    # def __init__(self) -> None:
    #     # some data structure to keep track of the follow graph
    #     self.follow_adj_list = defaultdict(list)
    #     self.tweeter = defaultdict(list)
    #     self.tweets = Node()

    def postTweet(self, userId: int, tweetId: int) -> None:
        # insert into tweet dictionary the tweetId for the userId key
        # self.tweeter[userId].append(tweetId)
        new_Tweet = Node()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # generate feed based on who the input userId is following
        # traverse the follow_adj_list and grab the tweets from each user that the input user is following
        feed = []

        if userId in self.follow_adj_list:


    def follow(self, followerId:int, followeeId: int) -> None:
        # use adjacency list to represent the DAG of the follower/followees
        if followerId in self.follow_adj_list:
            if followeeId in self.follow_adj_list[followerId]:
                return None
        else:
            self.follow_adj_list[followerId].append(followeeId)

    def unfollow(self, followerId:int, followeeId: int) -> None:
        if followeeId in self.follow_adj_list[followerId]:
            del self.follow_adj_list[followerId][followeeId]
