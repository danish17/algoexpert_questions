def minimumWaitingTime(queries):
    queries.sort()
    wt, mwt = 0, 0
    for query in queries:
        mwt += wt
        wt = wt + query
    return mwt

minimumWaitingTime([3,2,1,2,6])