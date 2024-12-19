**TASK1**

text1: OS data are not yet mature. Long-term follow-up is planned¹,⁴
IDFS in patients with HR+, HER2-, node-positive EBC at high risk of recurrence with Ki-67 ≥20% (n=2,003)
text2: OS data are not yet mature. Long-term follow-up is planned¹,⁴
IDFS in patients with HR+, HER2-, node-positive EBC at high risk of recurrence with Ki-67 ≥20% (n=2,003)
query: OS data are not yet mature. Long-term follow-up is planned¹,⁴
IDFS in patients with HR+, HER2-, node-positive EBC at high risk of recurrence with Ki-67 ≥20% (n=2,003)

**TASK2**

template = [Free text area for salutation and HCP preferred name for sales representative use. 
Use this free text area as an opportunity to let the HCP know why he/she is receiving the email. 
Do not include both product and disease state information. 
Free text is limited to 50 words. 
Drop down text selection may also be used.]

input_text = Dear Dr. Jones, it was good to talk to you last week. 
I would like to set up some time to further discuss some information about the new drug that we have. 
Please call or email me with some available times for us to talk. 
Thank you.

**TASK3**

text1 = A major breakthrough in HR+HER2-EBC
edit_instruction = Natalie Wolfe on behalf of Judith Grimes Must revise, and regulatory must review.
"Major breakthrough" is a claim and not appropriate for a subject line.
Must include the concept of high risk with disease state mention. 
target1 = A major breakthrough in HR+HER2-EBC

text2 = """ References:
1. Verzenio [package insert]. Indianapolis, IN: Eli Lilly and Company.
2. Mayer EL, Dueck AC, Martin M, et al. Palbociclib with adjuvant endocrine therapy in early breast cancer (PALLAS): interim analysis of a multicentre, open-label, randomised, phase 3 study. Lancet Oncol. 2021;22(2):212-222. doi:10.1016/S1470-2045(20)30757-9.
3. A trial to evaluate efficacy and safety of ribociclib with endocrine therapy as adjuvant treatment in patients with HR+/HER2- early breast cancer (NATALEE). https://clinicaltrials.gov/ct2/show/NCT03701334. Accessed February 12, 2021.
4. Johnston SRD, Harbeck N, Hegg R, et al; monarchE Committee Members and Investigators. Abemaciclib combined with endocrine therapy for the adjuvant treatment of HR+, HER2-, node-positive, high-risk, early breast cancer (monarchE). J Clin Oncol. 2020;38(34):3987-3998. doi:10.1200/JCO.20.02514.
"""
add_instruction = """ Melissa Ossanna
Assuming that the references will be listed in the fragment that is inserted? Must add Penelope-b reference: J Clin Oncol. 2021 May 10;39(14):1518-1530.
"""

text3 = """ Have you heard about the landmark monarchE trial """
delete_instruction = """ Natalie Wolfe on behalf of Judith Grimes
Must delete """
target3 = "landmark"



