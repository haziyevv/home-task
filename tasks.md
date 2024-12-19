In this document some test cases are given for each task.



### First Task

> In this task `first_text` and `second_text` should be given as input to the `/task1` endpoint. If there is any difference it will return those differences in this format:

```json
{
  "message": "string",
   "differences": [
        {
            "first_text": "string",
            "second_text": "string"
        },
        {
            "first_text": "string",
            "second_text": "string"
        },
    ]
}
```

`first_text`: Important Safety Information\n\nSevere diarrhea associated with dehydration and associated infection\noccurred in patients treated with Verzenio. Across 4 clinical trials in 3691\npatients, diarrhea occurred in 81% to 90% of patients who received\nVerzenio. Grade 3 diarrhea occurred in 8% to 20% of patients receiving\nVerzenio. Most patients experienced diarrhea during the first month of\nVerzenio treatment. The median time to onset of the first diarrhea event\nranged from 6 to 8 days, and the median duration of Grade 2 and Grade\n3 diarrhea ranged from 6 to 11 days and 5 to 8 days, respectively. Across\ntrials, 19% to 26% of patients with diarrhea required a Verzenio dose\ninterruption and 13% to 23% required a dose reduction.\n\nInstruct patients to start antidiarrheal therapy such as loperamide at the\nfirst sign of loose stools, increase oral fluids, and notify their healthcare\nprovider for further instructions and appropriate follow-up. For Grade 3 or\n4 diarrhea, or diarrhea that requires hospitalization, discontinue Verzenio\nuntil toxicity resolves to s Grade 1, and then resume Verzenio at the next\nlower dose.\n\nNeutropenia, including febrile neutropenia and fatal neutropenic\nsepsis, occurred in patients treated with Verzenio. Across 4 clinical trials\nin 3691 patients, neutropenia occurred in 37% to 46% of patients\nreceiving Verzenio. A Grade =3 decrease in neutrophil count (based on\nlaboratory findings) occurred in 19% to 32% of patients receiving\nVerzenio. Across trials, the median time to first episode of Grade =3\nneutropenia ranged from 29 to 33 days, and the median duration of\nGrade =3 neutropenia ranged from 11 to 16 days.\n\nFebrile neutropenia has been reported in <1% of patients exposed to\nVerzenio across trials. Two deaths due to neutropenic sepsis were\nobserved in MONARCH 2. Inform patients to promptly report any episodes\nof fever to their healthcare provider.\n\nMonitor complete blood counts prior to the start of Verzenio therapy,\nevery 2 weeks for the first 2 months, monthly for the next 2 months, and\nas Clinically indicated. Dose interruption, dose reduction, or delay in\nstarting treatment cycles is recommended for patients who develop\nGrade 3 or 4 neutropenia.\n\nSevere, life-threatening, or fatal interstitial lung disease (ILD) or\npneumonitis can occur in patients treated with Verzenio and other\nCDK4/6 inhibitors. In Verzenio-treated patients in early breast cancer\n(EBC) (monarchE), 3% of patients experienced ILD or pneumonitis of any\ngrade: 0.4% were Grade 3 or 4 and there was one fatality (0.1%). In\nVerzenio-treated patients in metastatic breast cancer (MBC) (MONARCH\n1, MONARCH 2, MONARCH 3), 3.3% of Verzenio-treated patients had ILD\nor pneumonitis of any grade: 0.6% had Grade 3 or 4, and 0.4% had fatal\noutcomes. Additional cases of ILD or pneumonitis have been observed in\nthe post-marketing setting, with fatalities reported.\n\nMonitor patients for pulmonary symptoms indicative of ILD or\npneumonitis. Symptoms may include hypoxia, cough, dyspnea, or\ninterstitial infiltrates on radiologic exams. Infectious, neoplastic, and\nother causes for such symptoms should be excluded by means of\nappropriate investigations.

`second_text`: Important Safety Information\n\nSevere diarrhea associated with dehydration and associated infection\noccurred in patients treated with Verzenio. Across 4 clinical trials in 3691\npatients, diarrhea occurred in 81% to 90% of patients who received\nVerzenio. Grade 3 diarrhea occurred in 8% to 20% of patients receiving\nVerzenio. Most patients experienced diarrhea during the first month of\nVerzenio treatment. The median time to onset of the first diarrhea event\nranged from 6 to 8 days, and the median duration of Grade 2 and Grade\n3 diarrhea ranged from 6 to 11 days and 5 to 8 days, respectively. Across\ntrials, 19% to 26% of patients with diarrhea required a Verzenio dose\ninterruption and 13% to 23% required a dose reduction.\n\nInstruct patients to start antidiarrheal therapy such as loperamide at the\nfirst sign of loose stools, increase oral fluids, and notify their healthcare\nprovider for further instructions and appropriate follow-up. For Grade 3 or\n4 diarrhea, or diarrhea that requires hospitalization, discontinue Verzenio\nuntil toxicity resolves to = Grade 1, and then resume Verzenio at the next\nlower dose.\n\nNeutropenia, including febrile neutropenia and fatal neutropenic\nsepsis, occurred in patients treated with Verzenio. Across 4 clinical trials\nin 3691 patients, neutropenia occurred in 37% to 46% of patients\nreceiving Verzenio. A Grade =3 decrease in neutrophil count (based on\nlaboratory findings) occurred in 19% to 32% of patients receiving\nVerzenio. Across trials, the median time to first episode of Grade =3\nneutropenia ranged from 29 to 33 days, and the median duration of\nGrade =3 neutropenia ranged from 11 to 16 days.\n\nFebrile neutropenia has been reported in <1% of patients exposed to\nVerzenio across trials. Two deaths due to neutropenic sepsis were\nobserved in MONARCH 2. Inform patients to promptly report any episodes\nof fever to their healthcare provider.\n\nMonitor complete blood counts prior to the start of Verzenio therapy,\nevery 2 weeks for the first 2 months, monthly for the next 2 months, and\nas Clinically indicated. Dose interruption, dose reduction, or delay in\nstarting treatment cycles is recommended for patients who develop\nGrade 3 or 4 neutropenia.\n\nSevere, life-threatening, or fatal interstitial lung disease (ILD) or\npneumonitis can occur in patients treated with Verzenio and other\nCDK4/6 inhibitors. In Verzenio-treated patients in early breast cancer\n(EBC) (monarchE), 3% of patients experienced ILD or pneumonitis of any\ngrade: 0.4% were Grade 3 or 4 and there was one fatality (0.1%). In\nVerzenio-treated patients in metastatic breast cancer (MBC) (MONARCH\n1, MONARCH 2, MONARCH 3), 3.3% of Verzenio-treated patients had ILD\nor pneumonitis of any grade: 0.6% had Grade 3 or 4, and 0.4% had fatal\noutcomes. Additional cases of ILD or pneumonitis have been observed in\nthe post-marketing setting, with fatalities reported.\n\nMonitor patients for pulmonary symptoms indicative of ILD or\npneumonitis. Symptoms may include hypoxia, cough, dyspnea, or\ninterstitial infiltrates on radiologic exams. Infectious, neoplastic, and\nother causes for such symptoms should be excluded by means of\nappropriate investigations.



### **Second Task**

> In this task template and input_text should be given as input to /task2 endpoint. It will check if the input_text follows the structure in the given template and return a result in this format:

```json
{
    "result": bool,
    "explanation": "string"
}
```

`template` = [Free text area for salutation and HCP preferred name for sales representative use. Use this free text area as an opportunity to let the HCP know why he/she is receiving the email. Do not include both product and disease state information. Free text is limited to 50 words. Drop down text selection may also be used.]

`input_text` = Dear Dr. Jones, it was good to talk to you last week. I would like to set up some time to further discuss some information about the new drug that we have. Please call or email me with some available times for us to talk. Thank you.



### Third Paragraph

> In this task, a text and an instruction will be input to the /task3 endpoint and it will add, edit or delete some part of the given text according to the instruction and return the updated_text:

```json
{
    "updated_text": "string"
}
```

**Below tests for edit, add and delete cases are given:**

`text1` = A major breakthrough in HR+HER2-EBC
`edit_instruction` = Natalie Wolfe on behalf of Judith Grimes Must revise, and regulatory must review. \"Major breakthrough\" is a claim and not appropriate for a subject line. Must include the concept of high risk with disease state mention.
target1 = A major breakthrough in HR+HER2-EBC



`text2` = References: 1. Verzenio [package insert]. Indianapolis, IN: Eli Lilly and Company. 2. Mayer EL, Dueck AC, Martin M, et al. Palbociclib with adjuvant endocrine therapy in early breast cancer (PALLAS): interim analysis of a multicentre, open-label, randomised, phase 3 study. Lancet Oncol. 2021;22(2):212-222. doi:10.1016/S1470-2045(20)30757-9. 3. A trial to evaluate efficacy and safety of ribociclib with endocrine therapy as adjuvant treatment in patients with HR+/HER2- early breast cancer (NATALEE). https://clinicaltrials.gov/ct2/show/NCT03701334. Accessed February 12, 2021. 4. Johnston SRD, Harbeck N, Hegg R, et al; monarchE Committee Members and Investigators. Abemaciclib combined with endocrine therapy for the adjuvant treatment of HR+, HER2-, node-positive, high-risk, early breast cancer (monarchE). J Clin Oncol. 2020;38(34):3987-3998. doi:10.1200/JCO.20.02514.
`add_instruction` = Melissa Ossanna Assuming that the references will be listed in the fragment that is inserted? Must add Penelope-b reference: J Clin Oncol. 2021 May 10;39(14):1518-1530.



`text3` = Have you heard about the landmark monarchE trial
`delete_instruction` = Natalie Wolfe on behalf of Judith Grimes Must delete
`target3` = landmark



