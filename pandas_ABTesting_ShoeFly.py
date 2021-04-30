import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(5))

platform_views=ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(platform_views)

ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks)

click_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

print(click_by_source)

clicks_pivot=click_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked']=clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])*100

print(clicks_pivot)

ab_groups=ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print(ab_groups)

ab_click_groups=ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='experimental_group',values='user_id').reset_index()

print(ab_click_groups)

a_clicks=ad_clicks[ad_clicks['experimental_group']=='A']
b_clicks=ad_clicks[ad_clicks['experimental_group']=='B']
print(a_clicks)

a_clicks_pivot=a_clicks.groupby(['day','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id').reset_index()

##add % column

a_clicks_pivot['%_clicked']=a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])*100
print(a_clicks_pivot)

b_clicks_pivot=b_clicks.groupby(['day','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id').reset_index()

##add % column

b_clicks_pivot['%_clicked']=b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False])*100
print(b_clicks_pivot)






