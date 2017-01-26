## prog2parta.py
## Srivarshini Ananta
## January 23, 2015

def pq(i, s, c, pn, pa, d, n ):
    """ compute preparedness quotient given importance of event(i), hours of sleep you had last night(s), shots of espresso or other stimulants consumed(c), hours of preparation needed to excel(pn), hours you actually spent preparing(pa), difficulty of subject matter(d), level of nervousness(n)
          parameter values expects number representing values
          returned result is number representing preparedness quotient """
    result = (8 * pa * ( s + c) )/ (3 * pn * ( d + n + i ) )
    return result 

def min3(n1, n2, n3):
    """ compute minimum of three values n1 n2 and n3 """
    if (n1<=n2) and (n1<=n3):
        return n1
    if (n2<=n1) and (n2<=n3):
        return n2 
    if (n3<=n1) and (n3<=n2):
        return n3 
