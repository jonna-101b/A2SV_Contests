if __name__ == "__main__":
    n = int(input().strip())
    r = [ int(num) for num in input().strip().split() ]



# A. Eskalate Finalists
# time limit per test2 s.
# memory limit per test256 MB
# This year, A2SV is inviting the top 25 applicants from the Eskalate web platform's screening phase for a final onsite interview. Not everyone who is eligible can afford to travel or commit to the schedule. Initially, the top 25 applicants are invited. Each eligible applicant must either accept or decline the invitation. Whenever an applicant declines, the highest-ranked applicant not yet invited is invited to take their place. This continues until exactly 25 applicants have accepted invitations.

# After the screening phase completes, you know K
#  of the accepted finalists, as well as their qualifying ranks (which start at 1
# , with no ties). Determine the minimum possible number of applicants that declined the invitation to interview.

# Input
# The first line of input contains K
#  (1≤K≤25
# ), the number of onsite finalists you know. The second line of input contains r1,r2,…,rK
#  (1≤ri≤106
# ), the qualifying ranks of the finalists you know. All these ranks are distinct.