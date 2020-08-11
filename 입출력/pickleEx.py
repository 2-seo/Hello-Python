# import pickle
#
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"Lee", "나이":25, "취미":["농구", "프로그래밍", "독서"]}
# pickle.dump(profile, profile_file)
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)

with open("profile.pickle", "rb") as fw:
    data = pickle.load(fw)
    print(data)