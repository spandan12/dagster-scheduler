
from dagster import  pipeline, repository, solid,ScheduleDefinition


@solid
def greet(context):
    context.log.info("Good morning")

@pipeline
def greeting_pipeline():
    greet()


greet_once_a_minute = ScheduleDefinition(
        "greet_once_a_minute",
        "*/1 * * * *",
        "greeting_pipeline",
    )

@repository
def hello_cereal_repository():
    return [greeting_pipeline, greet_once_a_minute]

__all__ = ['greeting_pipeline', "greet_once_a_minute"]