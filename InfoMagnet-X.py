#
#██╗███╗   ██╗███████╗ ██████╗ ███╗   ███╗ █████╗  ██████╗ ███╗   ██╗███████╗████████╗  ██╗  ██╗
#██║████╗  ██║██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔════╝ ████╗  ██║██╔════╝╚══██╔══╝  ╚██╗██╔╝
#██║██╔██╗ ██║█████╗  ██║   ██║██╔████╔██║███████║██║  ███╗██╔██╗ ██║█████╗     ██║█████╗╚███╔╝ 
#██║██║╚██╗██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══██║██║   ██║██║╚██╗██║██╔══╝     ██║╚════╝██╔██╗ 
#██║██║ ╚████║██║     ╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║     ██╔╝ ██╗
#╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝     ╚═╝  ╚═╝  
#               code by イスマエル・ベナリ 	         	  情報マグネットX
# 

import requests
import random

def generate_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
	"Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36",
	"Mozilla/5.0 (Android 11; Mobile; rv:86.0) Gecko/86.0 Firefox/86.0,"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.14 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.14 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.14 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    ]
    user_agent = random.choice(user_agents)
    return user_agent

def print_logo():
    logos = [
        """
		██╗███╗   ██╗███████╗ ██████╗ ███╗   ███╗ █████╗  ██████╗ ███╗   ██╗███████╗████████╗  ██╗  ██╗
		██║████╗  ██║██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔════╝ ████╗  ██║██╔════╝╚══██╔══╝  ╚██╗██╔╝
		██║██╔██╗ ██║█████╗  ██║   ██║██╔████╔██║███████║██║  ███╗██╔██╗ ██║█████╗     ██║█████╗╚███╔╝ 
		██║██║╚██╗██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══██║██║   ██║██║╚██╗██║██╔══╝     ██║╚════╝██╔██╗ 
		██║██║ ╚████║██║     ╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║     ██╔╝ ██╗
		╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝     ╚═╝  ╚═╝  
			           code by イスマエル・ベナリ 		     情報マグネットX
        """,
    ]
    logo = random.choice(logos)
    print(logo)


print_logo()

def gather_user_info():
    username = input("Please enter the username: ")

    twitter_info = gather_twitter_info(username)
    if twitter_info:
        print("User information from Twitter:")
        print_user_info(twitter_info)
        print("Close friends:")
        gather_twitter_friends(username)
        print("Checking tweets for threatening keywords:")
        threatening_keywords = ["threat", "danger", "violence", "harassment", "assault", "kill", "Mujahidden", "mujahidden", "fighting", "killing",
        "harm", "destroy", "attack", "ruin", "punish", "revenge", "intimidate", "sabotage", "menace", "blackmail", "assalt",]
        threatening_tweets = check_threatening_tweets(username, threatening_keywords)
        print("Checking for suspicious tweets:")
        suspicious_tweets = check_suspicious_tweets(username)
        print("Gathering popular tweets:")
        popular_tweets = gather_popular_tweets()

        save_results(username, twitter_info, threatening_tweets, suspicious_tweets, popular_tweets)
    else:
        print("Failed to gather user information from Twitter.")

def gather_twitter_info(username):
    url = f"https://api.twitter.com/users/{username}"
    headers = {
        "User-Agent": generate_random_user_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        user_info['email_registration_date'] = "2024-03-25"
        return user_info
    return None

def gather_twitter_friends(username):
    url = f"https://api.twitter.com/users/{username}/friends"
    headers = {
        "User-Agent": generate_random_user_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        friends = response.json()
        for friend in friends:
            print(friend.get("name"))
    else:
        print("Failed to gather close friends information from Twitter.")

def check_threatening_tweets(username, threatening_keywords):
    url = f"https://api.twitter.com/users/{username}/tweets"
    headers = {
        "User-Agent": generate_random_user_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tweets = response.json()
        threatening_tweets = []
        for tweet in tweets:
            for keyword in threatening_keywords:
                if keyword in tweet.get("content"):
                    threatening_tweets.append(tweet)
                    break
        if threatening_tweets:
            print("Threatening tweets found:")
            for tweet in threatening_tweets:
                print(f"Tweet date: {tweet.get('date')}")
                print(f"Tweet content: {tweet.get('content')}")
        else:
            print("No threatening tweets found.")
    else:
        print("Failed to gather user tweets.")

def check_suspicious_tweets(username):
    url = f"https://api.twitter.com/users/{username}/tweets"
    headers = {
        "User-Agent": generate_random_user_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tweets = response.json()
        suspicious_tweets = []
        for tweet in tweets:
            if "suspicious" in tweet.get("content"):
                suspicious_tweets.append(tweet)
        if suspicious_tweets:
            print("Suspicious tweets found:")
            for tweet in suspicious_tweets:
                print(f"Tweet date: {tweet.get('date')}")
                print(f"Tweet content: {tweet.get('content')}")
        else:
            print("No suspicious tweets found.")
    else:
        print("Failed to gather user tweets.")
def gather_popular_tweets():
    url = "https://api.twitter.com/tweets/popular"
    headers = {
        "User-Agent": generate_random_user_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        popular_tweets = response.json()
        if popular_tweets:
            print("Popular tweets gathered:")
            for tweet in popular_tweets:
                print(f"Tweet date: {tweet.get('date')}")
                print(f"Tweet content: {tweet.get('content')}")
        else:
            print("No popular tweets found.")
    else:
        print("Failed to gather popular tweets.")

def save_results(username, twitter_info, threatening_tweets, suspicious_tweets, popular_tweets):
    with open("results.txt", "w") as file:
        file.write(f"User information from Twitter:\n")
        file.write(f"Username: {username}\n")
        file.write(f"Full Name: {twitter_info.get('full_name')}\n")
        file.write(f"Email: {twitter_info.get('email')}\n")
        file.write(f"Registration Date: {twitter_info.get('email_registration_date')}\n")
        file.write(f"\n")

        file.write(f"Threatening tweets:\n")
        if threatening_tweets:
            for tweet in threatening_tweets:
                file.write(f"Tweet date: {tweet.get('date')}\n")
                file.write(f"Tweet content: {tweet.get('content')}\n")
                file.write(f"\n")
        else:
            file.write(f"No threatening tweets.\n")
        file.write(f"\n")

        file.write(f"Suspicious tweets:\n")
        if suspicious_tweets:
            for tweet in suspicious_tweets:
                file.write(f"Tweet date: {tweet.get('date')}\n")
                file.write(f"Tweet content: {tweet.get('content')}\n")
                file.write(f"\n")
        else:
            file.write(f"No suspicious tweets.\n")
        file.write(f"\n")

        file.write(f"Popular tweets:\n")
        if popular_tweets:
            for tweet in popular_tweets:
                file.write(f"Tweet date: {tweet.get('date')}\n")
                file.write(f"Tweet content: {tweet.get('content')}\n")
                file.write(f"\n")
        else:
            file.write(f"No popular tweets.\n")
        file.write(f"\n")

    print("Results saved in results.txt.")

gather_user_info()
