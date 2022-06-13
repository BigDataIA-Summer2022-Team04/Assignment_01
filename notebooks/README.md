# Prepare environment
1. Create a directory, `Sandbox` at home path
```bash
cd ~
mkdir Sandbox
cd Sandbox
```
2. Clone the git repo
```bash
git clone https://github.com/piyush-an/DAMG7245_Assignment_01.git
cd DAMG7245_Assignment_01
```

3. Create a python virtual environment on the working directory
```bash
python3 -m venv spyplane
```

4. Install all the packages
```bash
pip install -r requirements.txt
```

# Notebook Description

1. [data_analysis_pd.ipynb](notebooks/data_analysis_pd.ipynb)<br>
   Dataset analysis using pandas-profiling, html reports generated at [reports](notebooks/reports) with names `csv_name_pd_report.html`

2. [faa_registration_preprocessing.ipynb](notebooks/faa_registration_preprocessing.ipynb)<br>
   Pre-Processing of faa_registration to be loaded in big query, Processed file can be found [here](data/processed) with names `{file_name}_{timestamp}.csv`

# Error and Resolution
|Sl no| File      | Error | Fix |
| :---:  | :----:  | :--: | :--------:  |
|1| [data_analysis_pd.ipynb](notebooks/data_analysis_pd.ipynb)      | `URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)>`       | Update the certifi package using pip <br> `pip install certifi`
|2|    |         |