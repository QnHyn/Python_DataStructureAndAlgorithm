import djcelery
from datetime import timedelta
djcelery.setup_loader()

CELERY_IMPORTS = (
    'course.tasks',
)

# 把定时任务和普通任务区分开，绑定到不同的队列中
CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue',
    }
}

# 绑定默认队列为work_queue
CELERY_DEFAULT_QUEUE = 'work_queue'

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True

#设置并发的worker数量
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

#每个worker最多执行100个任务然后就被销毁，可以防止内存泄露(非常重要)
CELERYD_MAX_TASKS_PER_CHILD = 100

# 设置每一个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    # 每过10秒执行以下task1.add的定时任务
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=10),
        'options':{
            'queue': 'beat_tasks'
        }
    },
}