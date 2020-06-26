import rx
from rx import operators as ops
import multiprocessing
import rx.scheduler as scheduler

thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = scheduler.ThreadPoolScheduler(thread_count)

rx.of(1,2,3,4,5,6,7,8,9,10).pipe(
  ops.filter(lambda i: i % 2 == 0), 
  ops.subscribe_on(thread_pool_scheduler)
  ).subscribe(lambda i: print(1))

rx.of(1,2,3,4,5,6,7,8,9,10).pipe(
  ops.filter(lambda i: i % 2 == 0), 
  ops.subscribe_on(thread_pool_scheduler)
  ).subscribe(lambda i: print(2))

rx.of(1,2,3,4,5,6,7,8,9,10).pipe(
  ops.filter(lambda i: i % 2 == 0), 
  ops.subscribe_on(thread_pool_scheduler)
  ).subscribe(lambda i: print(3))

rx.of(1,2,3,4,5,6,7,8,9,10).pipe(
  ops.filter(lambda i: i % 2 == 0), 
  ops.subscribe_on(thread_pool_scheduler)
  ).subscribe(lambda i: print(4))

print("AAAAA")
