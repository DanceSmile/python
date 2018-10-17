'''
Email的历史比Web还要久远，直到现在，Email也是互联网上应用非常广泛的服务。

MUA：Mail User Agent——邮件用户代理
Outlook或者Foxmail之类的软件

MTA：Mail Transfer Agent——邮件传输代理
Email服务提供商，比如网易、新浪等等

MDA：Mail Delivery Agent——邮件投递代理


本质上就是：
1.编写MUA把邮件发到MTA；
2.编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，
后面的MTA到另一个MTA也是用SMTP协议。

收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；
IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。
'''