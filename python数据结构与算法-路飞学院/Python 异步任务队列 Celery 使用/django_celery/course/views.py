from django.http import JsonResponse
from course.tasks import CourseTask


def do(request):
    # 执行异步任务
    print("do request")
    # CourseTask.delay()
    #apply_async 传参数比较方便
    CourseTask.apply_async(args=('hello',), queue='work_queue')
    print("end do request")
    return JsonResponse({'result:': 'ok'})