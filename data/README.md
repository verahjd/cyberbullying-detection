# Dataset Information

## Source

- **Name:** Cyberbullying Detection Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/ziya07/cyberbullying-detection-dataset)
- **File:** cyberbullying_dataset_1000.csv
- **Size:** 1,000 rows

## Description

This dataset contains social media posts labeled as either "bullying" or "non-bullying", along with behavioral metadata.

## Columns

| Column Name    | Type   | Description                               |
| -------------- | ------ | ----------------------------------------- |
| post_id        | string | Unique post identifier                    |
| user_id        | string | User identifier                           |
| text           | string | The actual post content                   |
| label          | string | Target variable (bullying / non-bullying) |
| post_length    | int    | Number of words in post                   |
| avg_sentiment  | float  | Sentiment score (-1 to 1)                 |
| num_likes      | int    | Number of likes                           |
| num_shares     | int    | Number of shares                          |
| num_reports    | int    | Number of reports                         |
| user_posts     | int    | Total posts by user                       |
| user_friends   | int    | Number of friends                         |
| response_time  | float  | Response time in hours                    |
| toxicity_score | float  | Toxicity score (0-1)                      |

## Label Distribution

- **Bullying:** 500 samples (50%)
- **Non-bullying:** 500 samples (50%)

## Usage

Place `cyberbullying_dataset_1000.csv` in this directory to train the model.

## Citation

If you use this dataset, please cite:
Ziya07. (2024). Cyberbullying Detection Dataset. Kaggle.
