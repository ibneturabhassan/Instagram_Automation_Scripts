# Instagram_Automation_Scripts

This is collection of three scripts which I have developed for instgram Automation


#list_maker
this script is used to create list of followers that is then fed to follow_req script that sends follow requests from the given list. This script takes a json file as input that is generated using GrowBot chrome extension. This extension can be used to extract followers of any target profile.

#make_post
It picks a random caption from the caption file, select a random set of hashtags, and add a random picture from the images folder and upload it to the given chrome profile where insta account is already logged in

#follow
it sends follow request to the given list, maintains a list of users to which req has already been sent in the dump file.
