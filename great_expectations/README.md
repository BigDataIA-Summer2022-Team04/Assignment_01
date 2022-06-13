# Great Expectations
Expectations are basically unit tests for your data. Creates data documentation and data quality reports from those Expectations.

# Features
* __Automated data profiling__ <br>
The library profiles your data to get basic statistics, and automatically generates a suite of Expectations based on what is observed in the data.
* __Data validation__ <br>
Expectation Suite passes or fails, and returns any unexpected values that failed a test
* __Data Docs__ <br>
Renders HTML file of Expectations in clean, human-readable documentation containing both Expectation Suites and data Validation Results
* __Diverse Datasources and Store backends__ <br>
Various datasources such Pandas dataframes, Spark dataframes, and SQL databases via SQLAlchemy.


# Overview

1. **Expectations suite json**
    * [faa_registration](/great_expectations/expectations/faa_registration_suite.json)
    * [planes_features](/great_expectations/expectations/planes_features_suite.json)
2. **Data Docs html report**
    * [faa_registration](/great_expectations/uncommitted/data_docs/local_site/expectations/faa_registration_suite.html)
    * [planes_features](/great_expectations/uncommitted/data_docs/local_site/expectations/planes_features_suite.html)

---
# Step 01: Environment Configuration

## 1.1. Install module `great_expectations`
```bash
pip install great_expectations
```
## 1.2. Verify the version
```bash
great_expectations --version
```
Output: `great_expectations, version 0.15.9`
## 03. Initialize at the base dir
```bash
great_expectations init
```
Change working dir to the newly created dir, `great_expectations`
```bash
cd great_expectations
```
## 04. Import data into repo
Copy the dataset into `great_expectations/data`
Files:
> faa_registration.csv <br> planes_features.csv


# Step 02: Connect to data
## 05. Launch cli datasource process
```bash
great_expectations datasource new
```
Input following in the prompt
> `1` - Local File<br> `1` - Pandas <br> `data` - relative path to datasets

This open a Jupyter notebook, <br>
* Change to `datasource_name` var to `spy_plane_data`
* Update `example_yaml` to ignore all non csv files
    ```python
    example_yaml = f"""
    name: {datasource_name}
    class_name: Datasource
    execution_engine:
      class_name: PandasExecutionEngine
    data_connectors:
      default_inferred_data_connector_name:
        class_name: InferredAssetFilesystemDataConnector
        base_directory: data
        default_regex:
          group_names:
            - data_asset_name
          pattern: (.*)\.csv
      default_runtime_data_connector_name:
        class_name: RuntimeDataConnector
        batch_identifiers:
          - default_identifier_name
    """
    print(example_yaml)
    ```
* Save the datasource Configuration
* Close Jupyter notebook

# Step 03: Create Expectations for faa_registration

## 3.1. Launch cli suite process
```bash
great_expectations suite new
```
Input following in the prompt
  > `3` - Automatically, using a profiler <br> `1` - Select index of file `faa_registration.csv` <br> `faa_registration_suite` - suite name

This open a Jupyter notebook, <br>
* Change to `datasource_name` var to `spy_plane_data`
* Update `exclude_column_names` to
    ```python
    exclude_column_names = [
        "N-NUMBER",
        "SERIAL NUMBER",
        "MFR MDL CODE",
        "ENG MFR MDL",
    #    "YEAR MFR",
        "TYPE REGISTRANT",
        "NAME",
        "STREET",
        "STREET2",
        "CITY",
        "STATE",
        "ZIP CODE",
        "REGION",
        "COUNTY",
        "COUNTRY",
    #    "LAST ACTION DATE",
    #    "CERT ISSUE DATE",
        "CERTIFICATION",
        "TYPE AIRCRAFT",
        "TYPE ENGINE",
        "STATUS CODE",
        "MODE S CODE",
        "FRACT OWNER",
        "AIR WORTH DATE",
        "OTHER NAMES(1)",
        "OTHER NAMES(2)",
        "OTHER NAMES(3)",
        "OTHER NAMES(4)",
        "OTHER NAMES(5)",
    #    "EXPIRATION DATE",
    #    "UNIQUE ID",
        "KIT MFR",
        "KIT MODEL",
        "MODE S CODE HEX",
        "X35",
    ]
    ```
* Run to create default expectation and analyze the result
* Modify expectation as per need
    ```bash
    great_expectations suite edit faa_registration_suite
    ```
    Input following in the prompt (! SYS ERROR, COULD NOT LOAD THE NOTEBOOK)
  > `1` - Manually, without interacting with a sample batch of data (default)

  Modified the JSON file `great_expectations/expectations/faa_registration_suite.json` and kept necessary expectations <br>
  Updated to: <br>
  `This Expectation suite currently contains 8 total Expectations across 5 columns.`

# Step 04: Validate Data
## 4.1. Create checkpoint
```bash
great_expectations checkpoint new faa_registration_checkpoint_v0.1
```
This open a Jupyter notebook, <br>
* Run all cells.
* Report in new page

# Step 05: Create Expectations for planes_features
```bash
great_expectations suite new
```
Input following in the prompt
  > `3` - Automatically, using a profiler <br> `2` - Select index of file `planes_features.csv` <br> `planes_features_suite` - suite name

This open a Jupyter notebook, <br>
* Change to `datasource_name` var to `spy_plane_data`
* Update `exclude_column_names` to
    ```python
    exclude_column_names = [
      #    "adshex",
      #    "duration1",
      #    "duration2",
      #    "duration3",
      #    "duration4",
      #    "duration5",
      #    "boxes1",
      #    "boxes2",
      #    "boxes3",
      #    "boxes4",
      #    "boxes5",
      #    "speed1",
      #    "speed2",
      #    "speed3",
      #    "speed4",
      #    "speed5",
      #    "altitude1",
      #    "altitude2",
      #    "altitude3",
      #    "altitude4",
      #    "altitude5",
      #    "steer1",
      #    "steer2",
      #    "steer3",
      #    "steer4",
      #    "steer5",
      #    "steer6",
      #    "steer7",
      #    "steer8",
          "flights",
          "squawk_1",
          "observations",
      #    "type",
    ]
    ```
* Run to create default expectation and analyze the result
* Modify expectation as per need
    ```bash
    great_expectations suite edit planes_features_suite
    ```
    Input following in the prompt (! SYS ERROR, COULD NOT LOAD THE NOTEBOOK)
  > `1` - Manually, without interacting with a sample batch of data (default)

  Modified the JSON file `great_expectations/expectations/planes_features_suite.json` and kept necessary expectations <br>
  Updated to: <br>
  `This Expectation suite currently contains 31 total Expectations across 28 columns.`

# Step 06: Validate Data
## 6.1. Create checkpoint
```bash
great_expectations checkpoint new planes_features_checkpoint_v0.1
```
This open a Jupyter notebook, <br>
* Run all cells.
* Report in new page


# Ends

