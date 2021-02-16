import praw

user1 = praw.Reddit(client_id="Lmq7Hkt7L6giGg",
                    client_secret="NL9B6JA08bTE6Pbpf91pDBc7L3Ak1Q",
                    username="",
                    password="",
                    user_agent="Account Transfer Program v1 by Rae_Kendell99")

user2 = praw.Reddit(client_id="g9ugkB5qa_l9_w",
                    client_secret="nl1hZHTioUex3cjzQWspfLLTSMTiiA",
                    username="",
                    password="",
                    user_agent="Account Transfer Program v1 by Randawgy")

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

