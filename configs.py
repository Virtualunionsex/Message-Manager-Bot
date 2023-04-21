# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "16246834"))
    API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5851945481:AAHyxkGMsxi0bOipQSJmcZTHv6tbabFu_UU")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1AZWarzQBu6rgosBS-50MiWe1QCrvYC668bzf1Mxlm_fEl9-eQ6b1KK38MR2fNwF_KsMEz4OMPGfpz5KR1uZdrpNoWaD6e5gylAiVQdA7k2Zc1Zi_UOOrh5i10I6wgYT4O6eRuoadqmTp4Li46GLljJSQeV711LCKFd-VJ4_YTU0rOo4XWv1LMUwiZ0wdtITefTLaSXwiicna5ShxeB9Tqpl50_QnrpVRtFzWcvQdZ71E6DADITSctqjW5j2mPEl45aDJs4IfTGUwy5RXAXe8IKV2id1yu2bsrE1C8Yao17rVgpep0k9jz3cW9FyeyqUfPA2PBblFr6Ncf1rN-UUQs5fQuuY4jFA=")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Luffy:Malik10_@cluster0.f0cpndf.mongodb.net/?retryWrites=true&w=majority")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", " Hancock_robot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001729142523"))

    ASK_FOR_BLOCKED_WORDS_LIST = os.environ.get("ASK_FOR_BLOCKED_WORDS_LIST",
                                                "Reply to this message with a list of Blocked Words. If those in Message I will not Forward them!\n\nExample:\nhello\nhacker\ncracker\njoin\nabuse heroku\njoin my channel\nchutiyappa")
    ASK_FOR_BLOCKED_EXT_LIST = os.environ.get("ASK_FOR_BLOCKED_EXT_LIST",
                                              "Reply to this message with a list of Blocked Extensions. If any file with that extension I will not forward that file!\n\nExample:\nzip\nmkv\ntorrent\ntxt\npy\ncap\nmp4\nmp3\nrar\n\nExtensions should be in lower case!")
    START_TEXT = """
Hancock Robot adalah bot paling lengkap untuk membantu anda mengelola grup anda dengan mudah dan aman!

❓ APA PERINTAHNYA? ❓ 
Tekan /help dan /mhelp untuk melihat semua perintah dan cara kerjanya!
"""
    ABOUT_CUSTOM_FILTERS_TEXT = """
Custom Filters is for deleting only separate type Media Messages or Only Text Messages.
Like you can set only delete `photo` or `video` or `document` or `audio` or `text` ...

If Need More Help Ask in [Support Group](https://t.me/virtual_executive)!
"""
