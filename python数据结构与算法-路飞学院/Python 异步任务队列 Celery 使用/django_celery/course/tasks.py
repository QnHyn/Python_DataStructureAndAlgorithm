import time
from celery.task import Task


class CourseTask(Task):
    # 任务名称
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        time.sleep(4)
        print('end course task')
