#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : tweet.py
# Author: chen
# Date  : 2020-04-18

from typing import List
import time

class Twitter:
    follow_set = {}
    article = {}
    m = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_set = {}
        self.article = {}
        self.m = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """

        if userId in self.article.keys():
            self.article[userId].append([tweetId, self.m])
        else:
            self.article[userId] = [[tweetId, self.m]]
        self.m += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user_list = self.article[userId][:] if userId in self.article.keys() else []

        if userId in self.follow_set.keys():
            follow_list = self.follow_set[userId]
            for follow_id in follow_list:
                if follow_id in self.article.keys():
                    user_list.extend(self.article[follow_id])
        if user_list is not None and len(user_list) > 0:
            user_list.sort(key=lambda x: x[1], reverse=True)
            file_list = []
            if len(user_list) > 10:
                user_list = user_list[0:10]
            for data in user_list:
                file_list.append(data[0])
            return file_list
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.follow_set:
                follow_list = self.follow_set[followerId]
                if followeeId not in follow_list:
                    follow_list.append(followeeId)
            else:
                self.follow_set[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follow_set.keys():
            follow_list = self.follow_set[followerId]
            if followeeId in follow_list:
                follow_list.remove(followeeId)
                if len(follow_list) == 0:
                    self.follow_set.pop(followerId)
                else:
                    self.follow_set[followerId] = follow_list

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)