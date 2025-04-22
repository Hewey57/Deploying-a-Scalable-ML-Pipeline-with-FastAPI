# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Rick Hewitt on 4/20/2025. The selected model is a RandomForestClassifier machine learning model.The model pulls data from the US Census file contatined within the project.

## Intended Use
The intended use of this modelt is to determine if a person makes more or less than $50,000 per year. The following categories are used to train the model and predict the individuals income.
Data: age, workclass, fnlgt, education, education-num,marital-status, occupation, relationship, race, sex

## Training Data
This project uses training data stored in census.csv, located in the data directory. The dataset is a reduced version of the U.S. Census data from 1994. For full documentation and access to the original source, visit the UCI Census Income Dataset.

Each row in the dataset contains information about an individual, including both categorical and numerical attributes such as:

Age: Individual's age in years

Workclass: Type of employment 

fnlgt: Identifier from the Census 

Education / Education-num: Educational background as text and as a numerical score

Marital-status / Relationship: Marital and household status

Occupation / Race / Sex: Job title, ethnicity, and gender

Capital-gain / Capital-loss: Financial gains or losses from investments

Hours-per-week: Weekly work hours

Native-country: Country of origin

Salary: Target variable indicating whether income is above or below $50K


## Evaluation Data
The data in the model was split into a training dataset and a test dataset. The test dataset split was 20% of the overall dataset, while 80% of the dataset was used for training the model.

## Metrics
Precision: 0.7222
Recall: 0.6194
F1: 0.6669

## Ethical Considerations

The dataset raises a concerns regarding representativeness and fairness surrounding race. About 85% of records are from white individuals. This lack of diversity could distort predictions in more racially mixed communities. This show be considered in the overall training of the model. 


## Caveats and Recommendations
Sampling Bias 
    The data likely reflects a majority-white demographic and may not generalize well to all U.S. regions. It is recommended that the dataset be expanded to include additional race demographics to predict accurately. 
