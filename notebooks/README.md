# Data Profiling

# Deliverables
Use pandas profiling on your dataset<br>
https://github.com/ydataai/pandas-profiling<br>

**Note**: If you have an image dataset create a meta data of your dataset and do profiling on that. <br>

For creating meta data, you can use: <br>
https://pypi.org/project/Pillow/2.2.1/ <br>
https://www.thepythoncode.com/article/extracting-image-metadata-in-python <br>

Published a py file which has an example of generating metadata for a dataset: <br>
https://github.com/shahparth0007/Big-Data-Systems-Intelligence-Analytics-Labs-Summer-2022/tree/main/Generate_MetaData <br>

Why Profiling: So, you know how your data looks and we are aware of all data outliers which we need to handle in great expectation <br>

# Submission: Create a folder in your GitHub repository where you have  
1. IPYNP file containing the code of your pandas profiling 
2. HTML file containing the output of your profiling 

# Accomplishments

| **Sl No** | **File Name**                       | **Desc**                                | **Link**                                                                                      |
|:---------:|:-----------------------------------:|:---------------------------------------:|:---------------------------------------------------------------------------------------------:|
| **1**     | data_analysis_pd.ipynb              | Dataset analysis using pandas-profiling | [data_analysis_pd.ipynb](/notebooks/data_analysis_pd.ipynb)                                   |
| **2**     | faa_registration.csv_pd_report.html | Pandas Report                           | [faa_registration.csv_pd_report.html](/notebooks/reports/faa_registration.csv_pd_report.html) |
| **3**     | feds.csv_pd_report.html             | Pandas Report                           | [feds.csv_pd_report.html](/notebooks/reports/feds.csv_pd_report.html)                         |
| **4**     | planes_features.csv_pd_report.html  | Pandas Report                           | [planes_features.csv_pd_report.html](/notebooks/reports/planes_features.csv_pd_report.html)   |
| **5**     | model.r                             | R model                                 | [model.r](notebooks/model.r)                                                                  |
| **6**     | model.ipynb                         | Python model (Incomplete)               | [model.ipynb](notebooks/model.ipynb)                                                          |

---

# Notebook Description

1. [data_analysis_pd.ipynb](/notebooks/data_analysis_pd.ipynb)<br>
   Dataset analysis using pandas-profiling, html reports generated at [reports](/notebooks/reports) with names `csv_name_pd_report.html`

2. [faa_registration_preprocessing.ipynb](/notebooks/faa_registration_preprocessing.ipynb)<br>
   Pre-Processing of faa_registration to be loaded in big query, Processed file can be found [here](/data/processed) with names `{file_name}_{timestamp}.csv`

# Error and Resolution
|Sl no| File      | Error | Fix |
| :---:  | :----:  | :--: | :--------:  |
|1| [data_analysis_pd.ipynb](/notebooks/data_analysis_pd.ipynb)      | `URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)>`       | Update the certifi package using pip <br> `pip install certifi`
|2|    |         |


