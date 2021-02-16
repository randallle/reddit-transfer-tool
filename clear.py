import praw

user2 = praw.Reddit(client_id="g9ugkB5qa_l9_w",
                    client_secret="nl1hZHTioUex3cjzQWspfLLTSMTiiA",
                    username="Randawgy",
                    password="",
                    user_agent="Account Transfer Program v1 by Randawgy")

numPosts = 0

for saved in user2.user.me().saved(limit=None):
    submission = user2.submission(id=str(saved))
    print(str(numPosts+1) + ") " + str(saved))
    submission.unsave()

    numPosts += 1

print("\n", numPosts, " posts from", user2.user.me(), "have been unsaved")