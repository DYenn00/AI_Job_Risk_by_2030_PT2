# AI_Job_Risk_by_2030_PT2
AI Job Risk by 2030 part 2 (public version)

Hi all, if you've stumbled upon this page welcome! 

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)  
- [Data](#data)  
- [Methodology](#methodology)   
- [Installation](#installation)  
- [Results and Insights](#results-and-insights)  
- [Limitations](#limitations)  
- [Roadmap](#roadmap)  
- [Contributing](#contributing)  
- [License](#license)

## Project Overview

The impact Artificial Intelligence will have on jobs by 2030. I used data sets from Kaggle and Pandas for data manipulation and analysis, and Matplotlib along with Seaborn for coding the visual data sets. The code snippets will also be available on my GitHub under "AI Job Risk by 2030". The goal is to help policymakers, businesses, and workers understand potential displacement risks and identify upskilling or reskilling priorities.

## Tech Stack 

This project is implemented in Python and uses the following core libraries for data work and visualization.
​
1. Kaggle datasets as the primary data source for occupations, skills, and related labor metrics.
​

2. Pandas for data cleaning, manipulation, merging datasets, and calculating automation risk metrics.
​

3. Matplotlib for creating static charts such as bar plots, line charts, and histograms of job risk by 2030.
​

4. Seaborn for more advanced and styled statistical visualizations, including distribution plots and heatmaps to explore relationships between job features and AI risk.
​

## Features

​1. Job metadata

- Includes core descriptive fields such as job title, role category, and industry, which are used to group and compare occupations by their exposure to AI.
​

2. AI impact and automation indicators
- Uses dataset fields such as AI impact or automation risk scores to quantify how strongly each role is expected to be affected by AI technologies by 2030.
​

3. Skills, education, and experience
- Incorporates features describing required skills, education level, and experience, allowing analysis of how qualification profiles relate to AI impact levels.
​

4. Compensation and job characteristics
- Analyzes variables such as salary, company size, and (where available) remote or hybrid status to see how job quality and conditions correlate with AI risk.
​

5. Aggregated risk views
- Produces derived features and summaries (for example, average automation risk by industry, education band, or skill cluster) to highlight segments that appear more or less vulnerable in the dataset

## Data


This project is designed to work with publicly available datasets, from Kaggle:

- The Raw data set will be avaible for download under 'data/raw'or you can create an account and download it here: https://www.kaggle.com/datasets/akshwint/ai-job-impact-detection-dataset

## Methodology



This project follows a structured data analysis workflow using the Kaggle “AI Job Impact Detection Dataset,” Python, and Google Colab.
​

1. Data collection and loading

- Imported the AI job impact dataset directly from Kaggle into Google Colab, either via file upload or the Kaggle API.
​

- Loaded the dataset into a Pandas DataFrame to enable efficient tabular manipulation and inspection.
​

2. Data cleaning and preparation

- Checked for missing, duplicate, or inconsistent values in key columns such as job title, industry, AI impact/risk labels, and related features.
​

- Handled missing data (for example, by dropping incomplete rows or imputing reasonable defaults) and standardized text fields (e.g., consistent casing for industries or job roles).
​

3. Exploratory data analysis (EDA)

- Used Pandas to compute descriptive statistics and group-by summaries to understand distributions of AI impact across roles, sectors, and experience levels.
​

- Generated visualizations with Matplotlib and Seaborn (bar charts, histograms, box plots, heatmaps) to explore relationships between variables such as AI impact vs. salary, industry, or required skills.
​

4. Feature exploration and transformation

- Examined categorical features (e.g., job type, industry, AI adoption level) and, where needed, encoded them into numerical form suitable for analysis or basic modeling.
​

- Created derived features or groupings (for example, aggregating jobs into broader categories or risk bands) to clarify patterns in AI impact by 2030.
​

5. AI impact analysis

- Analyzed how the dataset’s AI impact/risk indicators vary across occupations, industries, education levels, and experience ranges to identify higher-risk and lower-risk segments.
​

- Summarized these patterns with tables and plots to highlight which types of jobs appear most exposed to AI-driven changes by 2030, based on the structure and labels provided in the dataset.
​

6. Visualization and reporting

- Compiled key figures (e.g., top at-risk roles, impact distribution by sector, trend-style visualizations) using Matplotlib and Seaborn for inclusion in the final notebook and README.
​

- Documented main insights, along with caveats about data and modeling limits, to help readers interpret the AI job risk findings appropriately.
​

## Installation

No local installation is required, as the entire project runs in Google Colab.
​

To get started:

1. Open the project notebook in Google Colab.
2. ​Run the setup cell in the notebook, which installs and imports the required Python libraries (such as pandas, matplotlib, seaborn, and any Kaggle utilities used to access datasets. Don't forget to have the dataset downloaded to your drive, if you only upload it to the notebook, yo may not be able to revisit your data later).
3. Execute the remaining cells in order to load the Kaggle datasets, perform the analysis, and generate the visualizations.
​


## Results and Insights


You can find the resuts in `reports/summary_report.md`.

## Limitations

- The analysis relies on a single Kaggle dataset, so results may not generalize to all countries, industries, or future AI adoption patterns. Job impact labels and feature definitions   may not capture the real-world labor markets or policy changes by 2030. The dataset is static, while AI capabilities and economic conditions evolve over time, so the findings should be seen as illustrative scenarios rather than precise forecasts. 


## Roadmap

Planned improvements:

TBD at a later date. Stay tuned!

## Contributing

Contributions are welcome:

- Open an issue to discuss bugs, feature requests, or data suggestions.
- Submit a pull request with clear descriptions, tests (if applicable), and updated documentation.


## License

This project is licensed under the MIT License.

Happy learning! ❤️

***
