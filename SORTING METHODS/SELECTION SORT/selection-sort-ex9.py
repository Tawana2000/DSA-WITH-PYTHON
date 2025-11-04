#Job Applicant Ranking System
"""
You are building a system for a tech company that needs to rank applicants for inteviews.
Each applicant record is:
[name, degree_level, experience_years, test_score, interview_score, application_time]

Sorting Rules (From highest to lowest)
1. Degree level (highest degree first):
       -PhD > Master's > Bachelors > Associate > High School
2. Experience (more years first)
3. Test Score (higher first)
4. Interview Score (higher first)
5. Application Time (earlier first)
6. If everything else is the same -> Sort alphabetically by name (A -> Z)
"""


class Selection_Sort:

    def job_application_ranking(self, applicants):

        for i in range(len(applicants)):
            rank = i

            for j in range(i + 1, len(applicants)):
                if applicants[j][1] > applicants[rank][1]:
                    rank = j
                elif applicants[j][1] == applicants[rank][1] and applicants[j][2] > applicants[rank][2]:
                    rank = j
                elif applicants[j][1] == applicants[rank][1] and applicants[j][2] == applicants[rank][2] and applicants[j][3] > applicants[rank][3]:
                    rank = j
                elif applicants[j][1] == applicants[rank][1] and applicants[j][2] == applicants[rank][2] and applicants[j][3] == applicants[rank][3] and applicants[j][4] > applicants[rank][4]:
                    rank = j
                elif applicants[j][1] == applicants[rank][1] and applicants[j][2] == applicants[rank][2] and applicants[j][3] == applicants[rank][3] and applicants[j][4] == applicants[rank][4] and applicants[j][5] < applicants[rank][5]:
                    rank = j

            applicants[i], applicants[rank] = applicants[rank], applicants[i]

        for name, degree, exp, test, interview, date_applied in applicants:
            formatted_time = f"{date_applied//100:02}:{date_applied%100:02}"  
            print(f"Name: {name} | Degree: {degree} | Exp: {exp} | Test: {test} | Interview: {interview} | Applied: {formatted_time}")

        return applicants


applicants = [
    ["Alice", "Master's", 5, 88, 92, 915],
    ["Bob", "Bachelor's", 6, 90, 88, 930],
    ["Charlie", "PhD", 3, 85, 95, 905],
    ["Diana", "PhD", 4, 85, 95, 910],
    ["Ethan", "Bachelor's", 6, 90, 88, 920],
    ["Fatima", "Master's", 5, 88, 92, 910],
    ["George", "Associate", 8, 80, 85, 900],
    ["Hannah", "PhD", 3, 85, 95, 900]
]

SS = Selection_Sort()
SS.job_application_ranking(applicants)
