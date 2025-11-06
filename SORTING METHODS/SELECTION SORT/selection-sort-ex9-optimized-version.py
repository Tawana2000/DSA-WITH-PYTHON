# Optimized version of Ex9
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

       def job_applicantion_ranking(self, applicants):
              degree_rank{"PHD: 5", 
                         "Master's: 4", 
                         "Bachelor's: 3",
                         "Associate: 2", 
                         "High School: 1"}
              
              def is_better(a, b):
                     if degree_rank[a[1]] != degree_rank[b[1]]:
                            return degree_rank[a[1]] > degree_rank[b[1]]
                            
                     if a[2] != b[2]:
                            return a[2] > b[2]
                     
                     if a[3] != b[3]:
                            return a[3] > b[3]
                            
                     if a[4] != b[4]:
                            return a[4] > b[4]
                            
                     if a[5] != b[5]:
                            return a[5] > b[5]
