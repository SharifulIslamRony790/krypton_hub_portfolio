from django import template
from django.db.models import Count
from core.models import ContactMessage, Service, TeamMember
import json

register = template.Library()


@register.simple_tag
def get_dashboard_stats():
    total_leads = ContactMessage.objects.count()
    unread_leads = ContactMessage.objects.filter(is_read=False).count()
    active_services = Service.objects.count()
    team_count = TeamMember.objects.count()

    # Get grouping for charts
    leads_by_service_qs = ContactMessage.objects.values(
        'service').annotate(count=Count('service'))

    # Map service choices to readable labels
    service_dict = dict(ContactMessage.SERVICE_CHOICES)

    chart_labels = []
    chart_data = []

    for item in leads_by_service_qs:
        service_key = item['service']
        label = service_dict.get(service_key, service_key)
        chart_labels.append(label)
        chart_data.append(item['count'])

    return {
        'total_leads': total_leads,
        'unread_leads': unread_leads,
        'active_services': active_services,
        'team_count': team_count,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
    }
