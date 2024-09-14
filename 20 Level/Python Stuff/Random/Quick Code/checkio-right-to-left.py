def left_join(phrases):  # sourcery skip: assign-if-exp, reintroduce-else, use-any

    phrases = list(phrases)

    right_in_phrases = False
    for i in phrases:
        if "right" in i:
            right_in_phrases = True

    if right_in_phrases is False:
        return ",".join(phrases)

    indexes = list(range(len(phrases)))
    for i in phrases:
        if "right" in i:
            phrases[phrases.index(i)]= i.split("right")
        del phrases[0][-1]
        for i in phrases:
            index = phrases.index(i)
#            if len(phrases[index]) > 1:
 #               phrases[index] = .join(phrases[index])




    return ""


print(left_join(("bright aright", "ok")))
