import instaloader

def profile():
    obj = instaloader.Instaloader()
    username = input("Enter a username: ")
    obj.download_profile(username, profile_pic_only=True)
    return

profile()