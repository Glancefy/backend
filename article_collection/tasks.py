from celery import shared_task
import random as rd


@shared_task
def scrape_articles():
    # print random number from 0 to 100
    print(f"\nThe random number is: {rd.randint(0, 100):=^10}")
