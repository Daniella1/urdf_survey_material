<p align="center">
    <img alt="ViewCount" src="https://views.whatilearened.today/views/github/Daniella1/urdf_survey_material.svg">
    <br>
    Counting since 20-10-2023
</p>

# Survey materials of "Understanding URDF: A Survey Based on User Experience"
---------------------------------

This package includes the survey materials of "Understanding URDF: A Survey Based on User Experience". The full paper can be found at [arXiv](https://arxiv.org/abs/2302.13442) or on [IEEE]([https://arxiv.org/abs/2308.00514](https://ieeexplore.ieee.org/document/10260660)).

This repository includes:

1. **survey_questions.pdf**: PDF showing the text used for the survey questions, that was set up using SurveyXact.

2. **recruitment_material.pdf**: PDF with the recruitment text used, links some of the posts for recruitment, and descriptions of how and where we have recruited people.

3. **responses**:
    - _all_responses.pdf_: PDF containing the answers from all the participants (both partially and fully completed). Personal and company names/information is removed from the data.
    
    - _completed_responses_frequency_overview.pdf_: PDF containing the frequency of the responses (from the participants that completed the survey).
    
    - _completed_participants_overview_analysis.xlsx_: Excel sheet with all the completed responses (open-ended answers included), that can be used for further analysis of the results. The tabs contain our analysis of the results that were used in the survey article. The overall results from the survey can be found in the first tab named 'raw data'.
    
    - sX_question_name.xlsx_: responses to questions with possibility of open-ended answers. The X indicates the question number, followed by the question name. Personal and company information are removed from the data.
    
    - _challenges_future_predictions_: contains the data on the challenges participants have faced, and their predictions for the future of URDF. The folder contains a Python script, 'analysis.py', for extracting data from 'challenges_future_predictions.csv', and an excel sheet, 'df_challenges_predictions.xlsx', with the analysis and plotting of the data.
    
    - _challenges_ratings_: contains the data on the challenges participants have faced and their rating on the difficulty of creating/modifying URDFs. The folder contains a Python script, 'analysis.py', for extracting data from 'challenges_ratings.csv', and an excel sheet, 'df_challenges_ratings.xlsx', with the analysis and plotting of the data.


## IEEE CASE Paper and Citation Info

Check out the published paper on [IEEE]([https://arxiv.org/abs/2308.00514](https://ieeexplore.ieee.org/document/10260660)).

If the dataset helped you in your research, please cite

```
@INPROCEEDINGS{10260660,
  author={Tola, Daniella and Corke, Peter},
  booktitle={2023 IEEE 19th International Conference on Automation Science and Engineering (CASE)}, 
  title={Understanding URDF: A Survey Based on User Experience}, 
  year={2023},
  pages={1-7},
  doi={10.1109/CASE56687.2023.10260660}
}
```
