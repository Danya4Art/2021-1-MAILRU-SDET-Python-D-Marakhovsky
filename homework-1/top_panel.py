# Top panel module names
tags = ['SEGMENTS', 'BILLING', 'STATISTICS',
       'PRO', 'PROFILE', 'TOOLS', 'DASHBOARD', 'LOGOUT']

# Top panel module @hrefs  
href = list(map(lambda x: '//*[@href="/{0}"]'.format(x.lower()), tags))

# URL of pages from top panel
urls = [
'https://target.my.com/segments/segments_list',
'https://target.my.com/billing#deposit',
'https://target.my.com/statistics/summary',
'https://target.my.com/pro',
'https://target.my.com/profile/contacts',
'https://target.my.com/tools/feeds'
]