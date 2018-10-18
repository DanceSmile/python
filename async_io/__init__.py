'''
异步IO模型需要一个消息循环
在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：

消息模型是如何解决同步IO必须等待IO操作这一问题的呢？
当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，
然后直接结束本轮消息处理，进入下一轮消息处理过程。
当IO操作完成后，将收到一条“IO完成”的消息，处理该消息时就可以直接获取IO操作结果。

loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)
'''
