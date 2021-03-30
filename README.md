# Description

This module is an alternative [Airflow](https://github.com/apache/airflow) XCom backend.

# Details

Airflow [XCom](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#xcoms) is a way Tasks exchange values in a DAG. By default the values are stored in the default Airflow database. This makes it unsuitable for sharing large volumes of data for two reasons:

* PostgreSQL has a limit of 1GB per XCom value
* Using the same database as other Airflow data may degrade performance

For these reasons Airflow [allows for implementing a custom XCom backend](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#custom-xcom-backend). This module is one such implementation for use with Redis.

# Requirements

Currently the module uses the [Python Redis module](https://pypi.org/project/redis/) which is already provided by Airflow.

The only requirements is for Airflow to have a Redis [Connection](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#connections) defined called `xcom_cache`.

# TODO

Possible future improvements:

* Get Connection ID from configuration or environment variables
* Splitting of values into different keys to avoid size limits
