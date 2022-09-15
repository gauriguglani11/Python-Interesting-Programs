# uploading a picture
from instabot import Bot

#enter your username and password
bot.login(password="###", username="###")

#uploading photo
bot.upload_photo("DPcv.JPG", caption="Python TEST")

# following a person
bot.follow("sundarpichai")

# sending a message on insta
text = "Hello, I am a huge fan"
user_ids = ["sundarpichai", "gauri_d_guglani"]
bot.send_messages(text, user_ids)

# commenting on post
media_id = "https://www.instagram.com/reel/Cideod3Dolf/?utm_source=ig_web_copy_link"
comment_text = "Just beautiful"
bot.comment(media_id, comment_text)

# bot.get_user_following("clicks_by_gg")
my_following = bot.get_user_following("clicks_by_gg")
for following in my_following:
    print(bot.get_user_info(following))
