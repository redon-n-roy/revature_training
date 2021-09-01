# AWS EMR Demo
With Amazon EMR you can set up a cluster to process and analyze data with big data frameworks in just a few minutes. This tutorial shows you how to launch a sample cluster using Spark, and how to run a simple PySpark script and data in CSV file format stored in an Amazon S3 bucket.

### EMR Workflow Diagram
![EMR Workflow](https://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-workflow.png)

:copyright: Image taken from [here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html).

## Resources
1. **departuredelays.zip** - dataset used for the demo. Unzip to get the CSV file. **If you face issue in unzipping, use [7-zip](https://www.7-zip.org/download.html).
2. **departureDelay.py** - pyspark program to demostarate basixc working of AWS EMR including reading data from S3 bucket into a dataframe, creating TempView and running sparkSQL operations.
3. **outputdepartureDelay.py** - simple pyspark program to show how to store the output into S3.

:octocat:
