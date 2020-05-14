import requests
import re
from requests import Request, Session
from bs4 import BeautifulSoup

#service_tag=raw_input("Enter a Dell Service Tag ")70JYWC2

url = 'https://www.dell.com/support/home/en-ca/product-support/servicetag/0-YW5odU91RHJWMDFjZDZ3WTRpWGNvQT090/overview'

cookies={'cookie':'eSupId=SID=129afb54-5589-4be6-9a99-325c084eeb63&ld=20201108; lwp=c=ca&l=en&cs=cabsdt1&s=bsd; dell_canary=live; DellCEMSession=F05BD3301579833C385FD1E93B8A879A; _abck=AFE59D6375D86D126ACFC0A908438A4B~0~YAAQZjIcuI3XaMNxAQAAIhin8QMMJWezGBpAfagLzI6akexQA2cvpUX6yWt7OxxyrcyPijzH2eSruQxaf0S2YJjNGe+7IkZvtGyInzVLjNRcKC0aUJufY4L029e12iR/v6AwoPnK2u/oA74irZHgGyqDWiGCO0AInlC4tdwilQCRiVI7rmqWHXQSLE3s2KXrcnzrl4fSTQIoCYNYNZQxh4yeYkDIiYaQHcfylavgWXgXCzBUiMKu0rzxd/r/VGjDRSftZzZrPXOUQAaShpaI3iECmDwa4WpWFtNnhsl0D3KTSVldCrF1DxxK/ZxKnC1MFtwRfM8=~-1~-1~-1; AMCVS_4DD80861515CAB990A490D45%40AdobeOrg=1; rumCki=false; _cls_v=7afd073a-7662-4e92-b7a8-768492a5285f; _cls_s=a5dcb64a-8780-4b39-a08a-597c57e32922:0; s_ecid=MCMID%7C58094480272501818763499939423452027571; cidlid=%3A%3A; sessionTime=2020%2C4%2C7%2C17%2C19%2C52%2C771; s_cc=true; TLGUID=58094480272501818763499939423452027571; s_sq=%5B%5BB%5D%5D; OLRProduct=OLRProduct=70JYWC2|; s_c49=c%3Dca%26l%3Den%26s%3Dbsd%26cs%3Dcabsdt1%26servicetag%3D70jywc2%26systemid%3Dnetworking-n3000-series; bm_sz=BCB218BA10704CDE8B17C5DC7AC9756D~YAAQXjIcuMHGWb9xAQAAc3Rb9gchOacYmruOQU4QRXZM/UjxnnacAaMAVDba7Jfpfgk6avnqwH5B1XKpEsy2Io7PAveRM+UYtIuaKUEn8zimkqfyfHqyNemy3vXx93yD7WFL9KzqUWJq374XT1HU90sWgaLBfBGLDo6aQnChHkQPEu7R7VR7tVwBrWZX; ak_bmsc=100FEF7BBE9F0B0EB8A3DE5E0C55384BB81C325E6C420000F8D9B55E0C0F5F22~pli6sfQSGRIR8cHy4TwtDyHzJDRTuo8L+hM5vyruO86W6eYphJHqS4F4mFEbrRIrzjkAVB0+1lM0/dG03hIrNnI7+o1q6L45vSQYEtYjXiA2r1f8l7zJ0PcjYj551e9SQPad/54lhZ24+sML4HsDsqyLp4qXNSbqRN9Nx3Qi/HQhrOo9JklhfX0vTrE2uw10vhx1eKS3+MjdC7tVk5mRYxEoAd+t8r5vtmmaWM+TRx1QSwVkykicdsQX9WyakXI0nf; AMCV_4DD80861515CAB990A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C18391%7CMCMID%7C58094480272501818763499939423452027571%7CMCAAMLH-1589580922%7C9%7CMCAAMB-1589580922%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1588983322s%7CNONE%7CMCSYNCSOP%7C411-18398%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_dl=1; s_channelstack=%5B%5B%27Direct%2520Load%27%2C%271588897192770%27%5D%2C%5B%27Direct%2520Load%27%2C%271588976122294%27%5D%5D; s_vnum=1620433192771%26vn%3D3; s_invisit=true; gpv_pn=ca%7Cen%7Ccabsdt1%7Cbsd%7Cesupport-productsupport%7Cproduct-support%7Cservicetag; s_ppv=ca%257Cen%257Ccabsdt1%257Cbsd%257Cesupport-productsupport%257Cproduct-support%257Cservicetag; s_depth=1; s_hwp=cabsdt1%7C%7Cnull%7C%7C8%3A5%3A2020%3A15%3A15%7C%7CN%7C%7CN%7C%7Cnull%7C%7C1316%7C%7Cnull%7C%7Cnull%7C%7CN%7C%7Cnull%7C%7Cnull%7C%7C70jywc2; akavpau_maintenance_vp=1588976584~id=b85b8ceaf352a7c4b3b7a5fac900bdd3; bm_sv=B02284772BEBC9BFBDB73CD4ED6CFE84~nscqg8OhWqoGmXh2lujXGz5yvhefPtRzK5Uw/QMdDru0OiBwTrdhc0MCjT/4k/YmZNDDEnwSGm+S1eigiIDVioZGBStV0YuZ3QlwFobWJ4f2KlEiAGwrcF47J0by5mDpLQjA79Fm68a30sQKuGB+cw==; RT="r=https%3A%2F%2Fwww.dell.com%2Fsupport%2Fhome%2Fen-ca%2Fproduct-support%2Fservicetag%2F0-YW5odU91RHJWMDFjZDZ3WTRpWGNvQT090%2Foverview&ul=1588976283658&hd=1588976284605'}

headers = {'referer':'https://www.dell.com/support/home/en-ca/product-support/servicetag/0-YW5odU91RHJWMDFjZDZ3WTRpWGNvQT090/overview','cookie':'eSupId=SID=129afb54-5589-4be6-9a99-325c084eeb63&ld=20201108; lwp=c=ca&l=en&cs=cabsdt1&s=bsd; dell_canary=live; DellCEMSession=F05BD3301579833C385FD1E93B8A879A; _abck=AFE59D6375D86D126ACFC0A908438A4B~0~YAAQZjIcuI3XaMNxAQAAIhin8QMMJWezGBpAfagLzI6akexQA2cvpUX6yWt7OxxyrcyPijzH2eSruQxaf0S2YJjNGe+7IkZvtGyInzVLjNRcKC0aUJufY4L029e12iR/v6AwoPnK2u/oA74irZHgGyqDWiGCO0AInlC4tdwilQCRiVI7rmqWHXQSLE3s2KXrcnzrl4fSTQIoCYNYNZQxh4yeYkDIiYaQHcfylavgWXgXCzBUiMKu0rzxd/r/VGjDRSftZzZrPXOUQAaShpaI3iECmDwa4WpWFtNnhsl0D3KTSVldCrF1DxxK/ZxKnC1MFtwRfM8=~-1~-1~-1; AMCVS_4DD80861515CAB990A490D45%40AdobeOrg=1; rumCki=false; _cls_v=7afd073a-7662-4e92-b7a8-768492a5285f; _cls_s=a5dcb64a-8780-4b39-a08a-597c57e32922:0; s_ecid=MCMID%7C58094480272501818763499939423452027571; cidlid=%3A%3A; sessionTime=2020%2C4%2C7%2C17%2C19%2C52%2C771; s_cc=true; TLGUID=58094480272501818763499939423452027571; s_sq=%5B%5BB%5D%5D; OLRProduct=OLRProduct=70JYWC2|; s_c49=c%3Dca%26l%3Den%26s%3Dbsd%26cs%3Dcabsdt1%26servicetag%3D70jywc2%26systemid%3Dnetworking-n3000-series; bm_sz=BCB218BA10704CDE8B17C5DC7AC9756D~YAAQXjIcuMHGWb9xAQAAc3Rb9gchOacYmruOQU4QRXZM/UjxnnacAaMAVDba7Jfpfgk6avnqwH5B1XKpEsy2Io7PAveRM+UYtIuaKUEn8zimkqfyfHqyNemy3vXx93yD7WFL9KzqUWJq374XT1HU90sWgaLBfBGLDo6aQnChHkQPEu7R7VR7tVwBrWZX; ak_bmsc=100FEF7BBE9F0B0EB8A3DE5E0C55384BB81C325E6C420000F8D9B55E0C0F5F22~pli6sfQSGRIR8cHy4TwtDyHzJDRTuo8L+hM5vyruO86W6eYphJHqS4F4mFEbrRIrzjkAVB0+1lM0/dG03hIrNnI7+o1q6L45vSQYEtYjXiA2r1f8l7zJ0PcjYj551e9SQPad/54lhZ24+sML4HsDsqyLp4qXNSbqRN9Nx3Qi/HQhrOo9JklhfX0vTrE2uw10vhx1eKS3+MjdC7tVk5mRYxEoAd+t8r5vtmmaWM+TRx1QSwVkykicdsQX9WyakXI0nf; AMCV_4DD80861515CAB990A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C18391%7CMCMID%7C58094480272501818763499939423452027571%7CMCAAMLH-1589580922%7C9%7CMCAAMB-1589580922%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1588983322s%7CNONE%7CMCSYNCSOP%7C411-18398%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_dl=1; s_channelstack=%5B%5B%27Direct%2520Load%27%2C%271588897192770%27%5D%2C%5B%27Direct%2520Load%27%2C%271588976122294%27%5D%5D; s_vnum=1620433192771%26vn%3D3; s_invisit=true; gpv_pn=ca%7Cen%7Ccabsdt1%7Cbsd%7Cesupport-productsupport%7Cproduct-support%7Cservicetag; s_ppv=ca%257Cen%257Ccabsdt1%257Cbsd%257Cesupport-productsupport%257Cproduct-support%257Cservicetag; s_depth=1; s_hwp=cabsdt1%7C%7Cnull%7C%7C8%3A5%3A2020%3A15%3A15%7C%7CN%7C%7CN%7C%7Cnull%7C%7C1316%7C%7Cnull%7C%7Cnull%7C%7CN%7C%7Cnull%7C%7Cnull%7C%7C70jywc2; akavpau_maintenance_vp=1588976584~id=b85b8ceaf352a7c4b3b7a5fac900bdd3; bm_sv=B02284772BEBC9BFBDB73CD4ED6CFE84~nscqg8OhWqoGmXh2lujXGz5yvhefPtRzK5Uw/QMdDru0OiBwTrdhc0MCjT/4k/YmZNDDEnwSGm+S1eigiIDVioZGBStV0YuZ3QlwFobWJ4f2KlEiAGwrcF47J0by5mDpLQjA79Fm68a30sQKuGB+cw==; RT="r=https%3A%2F%2Fwww.dell.com%2Fsupport%2Fhome%2Fen-ca%2Fproduct-support%2Fservicetag%2F0-YW5odU91RHJWMDFjZDZ3WTRpWGNvQT090%2Foverview&ul=1588976283658&hd=1588976284605'}

r = requests.Request('GET', url, headers=headers)
#page = requests.get(url) #create an object first - something like req
prepared = r.prepare()
#soup = BeautifulSoup(r.content, 'html.parser')
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
#results = soup.find(id='warrantyExpiringLabel')

pretty_print_POST(prepared)

s = Session()

resp = s.send(prepared)

soup = BeautifulSoup(resp.content, 'html.parser')
#results = soup.find(id='warrantyExpiringLabel')
#keyword = 'warrantyQparam'
results = soup.find_all('script',type='text/javascript')

# print(results.script.keyword)
# p = re.compile('var table_body = (.*?);')
# fields = dict(re.findall(p, results.text))
# print fields['warrantyQparam']

# data={'warrantyEncryptedParams':'eyJTZXJ2aWNlVGFnIjoiNzBKWVdDMiIsIkNvbXBhbnlOdW1iZXIiOiIwNCIsIkxvY2FsQ2hhbm5lbCI6IjA0IiwiTG9iIjoiUG93ZXJDb25uZWN0IiwiUHJvZHVjdENvZGUiOiJuZXR3b3JraW5nLW4zMDAwLXNlcmllcyIsIkJ1aWQiOiIxMSIsIlNlZ21lbnQiOiJCU0QiLCJGYW1pbHlOYW1lIjoibmV0d29ya2luZ19zd2l0Y2hlc19zZXJpZXMiLCJDdXN0b21lck51bWJlciI6IjE0Njk0ODkzMiIsIlByb2R1Y3RMT0IiOiI0Rk8iLCJBcHBOYW1lIjoibXNlIn01'}
#
# url2='https://www.dell.com/support/components/dashboard/en-ca/Warranty/GetInlineWarranty'
#
# q = requests.Request('GET', url2, headers=data)
# prepared = q.prepare()
# def pretty_print_POST(req):
#     """
#     At this point it is completely built and ready
#     to be fired; it is "prepared".
#
#     However pay attention at the formatting used in
#     this function because it is programmed to be pretty
#     printed and may differ from the actual request.
#     """
#     print('{}\n{}\r\n{}\r\n\r\n{}'.format(
#         '-----------START-----------',
#         req.method + ' ' + req.url,
#         '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
#         req.body,
#     ))

# pretty_print_POST(prepared)


"""
url2='https://www.dell.com/support/components/dashboard/en-ca/Warranty/GetInlineWarranty'

#eyJTZXJ2aWNlVGFnIjoiNzBKWVdDMiIsIkNvbXBhbnlOdW1iZXIiOiIwNCIsIkxvY2FsQ2hhbm5lbCI6IjA0IiwiTG9iIjoiUG93ZXJDb25uZWN0IiwiUHJvZHVjdENvZGUiOiJuZXR3b3JraW5nLW4zMDAwLXNlcmllcyIsIkJ1aWQiOiIxMSIsIlNlZ21lbnQiOiJCU0QiLCJGYW1pbHlOYW1lIjoibmV0d29ya2luZ19zd2l0Y2hlc19zZXJpZXMiLCJDdXN0b21lck51bWJlciI6IjE0Njk0ODkzMiIsIlByb2R1Y3RMT0IiOiI0Rk8iLCJBcHBOYW1lIjoibXNlIn01

<script type="text/javascript">
"""


# create a dictionary for cookie (https://stackoverflow.com/questions/7164679/how-to-send-cookies-in-a-post-request-with-the-python-requests-library)
