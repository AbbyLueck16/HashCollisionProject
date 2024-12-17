#!/usr/bin/python3
import hashlib
greeting = ["Hello","Hi", "Dear", "Greetings", "Hello there"]
punct1 =  [","," ", "\n", "!", "-"]
punct2 = ["."," ","!","\n",":)", "!!"]
punct3 = ["."," ",",","!","!!","\n"]
punct4 = ["."," ", ",","!","!!","\n"]
last = ["Sincerely","Take care","Kind regards","Best wishes"]

good = """
%s Bob%s
We should go out next week and meet for coffee%s
Let me know your thoughts%s
I hope you're having a good day%s
%s,
Alice"""
good_dict= {}
for mod1 in greeting:
        for mod2 in punct1:
                for mod3 in punct2:
                        for mod4 in punct3:
                                for mod5 in punct4:
                                        for mod6 in  last:
                                                modified = good%(mod1, mod2, mod3, mod4, mod5, mod6)
                                                y = hashlib.sha256(modified.encode('utf-8')).hexdigest()[:6]
                                                good_dict[y] = modified

greeting2 = ["Hello","Hi", "Dear", "Greetings", "Hello there"]
punc1 =  [","," ", "\n", "!", "-"]
punc2 = ["."," ","!","\n",":(", "!!"]
punc3 = ["."," ",",","!","!!","\n"]
badSyn = ["bad","awful","terrible","horrific","sucky"]
punc4  = ["."," ", ",","!","!!","\n"]

bad = """
%s Bob%s
We should not go out next week and meet for coffee%s
Don't let me know your thoughts%s
I hope you're having a %s day%s
Worst,
Alice"""

bad_dict = {}
for mod1 in greeting2:
        for mod2 in punc1:
                for mod3 in punc2:
                        for mod4 in punc3:
                                for mod5 in badSyn:
                                        for mod6 in  punc4:
                                                modified = bad%(mod1, mod2, mod3, mod4, mod5, mod6)
                                                y = hashlib.sha256(modified.encode('utf-8')).hexdigest()[:6] 
                                                if(y in good_dict):
                                                    finalEvil = modified
                                                    finalGood = good_dict[y]
with open("evil.txt","w") as evil_file, open("harmless.txt","w") as harmless_file:
    evil_file.write(finalEvil)
    harmless_file.write(finalGood)
