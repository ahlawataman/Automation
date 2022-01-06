from json.decoder import JSONDecodeError
import os
import json

# get all json files from current directory
files = os.listdir(".")
json_files = [file for file in files if file.endswith("json")]
processed = 0

# get a file reference to write data to (summary.csv) and write header
data_file = open("./summary.csv", "w")
data_file.write("Username, Posts, Followers, Following\n")

for file in json_files:
    # open the json file and load the content into a dict
    with open(file, "r") as json_file:
        try:
            content = json.loads(json_file.read())
            user_content = content['graphql']['user']
            username = user_content['username']
            posts = user_content['edge_owner_to_timeline_media']['count']
            followers = user_content['edge_followed_by']['count']
            following = user_content['edge_follow']['count']
            # print(f"User {username}, {posts}, {followers}, {following}\n"

            # write data to file
            data_file.write(f"{username}, {posts}, {followers}, {following}\n")
            processed += 1

        except json.decoder.JSONDecodeError as err:
            print(f"Could not load json from {file}... {err}")

print(f"Processed {processed} of {len(json_files)}")
data_file.close()