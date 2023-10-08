def countvotes(votes):
    candidate_count = {}
    for vote in votes:
        if vote in candidate_count:
            candidate_count[vote] += 1
        else:
            candidate_count[vote] = 1
    sorted_candidates = sorted(candidate_count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_candidates[0][0]
votes={"John","Johnny","Jackie","Johnny","John","Jackie","Jamie","Jamie","John","Johnny","Jamie","Johnny","John"}
print(countvotes(votes))
