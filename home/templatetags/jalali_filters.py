from django import template
import jdatetime


register = template.Library()


@register.filter
def to_jalali(gregorian_date):
    if not gregorian_date:
        return ""

    if hasattr(gregorian_date, 'date'):
        gregorian_date = gregorian_date.date()

    jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
    return jalali_date.strftime("%Y/%m/%d")


@register.filter
def to_jalali_datetime(gregorian_datetime):
    if not gregorian_datetime:
        return ""

    jalali_date = jdatetime.datetime.fromgregorian(datetime=gregorian_datetime)
    return jalali_date.strftime("%Y/%m/%d %H:%M:%S")