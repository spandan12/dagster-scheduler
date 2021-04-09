# dagster-scheduler
It's a demo to scheduler a function with no argument given. This is created a give an idea of how scheduler is set up in dagster

## Development Setup

### Prerequisites
---------------------

* [Python>=3.8](https://www.python.org/downloads/release/python-383/)
* [Git](https://git-scm.com/downloads)
* [Virtualenv](https://pypi.org/project/virtualenv/)

### Initial Setup
---------------------
-   [Clone](git@github.com:spandan12/dagster-scheduler.git) the main repository locally.

    ``` {.sourceCode .text}
    $ git clone git@github.com:spandan12/dagster-scheduler.git
    $ cd dagster-scheduler
    ```

-   Create a virtualenv.

    ``` {.sourceCode .text}
    $ virtualenv venv --python=python3.8
    $ source venv/bin/activate
    ```

    On Windows, activating is different.

    ``` {.sourceCode .text}
    > env\Scripts\activate
    ```

-   Install requirements.

    ``` {.sourceCode .text}
    $ pip install -r requirements.txt
    ```

### Initial Setup
---------------------

-   Copy the path of the project. 
    ``` {.sourceCode .text}
    $ pwd
    ```
-   Use the path as the dagster_home
    ``` {.sourceCode .text}
    $ export DAGSTER_HOME=<path>
    ```
-   Start the scheduler

    ``` {.sourceCode .text}
    $ dagster schedule start --start-all
    ```
    
-   Start the dagit

    ``` {.sourceCode .text}
    $ dagit
    ```
    > Note: To know if your scheulder is running. Go to schedules section in dagit. You will get the information of runs once in every minute
