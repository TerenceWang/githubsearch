import pycurl
import os
import time
import json
import Queue
import base64
from git import Repo
class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self, buf):
        self.contents = self.contents + buf
    def clear(self):
    	self.contents = ''

def getrepos(keyword, page):
	t = Test()
	start_time = time.time()
	c = pycurl.Curl()
	userpass = b""  # You need to add you name and password here for example b"tao:lalala"
		# username = 'terencewang'
	url = 'https://api.github.com/search/repositories?q='+keyword+'+language:java&sort=stars&order=desc&page='+str(page)
	c.setopt(c.URL, url)
	userAndPass = base64.b64encode(userpass)
	c.setopt(pycurl.HTTPHEADER, ['Authorization: Basic %s' % userAndPass,
	                                'Content-Type: application/json'])
	c.setopt(c.WRITEFUNCTION, t.body_callback)
	c.perform()
	end_time = time.time()
	c.close()
	return t.contents
# def getrepos(userlist):
# 	for user in userlist:

# userlist = set([u'gugakatsi', u'TerenceWang', u'sspreitzer', u'aliacarmen', u'naqvir', u'nevan1364257', u'ahmetabdi', u'srayner', u'inkpei', u'MichalPaszkiewicz', u'emojiijome', u'mmeyer2k', u'ahmyi', u'j-lustig', u'AeronStory', u'874516119', u'facelessman', u'cjld', u'stoked-zz', u'mmorenog', u'sblaplace', u'JsWatt', u'liamjmc', u'88250', u'andresgaragiola', u'shayanelhami', u'JiangInk', u'brunocasanova', u'tvvocold', u'ternsip', u'DaStrike', u'zombieleet', u'vxst', u'mishin', u'ganeshyuvi', 'terencewang', u'drahmel', u'JoaquinGonzalez', u'jhliberty', u'yuriak', u'adityaanupindi', u'AbubakerB', u'wozgeass', u'pisual', u'happyqq', u'yeahdongcn', u'bassbone', u'AbelS95', u'gbywt', u'caizheng1993', u'macressler', u'mzeeqazi', u'matiasinsaurralde', u'beckyzorz', u'YannisBacha', u'JonatanSalas', u'alexm98', u'angusshire', u'g-pechorin', u'HittaX', u'YAIBA2', u'jonahengler', u'PeytonsProfile', u'likeyiyy', u'llluiop', u'heuristicus', u'Nidhintsajee', u'evinw', u'yuraima', u'palerdot', u'riyasmohamedmr', u'ashref-hejazi', u'zackhaikal', u'AdamMurray', u'Denzeen', u'nblintao', u'qinix', u'Adam-K-P', u'christosc', u'tangqingxin', u'basicv8vc', u'ZTGravity', u'kfalconspb', u'smalladam', u'amitkalsi', u'mgwhitfield', u'YXJKTH', u'oetcxiaoliu', u'beali', u'ismdeep', u'BillTheBest', u'Qualia-Li', u'GrapeBaBa', u'zhangwengame', u'huangjunque', u'freire45', u'VagrantStory', u'tiandavis', u'samundrak', u'quietcoolwu', u'DaniAkash', u'zebbra2014', u'ReidHolmes', u'brianmillar', u'BahaminBB', u'csjaba', u'BroiSatse', u'shanmukh11', u'xieguigang', u'CraigyHK', u'stpettersens', u'YacratesWyh', u'pjmagee', u'cusspvz', u'arthurkiller', u'WallysonNunes', u'hehead', u'BespokeStan', u'aaronjden', u'gagikh', u'Linux-Player', u'sequoiar', u'dohliam', u'MegaColorBoy', u'gintern', u'dcarles', u'nandomegaman'])
# savefile(userlist)
# userlist = readfile("username.txt")
repos = []


def parserepos_json(keyword, page):
	json_str = getrepos(keyword,page)
	data = json.loads(json_str)
	count = data['total_count']
	for item in data['items']:
		user = item['owner']['login']
		name = item['name']
		git_url = item['git_url']
		clone_url = item['clone_url']
		svn_url = item['svn_url']
		repos.append({"user":user,"name":name,"git_url":git_url,"clone_url":clone_url,"svn_url":svn_url})
	filename = "py_repos_"+keyword+"_"+str(page)+".txt"
	f = open(filename,'w')
	f.write(json.dumps(repos))
	f.close()
	return repos

def cleanrepo(path):
	list_dirs = os.walk(path)
	command = 'find ./data/java/data -name ".git" | xargs rm -Rf'
	os.system(command)
	for root, dirs, files in list_dirs:
		for f in files:
			ff = u' '.join(f).encode('utf-8').strip()
			jj = u' '.join(".py").encode('utf-8').strip()
			if not str(ff).endswith(str(jj)):
				try:
					os.remove(os.path.join(root, f))
				except OSError:
					continue

	list_dirs = os.walk(path)
	for root, dirs, files in list_dirs:
		for dir in dirs:
			if len(os.listdir(os.path.join(root, dir)))==0:
				try:
					os.rmdir(os.path.join(root, dir))
				except OSError:
					continue



# for i in range(20):
# 	parserepos_json(getrepos('leetcode',i))
# f = open('repos.txt','r')
# s = f.readline()
# repos = json.loads(s)

parserepos_json('leetcode',2)

print 'reading repos done'
for i in range(30):
	name = repos[i]['name']
	user = repos[i]['user']
	path = './data/java/data/'+user+'/'+name
	isExists = os.path.exists(path)
	if not isExists:
		os.makedirs(path)
		print "Downloading repo "+name+"..."
		git_address = repos[i]['git_url']
		Repo.clone_from(git_address, path)
		print "Download repo "+name+" Done"
	# else:
	# 	continue
	print "Cleaning repo "+name+"..."
	cleanrepo(path)
	print "Cleaning repo "+name+" Done"


