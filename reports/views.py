from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from campaigns.models import Campaign

@api_view(['GET'])
def campaign_summary(request):
    total_campaigns = Campaign.objects.count()

    totals = Campaign.objects.aggregate(
        total_budget=Sum('budget'),
        total_clicks=Sum('clicks'),
        total_impressions=Sum('impressions')
    )

    average_ctr = 0
    if totals['total_impressions']:
        average_ctr = (totals['total_clicks'] / totals['total_impressions']) * 100

    return Response({
        "total_campaigns": total_campaigns,
        "total_budget": totals['total_budget'],
        "total_clicks": totals['total_clicks'],
        "total_impressions": totals['total_impressions'],
        "average_ctr": round(average_ctr, 2)
    })
