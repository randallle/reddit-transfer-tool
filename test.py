import praw

numPosts = 0
display = ""

for saved in user1.user.me().saved(limit=None):

    submission = user2.submission(id=str(saved))

    try:
        display = str(numPosts+1) + ") " + str(saved)
        submission.save()
    except:
        print("There was an error saving", str(saved), "...")
        display += " ***ERROR***"

    print(display)
    numPosts += 1

print("\n", numPosts, "saved posts from", user1.user.me(), "have been transferred to", user2.user.me())

