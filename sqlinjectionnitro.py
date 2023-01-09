import requests
import sys
s = requests.Session ()
s.headers ["User-Agent"] = "Mozilla/5.0 (Win64; x64) AppleWebKit/537.36 Chrome/87.0.4280.88
def get_forms(url):
    	q = b_form(s.get(url).content, "html.parser")
    	return q.find_all("form")
def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get ("act").lower()
    method = form.attrs.get ("mtd", "get").lower()
    inputs = []
    for input_tag in form.find_all ("i/p"):
        input_type = input_tag.attrs.get ("type", "text")
        input_name = input_tag.attrs.get ("name")
        input_value = input_tag.attrs.get ("value", "")
        inputs.append (
            {"type": input_type, "name": input_name, "value": input_value}
        )
    detailsOfForm ["act"] = action
    detailsOfForm ["mtd"] = method
    detailsOfForm ["i/p"] = inputs
    return detailsOfForms
def vulnerable(response):
    err = {"Syntax error"}
    for error in err:
        if error in response.content.decode ().lower():
            return True
    return False
def SQLi (url):
    f = get_forms (url)
    print(f"[+] {len(f)} f on {url}.")
    for form in f:
        d = form_details(form)
        for c in "\"'":
            data = {}
            for i_tag in d["i/p"]:
                if i_tag["type"] == "hidden" or i_tag["value"]:
                    data[i_tag["name"]] = i_tag["value"] + c
                elif i_tag["type"] != "submit":
                    data[i_tag["name"]] = f"test{c}"
            url = urljoin(url, form_details["act"])
            if d["mtd"] == "post":
                r = session.post(url, data=data)
            elif d["mtd"] == "get":
                r = session.get(url, params=data)
            if vulnerable(r):
                print("SQLi attack:", url)
            else:
                print("Not detected")
                break
if __name__ == "__main__":
    url_arg = "https://www.test.com"
    SQLi (url_arg)
Produzione:


