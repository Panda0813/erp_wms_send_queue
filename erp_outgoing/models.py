from django.db import models


class ViewInfo(models.Model):
    view_name = models.CharField(verbose_name='视图名称', max_length=100)
    service_name = models.CharField(verbose_name='业务名称', max_length=100)
    params_map = models.TextField(verbose_name='erp与wms参数转换模板', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'service_base_info'
        verbose_name = '视图关系表'
        verbose_name_plural = verbose_name


class SendToWmsRecord(models.Model):
    view = models.ForeignKey(ViewInfo, verbose_name='视图', on_delete=models.SET_NULL, null=True)
    fid = models.CharField(verbose_name='视图ID', max_length=100)
    send_date = models.CharField(verbose_name='推送日期', max_length=20)
    base_data = models.TextField(verbose_name='原始信息')
    send_data = models.TextField(verbose_name='推送信息')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'erp_send_record'
        verbose_name = 'ERP推送记录表'
        verbose_name_plural = verbose_name
