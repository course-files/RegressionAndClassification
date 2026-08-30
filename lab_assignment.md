# Lab Assignment: Applied Regression / Classification Project

Your group has been assigned one of the datasets below. Work through the complete
modeling pipeline we went through during the lab: from installation of
dependencies all the way to model persistence, applied to your assigned dataset.
Submit one Jupyter notebook (`.ipynb`) per group.

**This must be your own analysis of your assigned dataset, not the demonstration
notebook with different column names, i.e. you have to customize your analysis.**
Each dataset has its own missingness patterns, correlated features, and target
shape. Your decisions should reflect that. Refer to
[the rubric](./lab_assignment_grading_rubric.md) for what each
stage needs to earn full marks.

## Assigned Datasets

| Dataset                                                               | Group                     | Context                                                           | Target to Predict                    |
|-----------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------|--------------------------------------|
| [`real_estate_rental_price.csv`](./data/real_estate_rental_price.csv) | A                         | Monthly rental listings across Nairobi-area neighborhoods         | `monthly_rent_kes`                   |
| [`retail_daily_sales.csv`](./data/retail_daily_sales.csv)             | C                         | Daily performance of retail stores of varying format and location | `daily_sales_revenue_kes`            |
| [`marketing_campaign_roi.csv`](./data/marketing_campaign_roi.csv)     | Not assigned to any group | Digital ad campaigns across platforms and objectives              | `campaign_roi_pct` (can be negative) |
| [`farm_annual_income.csv`](./data/farm_annual_income.csv)             | D                         | Smallholder and commercial farm operations across counties        | `annual_farm_income_kes`             |
| [`student_exam_score.csv`](./data/student_exam_score.csv)             | B                         | Student study habits, background, and support factors             | `final_exam_score` (bounded 0–100)   |

**Beyond the notebook**, every group member should individually complete:
- A 2-3-minute one-on-one conversation (defense) where you will be asked
  **only one** random question related to a decision that was made in your
  group's notebook. Note that this is not necessarily only the part you
  personally coded; you are expected to understand the entire group submission
  (the whole notebook).
- A **private** peer-contribution rating of your teammates. This will adjust each
  teammate's final grade according to their group contribution.

**Logistics**:
- Groups of 5, as assigned from Business Intelligence 1.
- Use the dataset that has been assigned to your group. Do not substitute it with
  a different dataset.
