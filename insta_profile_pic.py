import instaloader
mod = instaloader.Instaloader()
a = input("Enter the User Name --> ")
mod.download_profile(a,profile_pic_only = True)