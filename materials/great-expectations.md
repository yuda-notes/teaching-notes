# Data Validation with Great Expectations

## Definition

- Data validation is a process of validating data to a specific rules/standards.
- This process is crucial to ensure data quality.
- Example of data validation
  - Check for missing values.
  - Check for duplicate values.
  - Verify date format.
  - Verify data type consistencies.
  - etc.

## Great Expectations

- Great Expectations (GX) is a specific python package to perform data validation pipeline.
- To install GX

  ```bash
  pip install great_expectations
  ```

### Creating Data Context

- Data Context is the primary entry point for GX that contains all configurations and methods.
  ![alt text](https://docs.greatexpectations.io/assets/images/data_context_does_for_you-df2eca32d0152ead16cccd5d3d226abb.png)
- By default, we can use GX without creating a new data context.

  ```py
  from great_expectations import get_context

  # using default data context
  context = get_context()
  ```

- But to create one, we can use this snippet code

  ```py
  from great_expectations.data_context import FileDataContext

  # Create data context in current directory
  context = FileDataContext.create(project_root_dir='./')
  ```

### Expectations

- Expectation is a verifiable assertion about source data, similar to unit test, which provides a flexible, declarative language for describing expected behaviors.
- List of available expectations [here](https://greatexpectations.io/expectations)
- We can also group all expectations into one, called Expectation Suite.

### Checkpoint

- GX allows us to create checkpoint to perform data validation for each different datasources.
  ![alt text](https://docs.greatexpectations.io/assets/images/how_a_checkpoint_works-10e7fda2c9013d98a36c1d8526036764.png)

## Example

```py
from great_expectations import get_context
from great_expectations.data_context import FileDataContext

# Create data context in current directory
context = FileDataContext.create(project_root_dir='./')

# Connect to datasource
# for accessing and interacting with data from a wide variety of source systems.
datasource = context.sources.add_pandas('main-dataset')

# Create data asset
# a collection of records within a Datasource
asset_name = 'nfl_players_dataset'
path_to_data = 'https://raw.githubusercontent.com/yuda-notes/lecture-notes/refs/heads/main/dataset/players.csv'
asset = datasource.add_csv_asset(asset_name, filepath_or_buffer=path_to_data)

# Build batch request
# contains all the necessary details to query the appropriate underlying data
batch_request = asset.build_batch_request()

# Create expectation suite
# a collection of verifiable assertions about data
expectation_suite_name = 'expectation-suite'
context.add_or_update_expectation_suite(expectation_suite_name)

# Create a validator using above expectation suite
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name
)

# Define what validation should perform
# check missing values
validator.expect_column_values_to_not_be_null(column='full_school_name')
validator.expect_column_values_to_not_be_null(column='player_name')

# check duplicate values
validator.expect_column_values_to_be_unique(column='id')

# check name length between 3 to 50 chars
validator.expect_column_value_lengths_to_be_between(
    column='player_name', min_value=3, max_value=50)

# Save Expectation Suite
validator.save_expectation_suite(discard_failed_expectations=False)

# Create a checkpoint
# primary means for validating data in a production deployment of Great Expectations
checkpoint_1 = context.add_or_update_checkpoint(
    name='checkpoint_1',
    validator=validator,
)

# Run a checkpoint
checkpoint_result = checkpoint_1.run()

# Build data docs
context.build_data_docs()

# Open data docs
context.open_data_docs()
```
