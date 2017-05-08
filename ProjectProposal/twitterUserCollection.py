#!/usr/bin/python3

import csv
import tweepy
from tweepy import OAuthHandler

def main():
    consumer_key= 'twittwrConsumerKey'
    consumer_secret= 'twitterConsumerSecret'
    access_token='twitterAccessToken'
    access_secret='twitterAccessSecret'

    #Authorizing the twitter account to set up auth object
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
     
    api = tweepy.API(auth)
    user=api.get_user('greatartbot') # Specify screenname of the user to get the userJson(Users Object)
    print(user.id)
    print(user.id_str)
    print(user.screen_name)
    print(user.location)
    print(user.description)
    print(user.url)
    print(user.followers_count)
    print(user.friends_count)
    print(user.listed_count)
    print(user.created_at)
    print(user.favourites_count)
    print(user.verified)
    print(user.statuses_count)
    print(user.lang)
    print(user.status)
    print(user.default_profile)
    print(user.default_profile_image)
    print(user.has_extended_profile)
    print(user.name)

    #writing the userprofile to the tweets.csv with bot or not bot label
    with open('tweets.csv','a') as f:
        writer=csv.writer(f)
        writer.writerow([user.id,user.id_str,user.screen_name,user.location,user.description,user.url,user.followers_count,user.friends_count,user.listed_count,user.created_at,user.favourites_count,user.verified,user.statuses_count,user.lang,user.status,user.default_profile,user.default_profile_image,user.has_extended_profile,user.name,0])

        

if __name__=="__main__":main() 
         

