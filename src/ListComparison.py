from bs4 import BeautifulSoup


def extract_usernames_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        usernames = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("https://www.instagram.com/"):
                username = href.replace("https://www.instagram.com/", "").strip("/")
                usernames.add(username)
        return usernames


# paths to HTML files
followers_file = 'followers_1.html'
following_file = 'following.html'

# extract usernames
followers = extract_usernames_from_file(followers_file)
following = extract_usernames_from_file(following_file)

# calculate differences
not_following_you_back = following - followers
you_dont_follow_back = followers - following

# output
print("People you follow who don't follow you back:")
for user in sorted(not_following_you_back):
    print(f"- {user}")

print("\nPeople who follow you but you don't follow back:")
for user in sorted(you_dont_follow_back):
    print(f"- {user}")
