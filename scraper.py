from bs4 import BeautifulSoup
import io


def get_list_titles_with_links(page, base = 'http://www.netflix.com'):
	list = {}

	def get_list_x_row(row_content, list):
		i = 0
		while True:
			box = row_content.find('div', class_ = 'slider-item slider-item-'+str(i))
			if box == None:
				break
			i += 1
			#print(box)
			url = box.find('a', role = 'link').get('href')
			title = box.find('a', role = 'link').get('aria-label')
			url = url[0:url.index('?',1)]
			list[title] = base + url

	page_parsed_html = BeautifulSoup(page, 'html.parser')
	if page_parsed_html != None:
		content_main = page_parsed_html.find('div', class_='galleryLockups')
		i = 0
		while True:
			content_row = content_main.find('div', id = 'row-'+str(i))
			if content_row == None:
				break
			i += 1
			get_list_x_row(content_row, list)
	return list



