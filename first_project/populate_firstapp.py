import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from faker import Faker
from firstapp.models import Topic,AccessRecord,Webpage

fakegen = Faker()
topics = ['Search','Social','News','Sports']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top= add_topic()
        #Create fake datafor that entry
        fakeurl = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #CReate Web page entry
        webpg=Webpage.objects.get_or_create(topic=top,urls=fakeurl,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)
if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete")

