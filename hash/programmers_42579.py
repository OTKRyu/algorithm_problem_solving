def solution(genres, plays):
    genre_cnts = {}
    genre_indexs = {}
    for i in range(len(genres)):
        if genre_cnts.get(genres[i]):
            genre_cnts[genres[i]] += plays[i]
            genre_indexs[genres[i]].append((i,plays[i]))
        else:
            genre_cnts[genres[i]] = plays[i]
            genre_indexs[genres[i]] = [(i,plays[i])]
    items = list(genre_cnts.items())
    items.sort(key=lambda x:-x[1])
    answer = []
    for item in items:
        genre_indexs[item[0]].sort(key=lambda x:-x[1])
        if len(genre_indexs[item[0]]) >= 2:
            answer.append(genre_indexs[item[0]][0][0])
            answer.append(genre_indexs[item[0]][1][0])
        else:
            answer.append(genre_indexs[item[0]][0][0])
    return answer