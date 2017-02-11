import requests
from bs4 import BeautifulSoup


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

ny_url="http://www.nytimes.com"
ny_req=requests.get(ny_url)
ny_html=BeautifulSoup(ny_req.text,"html.parser")
ny_tags=ny_html.find_all(class_="story-heading",limit=10)

for tag in ny_tags:
	if tag.a:
		print(tag.a.text.replace("\n"," ").strip())
	else:
		print(tag.contents[0].strip())


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

md_url="http://www.michigandaily.com"
md_req=requests.get(md_url)
md_html=BeautifulSoup(md_req.text,"html.parser")
md_tags=md_html.find_all(class_="pane-mostread")

for tag in md_tags:
	if tag.ol:
		print(tag.ol.text.strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

cat_url="http://newmantaylor.com/gallery.html"
cat_req=requests.get(cat_url)
cat_html=BeautifulSoup(cat_req.text,"html.parser")
cat_tags=cat_html.find_all("img")

for tag in cat_tags:
	try:
		attr_dict=tag.attrs
		print(attr_dict["alt"])
	except:
		print("No alternative text provided!")



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

directory=["/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"]
email_list=[]
for page in directory:
	um_url="https://www.si.umich.edu"+page
	um_req=requests.get(um_url)
	um_html=BeautifulSoup(um_req.text,"html.parser")
	um_tags=um_html.find_all("a",string="Contact Details")

	um_links=[]
	for tag in um_tags:
		attr_dict=tag.attrs
		um_links.append(attr_dict["href"])

	for link in um_links:
		contact_url="https://www.si.umich.edu"+link
		contact_req=requests.get(contact_url)
		contact_html=BeautifulSoup(contact_req.text,"html.parser")
		contact_tags=contact_html.find_all(class_="field-name-field-person-email")
		for tag in contact_tags:
			if tag.a:
				tag_txt=tag.a.text.strip()
				str_tag=str(tag_txt)
				email_list.append(str_tag)
	try:
		nxt_tag_list=um_html.find_all(class_="pager-next")
		nxt_tag=nxt_tag_list[0].a
		nxt_attr=nxt_tag.attrs
		nxt_href=nxt_attr["href"]
		directory.append(nxt_href)
	except:
		break

count=1
for email in email_list:
	str_count=str(count)
	print(("{} {}").format(str_count,email))
	count+=1
















