from celery import shared_task
import time




@shared_task
def test():
    time.sleep(7)
    print ("test")



def test2():
    time.sleep(7)
    print ("test2")