[Skip to Main Content](#aws-page-content-main)

* Filter: All

* English
* [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu)
* [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp)
* Support
* My account

* Search

  Filter: All
* [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
* [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

* [Home](https://aws.amazon.com/blogs/)
* Blogs
* Editions

## [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)

# Develop and test AWS Glue 5.0 jobs locally using a Docker container

by Subramanya Vajiraya and Noritaka Sekiyama on 12 MAR 2025 in [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue/ "View all posts in AWS Glue"), [Intermediate (200)](https://aws.amazon.com/blogs/big-data/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Technical How-to](https://aws.amazon.com/blogs/big-data/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-5-0-jobs-locally-using-a-docker-container/)  [Comments](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-5-0-jobs-locally-using-a-docker-container/#Comments)  Share

*August 2025: This post was updated with Appendix E: Spark history server.*

*April 2025: This post was updated with Glue 5.0 new features introduced in April.*

[AWS Glue](https://aws.amazon.com/glue) is a serverless data integration service that allows you to process and integrate data coming through different data sources at scale. AWS Glue 5.0, the latest version of AWS Glue for Apache Spark jobs, provides a performance-optimized Apache Spark 3.5 runtime experience for batch and stream processing. With AWS Glue 5.0, you get improved performance, enhanced security, support for the next generation of [Amazon SageMaker](https://aws.amazon.com/sagemaker/), and more. AWS Glue 5.0 enables you to develop, run, and scale your data integration workloads and get insights faster.

AWS Glue accommodates various development preferences through multiple job creation approaches. For developers who prefer direct coding, Python or Scala development is available using the AWS Glue ETL library.

Building production-ready data platforms requires robust development processes and continuous integration and delivery (CI/CD) pipelines. To support diverse development needs—whether on local machines, Docker containers on [Amazon Elastic Compute Cloud](http://aws.amazon.com/ec2) (Amazon EC2), or other environments—AWS provides an official AWS Glue Docker image through the [Amazon ECR Public Gallery](http://aws.amazon.com/ecr/). The image enables developers to work efficiently in their preferred environment while using the AWS Glue ETL library.

In this post, we show how to develop and test AWS Glue 5.0 jobs locally using a Docker container. This post is an updated version of the post [Develop and test AWS Glue version 3.0 and 4.0 jobs locally using a Docker container](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/), and uses AWS Glue 5.0 .

## Available Docker images

The following Docker images are available for the [Amazon ECR Public Gallery](https://gallery.ecr.aws/glue/aws-glue-libs):

* **AWS Glue version 5.0** – `ecr.aws/glue/aws-glue-libs:5`

AWS Glue Docker images are compatible with both `x86_64` and `arm64`.

In this post, we use `public.ecr.aws/glue/aws-glue-libs:5` and run the container on a local machine (Mac, Windows, or Linux). This container image has been tested for AWS Glue 5.0 Spark jobs. The image contains the following:

* Amazon Linux 2023
* AWS Glue ETL Library
* Apache Spark 3.5.4
* Open table format libraries; Apache Iceberg 1.7.1, Apache Hudi 0.15.0, and Delta Lake 3.3.0
* AWS Glue Data Catalog client
* [Amazon Redshift connector for Apache Spark](https://github.com/spark-redshift-community/spark-redshift)
* [Amazon DynamoDB connector for Apache Hadoop](https://github.com/awslabs/emr-dynamodb-connector)

To set up your container, you pull the image from the ECR Public Gallery and then run the container. We demonstrate how to run your container with the following methods, depending on your requirements:

* `spark-submit`
* REPL shell (`pyspark`)
* `pytest`
* Visual Studio Code

## Prerequisites

Before you start, make sure that Docker is installed and the Docker daemon is running. For installation instructions, see the Docker documentation for [Mac](https://docs.docker.com/docker-for-mac/install/), [Windows](https://docs.docker.com/docker-for-windows/install/), or [Linux](https://docs.docker.com/engine/install/). Also make sure that you have at least 7 GB of disk space for the image on the host running Docker.

## Configure AWS credentials

To enable AWS API calls from the container, set up your AWS credentials with the following steps:

1. [Create an AWS named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html).
2. Open cmd on Windows or a terminal on Mac/Linux, and run the following command:

```
PROFILE_NAME="profile_name"
```

In the following sections, we use this AWS named profile.

## Pull the image from the ECR Public Gallery

If you’re running Docker on Windows, choose the Docker icon (right-click) and choose **Switch to Linux containers** before pulling the image.

Run the following command to pull the image from the ECR Public Gallery:

```
docker pull public.ecr.aws/glue/aws-glue-libs:5
```

## Run the container

Now you can run a container using this image. You can choose any of following methods based on your requirements.

### spark-submit

You can run an AWS Glue job script by running the `spark-submit` command on the container.

Write your job script (`sample.py` in the following example) and save it under the `/local_path_to_workspace/src/` directory using the following commands:

```
$ WORKSPACE_LOCATION=/local_path_to_workspace
$ SCRIPT_FILE_NAME=sample.py
$ mkdir -p ${WORKSPACE_LOCATION}/src
$ vim ${WORKSPACE_LOCATION}/src/${SCRIPT_FILE_NAME}
```

These variables are used in the following `docker run` command. The sample code (`sample.py`) used in the `spark-submit` command is included in the appendix at the end of this post.

Run the following command to run the `spark-submit` command on the container to submit a new Spark application:

```
$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_spark_submit \
    public.ecr.aws/glue/aws-glue-libs:5 \
    spark-submit /home/hadoop/workspace/src/$SCRIPT_FILE_NAME
```

### REPL shell (pyspark)

You can run a REPL (read-eval-print loop) shell for interactive development. Run the following command to run the pyspark command on the container to start the REPL shell:

```
$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_pyspark \
    public.ecr.aws/glue/aws-glue-libs:5 \
    pyspark
```

You will see following output:

```
Python 3.11.11 (main, Mar 20 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.4-amzn-0
      /_/

Using Python version 3.11.11 (main, Mar 20 2025 00:00:00)
Spark context Web UI available at None
Spark context available as 'sc' (master = local[*], app id = local-1744014002826).
SparkSession available as 'spark'.
>>>
```

With this REPL shell, you can code and test interactively.

### pytest

For unit testing, you can use `pytest` for AWS Glue Spark job scripts.

Run the following commands for preparation:

```
$ WORKSPACE_LOCATION=/local_path_to_workspace
$ SCRIPT_FILE_NAME=sample.py
$ UNIT_TEST_FILE_NAME=test_sample.py
$ mkdir -p ${WORKSPACE_LOCATION}/tests
$ vim ${WORKSPACE_LOCATION}/tests/${UNIT_TEST_FILE_NAME}
```

Now let’s invoke `pytest` using `docker run`:

```
$ docker run -i --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    --workdir /home/hadoop/workspace \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_pytest \
    public.ecr.aws/glue/aws-glue-libs:5 \
    -c "python3 -m pytest --disable-warnings"
```

When `pytest` finishes executing unit tests, your output will look something like the following:

```
============================= test session starts ==============================
platform linux -- Python 3.11.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/hadoop/workspace
plugins: integration-mark-0.2.0
collected 1 item

tests/test_sample.py .                                                   [100%]

======================== 1 passed, 1 warning in 34.28s =========================
```

### Visual Studio Code

To set up the container with Visual Studio Code, complete the following steps:

1. Install Visual Studio Code.
2. Install [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
3. Install [Dev Containers](https://code.visualstudio.com/docs/remote/containers).
4. Open the workspace folder in Visual Studio Code.
5. Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (Mac).
6. Enter `Preferences: Open Workspace Settings (JSON)`.
7. Press **Enter**.
8. Enter following JSON and save it:

```
{
    "python.defaultInterpreterPath": "/usr/bin/python3.11",
    "python.analysis.extraPaths": [
        "/usr/lib/spark/python/lib/py4j-0.10.9.7-src.zip:/usr/lib/spark/python/:/usr/lib/spark/python/lib/",
    ]
}
```

Now you’re ready to set up the container.

9. Run the Docker container:

```
$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_pyspark \
    public.ecr.aws/glue/aws-glue-libs:5 \
    pyspark
```

10. Start Visual Studio Code.
11. Choose **Remote Explorer** in the navigation pane.
12. Choose the container `ecr.aws/glue/aws-glue-libs:5` (right-click) and choose **Attach in Current Window**.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/06/bdb4724-vs_attach_container.jpg)

13. If the following dialog appears, choose **Got it**.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/06/bdb4724-vs_attach_dialog.jpg)

14. Open `/home/hadoop/workspace/`.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/06/bdb4724-vs_choose_ws.jpg)

15. Create an AWS Glue PySpark script and choose **Run**.

You should see the successful run on the AWS Glue PySpark script.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/06/bdb4724-vs_run_script.jpg)

## Changes between the AWS Glue 4.0 and AWS Glue 5.0 Docker image

The following are major changes between the AWS Glue 4.0 and Glue 5.0 Docker image:

* In AWS Glue 5.0, there is a single container image for both batch and streaming jobs. This differs from AWS Glue 4.0, where there was one image for batch and another for streaming.
* In AWS Glue 5.0, the default user name of the container is hadoop. In AWS Glue 4.0, the default user name was glue\_user.
* In AWS Glue 5.0, several additional libraries, including JupyterLab and Livy, have been removed from the image. You can manually install them.
* In AWS Glue 5.0, all of Iceberg, Hudi, and Delta libraries are pre-loaded by default, and the environment variable `DATALAKE_FORMATS` is no longer needed. Until AWS Glue 4.0, the environment variable `DATALAKE_FORMATS` was used to specify whether the specific table format is loaded.

The preceding list is specific to the Docker image. To learn more about AWS Glue 5.0 updates, see [Introducing AWS Glue 5.0 for Apache Spark](https://aws.amazon.com/blogs/big-data/introducing-aws-glue-5-0-for-apache-spark/) and [Migrating AWS Glue for Spark jobs to AWS Glue version 5.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-50.html).

## Considerations

Keep in mind that the following features are not supported when using the AWS Glue container image to develop job scripts locally:

* [Job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html)
* AWS Glue Parquet writer (see [Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html))
* [FillMissingValues transform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-fillmissingvalues.html)
* [FindMatches transform](https://docs.aws.amazon.com/glue/latest/dg/machine-learning.html#find-matches-transform)
* [Vectorized SIMD CSV reader](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-csv-home.html#aws-glue-programming-etl-format-simd-csv-reader)
* The property [customJdbcDriverS3Path](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html#aws-glue-programming-etl-connect-jdbc) for loading the JDBC driver from an [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) path
* [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
* [Sensitive data detection](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html)
* [AWS Lake Formation](https://aws.amazon.com/lake-formation/) permission-based credential vending

## Conclusion

In this post, we explored how the AWS Glue 5.0 Docker images provide a flexible foundation for developing and testing AWS Glue job scripts in your preferred environment. These images, readily available in the Amazon ECR Public Gallery, streamline the development process by offering a consistent, portable environment for AWS Glue development.

To learn more about how to build end-to-end development pipeline, see [End-to-end development lifecycle for data engineers to build a data integration pipeline using AWS Glue](https://aws.amazon.com/blogs/big-data/end-to-end-development-lifecycle-for-data-engineers-to-build-a-data-integration-pipeline-using-aws-glue/). We encourage you to explore these capabilities and share your experiences with the AWS community.

---

## Appendix A: AWS Glue job sample codes for testing

This appendix introduces three different scripts as AWS Glue job sample codes for testing purposes. You can use any of them in the tutorial.

The following sample.py code uses the AWS Glue ETL library with an [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) API call. The code requires Amazon S3 permissions in [AWS Identity and Access Management](http://aws.amazon.com/iam) (IAM). You need to grant the IAM-managed policy arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess or IAM custom policy that allows you to make ListBucket and GetObject API calls for the S3 path.

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

class GluePythonSampleTest:
    def __init__(self):
        params = []
        if '--JOB_NAME' in sys.argv:
            params.append('JOB_NAME')
        args = getResolvedOptions(sys.argv, params)

        self.context = GlueContext(SparkContext.getOrCreate())
        self.job = Job(self.context)

        if 'JOB_NAME' in args:
            jobname = args['JOB_NAME']
        else:
            jobname = "test"
        self.job.init(jobname, args)

    def run(self):
        dyf = read_json(self.context, "s3://awsglue-datasets/examples/us-legislators/all/persons.json")
        dyf.printSchema()

        self.job.commit()

def read_json(glue_context, path):
    dynamicframe = glue_context.create_dynamic_frame.from_options(
        connection_type='s3',
        connection_options={
            'paths': [path],
            'recurse': True
        },
        format='json'
    )
    return dynamicframe

if __name__ == '__main__':
    GluePythonSampleTest().run()
```

The following test\_sample.py code is a sample for a unit test of sample.py:

```
import pytest
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
import sys
from src import sample

@pytest.fixture(scope="module", autouse=True)
def glue_context():
    sys.argv.append('--JOB_NAME')
    sys.argv.append('test_count')

    args = getResolvedOptions(sys.argv, ['JOB_NAME'])
    context = GlueContext(SparkContext.getOrCreate())
    job = Job(context)
    job.init(args['JOB_NAME'], args)
```

## Appendix B: Adding JDBC drivers and Java libraries

To add a JDBC driver not currently available in the container, you can create a new directory under your workspace with the JAR files you need and mount the directory to `/opt/spark/jars/` in the `docker run` command. JAR files found under `/opt/spark/jars/` within the container are automatically added to Spark Classpath and will be available for use during the job run.

For example, you can use the following `docker run` command to add JDBC driver jars to a PySpark REPL shell:

```
$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -v $WORKSPACE_LOCATION/jars/:/opt/spark/jars/ \
    --workdir /home/hadoop/workspace \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_jdbc \
    public.ecr.aws/glue/aws-glue-libs:5 \
    pyspark
```

As highlighted earlier, the `customJdbcDriverS3Path` connection option can’t be used to import a custom JDBC driver from Amazon S3 in AWS Glue container images.

## Appendix C: Adding Livy and JupyterLab

The AWS Glue 5.0 container image doesn’t have Livy installed by default. You can create a new container image extending the AWS Glue 5.0 container image as the base. The following Dockerfile demonstrates how you can extend the Docker image to include additional components you need to enhance your development and testing experience.

To get started, create a directory on your workstation and place the `Dockerfile.livy_jupyter` file in the directory:

```
$ mkdir -p $WORKSPACE_LOCATION/jupyterlab/
$ cd $WORKSPACE_LOCATION/jupyterlab/
$ vim Dockerfile.livy_jupyter
```

The following code is `Dockerfile.livy_jupyter`:

```
FROM public.ecr.aws/glue/aws-glue-libs:5 AS glue-base

ENV LIVY_SERVER_JAVA_OPTS="--add-opens java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED"

# Download Livy
ADD --chown=hadoop:hadoop https://dlcdn.apache.org/incubator/livy/0.8.0-incubating/apache-livy-0.8.0-incubating_2.12-bin.zip ./

# Install and configure Livy
RUN unzip apache-livy-0.8.0-incubating_2.12-bin.zip && \
rm apache-livy-0.8.0-incubating_2.12-bin.zip && \
mv apache-livy-0.8.0-incubating_2.12-bin livy && \
mkdir -p livy/logs && \
cat <<EOF >> livy/conf/livy.conf
livy.server.host = 0.0.0.0
livy.server.port = 8998
livy.spark.master = local
livy.repl.enable-hive-context = true
livy.spark.scala-version = 2.12
EOF && \
cat <<EOF >> livy/conf/log4j.properties
log4j.rootCategory=INFO,console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n
log4j.logger.org.eclipse.jetty=WARN
EOF

# Switching to root user temporarily to install dev dependency packages
USER root
RUN dnf update -y && dnf install -y krb5-devel gcc python3.11-devel
USER hadoop

# Install SparkMagic and JupyterLab
RUN export PATH=$HOME/.local/bin:$HOME/livy/bin/:$PATH && \
printf "numpy<2\nIPython<=7.14.0\n" > /tmp/constraint.txt && \
pip3.11 --no-cache-dir install --constraint /tmp/constraint.txt --user pytest boto==2.49.0 jupyterlab==3.6.8 IPython==7.14.0 ipykernel==5.5.6 ipywidgets==7.7.2 sparkmagic==0.21.0 jupyterlab_widgets==1.1.11 && \
jupyter-kernelspec install --user $(pip3.11 --no-cache-dir show sparkmagic | grep Location | cut -d" " -f2)/sparkmagic/kernels/sparkkernel && \
jupyter-kernelspec install --user $(pip3.11 --no-cache-dir show sparkmagic | grep Location | cut -d" " -f2)/sparkmagic/kernels/pysparkkernel && \
jupyter server extension enable --user --py sparkmagic && \
cat <<EOF >> /home/hadoop/.local/bin/entrypoint.sh
#!/usr/bin/env bash
mkdir -p /home/hadoop/workspace/
livy-server start
sleep 5
jupyter lab --no-browser --ip=0.0.0.0 --allow-root --ServerApp.root_dir=/home/hadoop/workspace/ --ServerApp.token='' --ServerApp.password=''
EOF

# Setup Entrypoint script
RUN chmod +x /home/hadoop/.local/bin/entrypoint.sh

# Add default SparkMagic Config
ADD --chown=hadoop:hadoop https://raw.githubusercontent.com/jupyter-incubator/sparkmagic/refs/heads/master/sparkmagic/example_config.json .sparkmagic/config.json

# Update PATH var
ENV PATH=/home/hadoop/.local/bin:/home/hadoop/livy/bin/:$PATH

ENTRYPOINT ["/home/hadoop/.local/bin/entrypoint.sh"]
```

Run the docker build command to build the image:

```
docker build \
    -t glue_v5_livy \
    --file $WORKSPACE_LOCATION/jupyterlab/Dockerfile.livy_jupyter \
    $WORKSPACE_LOCATION/jupyterlab/
```

When the image build is complete, you can use the following docker run command to start the newly built image:

```
docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -p 8998:8998 \
    -p 8888:8888 \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_jupyter  \
    glue_v5_livy
```

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/06/bdb4724-jupyter.jpg)

## Appendix D: Adding extra Python libraries

In this section, we discuss adding extra Python libraries and installing Python packages using

### Local Python libraries

To add local Python libraries, place them under a directory and assign the path to `$EXTRA_PYTHON_PACKAGE_LOCATION`:

```
$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -v $EXTRA_PYTHON_PACKAGE_LOCATION:/home/hadoop/workspace/extra_python_path/ \
    --workdir /home/hadoop/workspace \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_pylib \
    public.ecr.aws/glue/aws-glue-libs:5 \
    -c 'export PYTHONPATH=/home/hadoop/workspace/extra_python_path/:$PYTHONPATH; pyspark'
```

To validate that the path has been added to `PYTHONPATH`, you can check for its existence in `sys.path`:

```
Python 3.11.11 (main, Mar 20 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.4-amzn-0
      /_/

Using Python version 3.11.11 (main, Mar 20 2025 00:00:00)
Spark context Web UI available at None
Spark context available as 'sc' (master = local[*], app id = local-1744014002826).
SparkSession available as 'spark'.
>>> import sys
>>> "/home/hadoop/workspace/extra_python_path" in sys.path
True
```

### Installing Python packages using pip

To install packages from PyPI (or any other artifact repository) using pip, you can use the following approach:

```
docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    --workdir /home/hadoop/workspace \
    -e AWS_PROFILE=$PROFILE_NAME \
    -e SCRIPT_FILE_NAME=$SCRIPT_FILE_NAME \
    --name glue5_pylib \
    public.ecr.aws/glue/aws-glue-libs:5 \
    -c 'pip3 install snowflake==1.0.5; spark-submit /home/hadoop/workspace/src/$SCRIPT_FILE_NAME'
```

## Appendix E: Debugging with Spark history server

In case you want to debug your Spark scripts with Spark history server, run following commands.

### spark-submit

```
docker run --rm -it -p 18080:18080 public.ecr.aws/glue/aws-glue-libs:5 -c "/usr/lib/spark/sbin/start-history-server.sh && spark-submit sample.py"
```

### REPL (pyspark)

```
docker run --rm -it -p 18080:18080 public.ecr.aws/glue/aws-glue-libs:5 -c "/usr/lib/spark/sbin/start-history-server.sh && pyspark"
```

---

### About the Authors

**![Author Headshot - Subramanya Vajiraya](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2023/05/27/Subramanya-Vajiraya.jpg)Subramanya Vajiraya** is a Sr. Cloud Engineer (ETL) at AWS Sydney specialized in AWS Glue. He is passionate about helping customers solve issues related to their ETL workload and implementing scalable data processing and analytics pipelines on AWS. Outside of work, he enjoys going on bike rides and taking long walks with his dog Ollie.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2021/02/10/Noritaka-Sekiyama-p.png)Noritaka Sekiyama** is a Principal Big Data Architect on the AWS Glue team. He works based in Tokyo, Japan. He is responsible for building software artifacts to help customers. In his spare time, he enjoys cycling with his road bike.

Loading comments…

### Resources

* [Amazon Athena](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-athena?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon EMR](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-emr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Kinesis](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon MSK](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-managed-streaming-for-apache-kafka/)
* [Amazon QuickSight](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-quicksight?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-social)

[Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc1=f_ct&src=footer_signup)

## Learn

* [What Is AWS?](/what-is-aws/?nc1=f_cc)
* [What Is Cloud Computing?](/what-is-cloud-computing/?nc1=f_cc)
* [What Is Agentic AI?](/what-is/agentic-ai/?nc1=f_cc)
* [Cloud Computing Concepts Hub](/what-is/?nc1=f_cc)
* [AWS Cloud Security](/security/?nc1=f_cc)
* [What's New](/new/?nc1=f_cc)
* [Blogs](/blogs/?nc1=f_cc)
* [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

* [Getting Started](/getting-started/?nc1=f_cc)
* [Training](/training/?nc1=f_cc)
* [AWS Trust Center](/trust-center/?nc1=f_cc)
* [AWS Solutions Library](/solutions/?nc1=f_cc)
* [Architecture Center](/architecture/?nc1=f_cc)
* [Product and Technical FAQs](/faqs/?nc1=f_dr)
* [Analyst Reports](/resources/analyst-reports/?nc1=f_cc)
* [AWS Partners](/partners/work-with-partners/?nc1=f_dr)

## Developers

* [Builder Center](/developer/?nc1=f_dr)
* [SDKs & Tools](/developer/tools/?nc1=f_dr)
* [.NET on AWS](/developer/language/net/?nc1=f_dr)
* [Python on AWS](/developer/language/python/?nc1=f_dr)
* [Java on AWS](/developer/language/java/?nc1=f_dr)
* [PHP on AWS](/developer/language/php/?nc1=f_cc)
* [JavaScript on AWS](/developer/language/javascript/?nc1=f_dr)

## Help

* [Contact Us](/contact-us/?nc1=f_m)
* [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
* [AWS re:Post](https://repost.aws/?nc1=f_dr)
* [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
* [AWS Support Overview](/premiumsupport/?nc1=f_dr)
* [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
* [AWS Accessibility](/accessibility/?nc1=f_cc)
* [Legal](/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[x](https://twitter.com/awscloud) [facebook](https://www.facebook.com/amazonwebservices) [linkedin](https://www.linkedin.com/company/amazon-web-services/) [instagram](https://www.instagram.com/amazonwebservices/) [twitch](https://www.twitch.tv/aws) [youtube](https://www.youtube.com/user/AmazonWebServices/Cloud/) [podcasts](/podcasts/?nc1=f_cc) [email](https://pages.awscloud.com/communication-preferences?trk=homepage)

* [Privacy](/privacy/?nc1=f_pr)
* [Site terms](/terms/?nc1=f_pr)
* Cookie Preferences

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved.