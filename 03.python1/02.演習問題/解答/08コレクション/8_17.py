# 科目名と得点を連想配列に格納し表示

# 連想配列を作成し配列に格納
subjects_score_array = []
subjects_score_array.append({"国語" : 75, "算数" : 80})
subjects_score_array.append({"国語" : 70, "数学" : 80})
subjects_score_array.append({"国語": 75, "数学": 80, "理科": 65, "社会": 90, "英語": 70})

for subjects_score in subjects_score_array:
    print(subjects_score)
