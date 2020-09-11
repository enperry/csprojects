def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    tempscores = scores
    tempscores.sort(reverse = True)
    return tempscores[:3]

