import subprocess
import sys
folder = "."
if( len(sys.argv)>1):
    folder=sys.argv[1]
proc = subprocess.Popen(["tree", folder], stdout=subprocess.PIPE)
tree = proc.stdout.read().decode("utf-8")
tree=tree.split("\n")
tree=tree[1:len(tree)-3]
tree='\n'.join(tree)
files_name= tree.replace("├","").replace("─","").replace("│","").replace("└","").replace(u'\xa0', u' ').replace(" ","").split("\n")
for file in files_name:
    proc = subprocess.Popen(["find", folder, "-name", file], stdout=subprocess.PIPE)
    file_path=proc.stdout.read().decode("utf-8").replace("\n","")
    tree=tree.replace(file,"<a href=\""+file_path+"\">"+ file +"</a>")
tree="<pre>\n"+tree+"\n</pre>"
f = open("index.md", "w")
f.write(tree)
f.close()