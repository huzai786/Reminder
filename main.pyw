import time

import schedule

from whatsapp.whatsapp import Person, Job, Schedular


hafsa = Person(number='+92 317 2164811')
hafsa_job1 = Job(time='10:55', reminder='checking')
hafsa_job2 = Job(time='11:00', reminder='checking2')
hafsa_job3 = Job(time='11:33', reminder='checking3')

hafsa_reminder = Schedular(hafsa, hafsa_job1, hafsa_job2, hafsa_job3)
hafsa_reminder.schedule_reminder()


while True:
    schedule.run_pending()
    time.sleep(1)

