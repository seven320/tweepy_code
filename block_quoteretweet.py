#encoding:utf-8
#引用リツイートしたアカウントをブロックするプログラム
#中断！！！　引用リツイートした人のidが辿れなくなってるのでややこしいことになる




import certifi
import tweepy

#親ディレクトリにあるアカウント情報へのパス
import sys,os
pardir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)

#account情報をaccount.pyからロード
from account import account #load account
auth=account.Initialize()
api = tweepy.API(auth)
twitter_id=account.id()


# a=api.get_user("yosyuaomenww")
# print(a)
#
me=api.me()
me_id=me.id
print("今のID{0}".format(me_id))

# obj_rts=api.retweets_of_me(count=10)
# # print(obj_rts)
# for obj_rt in obj_rts:
#     print("text:{0}".format(obj_rt.text))
    # print(obj_rt.is_quote_status)
    # print(obj_rt.user)


for status in tweepy.Cursor(api.user_timeline).items():
    print(status.is_quote_status)
    print(status.favorite_count)
    if status.is_quote_status==True:
        print(status.text)
