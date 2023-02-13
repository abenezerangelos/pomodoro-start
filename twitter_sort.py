'''
For this assignment I will be using two methods to obtain the directory of the file
i.e., I will be using standard I/O function such as input on the console and an optional command line argument
- I will be using an exception handler to make sure its either one of these scenerios since the problem statement in the homework was a bit unclear.
##############################################
# Title: Twitter (PA1)
# Author: Ebenezer Abate
# Version: 1.0
# Date: Feb 8,2023
#
# Description: This program writes a file with a chronologically sorted list of tweets, given two files containing multiple tweets.

##############################################

P.S. i just realized that I had submitted the wrong file yesterday and so can you please not deduct more points, I feel that I need to get a penalty of 20% deduction.
'''
import re
import sys
def read_tweets(tweets):
    '''
    This function parses through lines of twitter posts to get the tweeter,tweet,date and time of each post so it can be sorted by another function
    :param tweets:these are the lines of tweets we are going to pass that are going to be parsed through
    :return:a list of dictionaries where the key,value pair is the category our data belongs in and the following data
    '''
    records_list=[]




    sorter_list=[]
    #iterate through our file containing tweets
    for line in tweets:
        twitter_logs={}
        tweeter=re.match('@\w+',line).group()

        date = re.search('(....\s\d*\s\d*\s..:..:..\s*)$', line).group()

        time = re.search('..:..:..(?=\s*)', line).group()
        tweet=re.search(f'(?<={tweeter}\s).*(?=\s{date})',line).group()
        year=re.match('(....)',date).group()
        month=re.search(f'(?<={year}\s)\d+',date).group()
        day=re.search(f'(?<={month}\s)\d+',date).group()
        twitter_logs["tweeter"]=tweeter
        twitter_logs['tweet']=tweet
        twitter_logs["year"]=year
        twitter_logs["month"]=month
        twitter_logs["day"]=day
        twitter_logs["time"]=time
        time=time[0:2]+time[3:5]+time[6:8]
        if len(month)==1:
            month="0"+month

        if len(day)==1:
            day="0"+day


        sorter=year+month+day+time
        sorter_list.append(sorter)
        twitter_logs["sorter"]=sorter
        records_list.append(twitter_logs)

    return records_list
#merge function
def merge_tweets(records_list1,records_list2):
    '''

    :param records_list1:this is the return from the first implementation of the read_tweets function
    :param records_list2:this is the returned object from the second implementation of the read_tweets function
    :return:this function will return a sorted (based on date and time i.e., chronologically) and merged list of dictionaries
    '''
    merged_records_list=records_list1+records_list2


    #this is a helper function that will help with sorting the list of dictionaries
    def helper(dictionary):
        return dictionary["sorter"]

    #we will be using the default library sort function since we haven't learned any sorting algorithms just yet
    merged_records_list.sort(key=helper,reverse=True)
    return merged_records_list

def write_tweets(merged_records_list):
    '''

    :param merged_records_list: this parameter is the object that is returned from the implementation of the merge_tweets function
    :return: void(we will not be using a return statement in this function) instead this function will write our sorted set of tweets
    '''
    #this variable will be the variable that will hold the count the tweets that contain a hashtag
    hashtag_counter=0
    output_list=[]
    for dictionary in merged_records_list:
        #this is the algorithm that i will be using for the bonus problem.
        hashtag_counter+=dictionary['tweet'].count("#")
        output_string=f"{dictionary['tweeter']} {dictionary['tweet']} {dictionary['year']} {dictionary['month']} {dictionary['day']} {dictionary['time']} \n"
        output_list.append(output_string)

    with open("merged_and_sorted.txt",mode="w") as file_output:
        file_output.writelines(output_list)
        file_output.write(f"Number of hashtags counted within the two files: {hashtag_counter}")



def main():
    '''
    This function is the main function and so will not have any parameters or any return values for that matter
    :return:void
    '''


    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    except Exception:
        file1 = input("Please input the file directory for the location of the first set of tweet data")
        file2 = input("Please input the file directory for the location of the second set of tweet data")
    with open(file1, "r") as x:
        tweets1 = x.readlines()
    with open(file2, "r") as y:
        tweets2 = y.readlines()







    #sort function
    records_list1=read_tweets(tweets1)
    records_list2=read_tweets(tweets2)
    merged_records_list=merge_tweets(records_list1,records_list2)
    write_tweets(merged_records_list)




#we are stating that our program runs the main function
if __name__ == '__main__':
    main()