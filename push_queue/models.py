from django.db import models


class ServiceBaseInfo(models.Model):
    name = models.CharField(verbose_name='业务名称', max_length=100)
    desc = models.CharField(verbose_name='业务描述', max_length=200, null=True)
    sender = models.CharField(verbose_name='发送方', max_length=100)
    receiver = models.CharField(verbose_name='接收方', max_length=100)
    send_address = models.CharField(verbose_name='推送接口', max_length=200, null=True)
    authentication_func = models.CharField(verbose_name='获取验证的函数', max_length=100, null=True)
    headers = models.TextField(verbose_name='所需请求头', null=True)
    # True：需要保证推送成功，不成功则要重新推送, False：只记录推送过程
    is_ensure_success = models.BooleanField(verbose_name='是否保证推送成功')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'service_base_info'
        verbose_name = '业务基础信息表'
        verbose_name_plural = verbose_name


class MiddlePushQueue(models.Model):
    service = models.ForeignKey(ServiceBaseInfo, verbose_name='所属业务', on_delete=models.PROTECT)
    lcbh = models.CharField(verbose_name='流程编号', max_length=50, null=True)
    send_date = models.CharField(verbose_name='推送日期', max_length=20)
    send_data = models.TextField(verbose_name='推送信息')
    send_status = models.CharField(verbose_name='推送状态', max_length=20)  # success 成功，fail 失败
    return_data = models.TextField(verbose_name='推送返回信息')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'middle_push_queue'
        verbose_name = '推送队列表'
        verbose_name_plural = verbose_name
