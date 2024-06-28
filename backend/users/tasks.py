from django.core import management

from sinister_scheme import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
