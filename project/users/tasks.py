from celery import shared_task


@shared_task
def divide(x, y):
    import time
    print("starting sleep")
    time.sleep(5)
    print("ending sleep")
    return x / y
