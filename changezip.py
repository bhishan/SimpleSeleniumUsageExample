from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Chrome()
browser.get('http://www.lowes.com/store/')
time.sleep(7)

def click_each_store(li_elem):
    shop_this_store = li_elem.find_element_by_tag_name('button')
    shop_this_store.click()
    time.sleep(15)
    

def search_stores_with_zip(each_zip):
    print len(each_zip)

    print each_zip
    
    if len(each_zip) != 5:
        each_zip = "0" + each_zip
    search_element = browser.find_element_by_id("search-box")

    find_form = browser.find_element_by_id("storeSearch")
    all_form_inputs = find_form.find_elements_by_tag_name('input')
    find_button = all_form_inputs[-1]
    
    search_element.send_keys(each_zip)
    time.sleep(3)
    find_button.click()
    time.sleep(20)
    required_ul = browser.find_element_by_id("storeList")
    all_li_elem = required_ul.find_elements_by_tag_name("li")
    click_each_store(all_li_elem[0])
    for i in range(len(all_li_elem)):
        required_ul = browser.find_element_by_id("storeList")
        all_li_elem = required_ul.find_elements_by_tag_name("li") 
        click_each_store(all_li_elem[1])
        

def main():
    with open('ZipCodes.txt', 'rb') as f:
        for each_zip in f:
            each_zip = each_zip.rstrip()
            try:
                search_stores_with_zip(each_zip)
            except:
                print "Failed for zip ", each_zip



if __name__ == '__main__':
    main()
