# Regression and Classification

| Key              | Value                                                                                                                                                                                                                                                                                                |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Course Codes** | BBT 4106, BCM 3104, and BFS 4102                                                                                                                                                                                                                                                                     |
| **Course Names** | BBT 4106: Business Intelligence I (Week 10-12 of 13),<br/>BCM 3104: Business Intelligence and Data Analytics (Week 10-12 of 13) and<br/>BFS 4102: Advanced Business Data Analytics (Week 4-6 of 13)                                                                                                  |
| **Semester**     | January to April 2026                                                                                                                                                                                                                                                                                |
| **Lecturer**     | Allan Omondi                                                                                                                                                                                                                                                                                         |
| **Contact**      | aomondi@strathmore.edu                                                                                                                                                                                                                                                                               |
| **Note**         | The lecture contains both theory and practice.<br/>This notebook forms part of the practice.<br/>It is intended for educational purpose only.<br/>Recommended citation: [BibTex](https://raw.githubusercontent.com/course-files/RegressionAndClassification/refs/heads/main/RecommendedCitation.bib) |

## 📦 Project Structure

```text
.
├── 0_helloKenya.ipynb
├── 1a_decision_tree.ipynb
├── 1b_decision_tree.ipynb
├── 2_naive_bayes.ipynb
├── 3_knn.ipynb
├── 4_svm.ipynb
├── 5_random_forest.ipynb
├── LICENSE
├── README.md
├── RecommendedCitation.bib
├── api.py
├── api_consumer.py
├── assets
│   └── images
│       ├── activate_venv_pycharm.png
│       └── activate_venv_vscode.png
├── data
│   ├── DataCoSupplyChainDataset.csv
│   ├── DataCoSupplyChainDataset_description.csv
│   ├── DataCoSupplyChainDataset_new_data.csv
│   ├── DataCoSupplyChainDataset_predicted_data.csv
│   ├── DataCoSupplyChainDataset_predicted_with_prob.csv
│   ├── SuperStoreSales.csv
│   ├── SuperStoreSales.xlsx
│   ├── SuperStoreSales_new_data.csv
│   ├── SuperStoreSales_predicted.csv
│   ├── customer_data_with_clusters.csv
│   ├── online_shoppers_intention.csv
│   ├── online_shoppers_intention_new_data.csv
│   ├── online_shoppers_intention_predicted_data.csv
│   ├── online_shoppers_intention_predicted_data_rf.csv
│   ├── online_shoppers_intention_predicted_data_svc.csv
│   ├── paper2_dataset.csv
│   ├── siwaka_dishes_orderstatus.csv
│   ├── siwaka_dishes_view_profit_per_product.csv
│   ├── siwaka_dishes_view_profit_per_product_new_data.csv
│   ├── siwaka_dishes_view_profit_per_product_predicted_data.csv
│   ├── subscription_churn.csv
│   ├── subscription_churn_new_data.csv
│   └── subscription_churn_predicted_data.csv
├── frontend_tests
│   ├── api_test_DT_classifier.html
│   └── api_test_DT_regressor.html
├── lab_submission
│   └── CAT2_P2_StudentID_Name.ipynb
├── main.py
├── model
│   ├── decisiontree_classifier_baseline.pkl
│   ├── decisiontree_regressor_optimum.pkl
│   ├── knn_classifier_optimum.pkl
│   ├── label_encoders_1b.pkl
│   ├── label_encoders_2.pkl
│   ├── label_encoders_4.pkl
│   ├── label_encoders_5.pkl
│   ├── naive_Bayes_classifier_optimum.pkl
│   ├── onehot_encoder_3.pkl
│   ├── random_forest_classifier_optimum.pkl
│   ├── scaler_4.pkl
│   ├── scaler_5.pkl
│   └── support_vector_classifier_optimum.pkl
├── requirements.txt
└── setup_instructions.md

7 directories, 56 files
```

## Setup Instructions

- [Setup Instructions](setup_instructions.md)

## Lab Manual

Refer to the files below for more details:

1. [0_a_helloKenya.py](0_a_helloKenya.py) and
[0_b_helloKenya.ipynb](0_b_helloKenya.ipynb): to confirm that the required
libraries to run a Jupyter notebook locally have been installed in your Python
virtual environment.
2. [1a_decision_tree.ipynb](1a_decision_tree.ipynb): A decision tree regressor.

## Lab Submission Instructions

- [Lab Submission Instructions](lab_submission_instructions.md)
