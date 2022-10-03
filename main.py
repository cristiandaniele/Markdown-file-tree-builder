import subprocess
import sys

def replace_all(text, list):
    for word in list:
        text = text.replace(word, "")
    return text

def main():
    # setting defult folder
    folder = "." 

    #setting optional folder
    if(len(sys.argv)>1):
        folder=sys.argv[1]
    
    proc = subprocess.Popen(["tree", folder], stdout=subprocess.PIPE)
    tree = proc.stdout.read().decode("utf-8").split("\n")
    tree=tree[1:len(tree)-3]
    tree='\n'.join(tree)

    files_name= replace_all(tree,["├","─","│","└",u'\xa0'," "]).split("\n")
    files_name= files_name[1:len(files_name)-3]
    
    for file in files_name:
        proc = subprocess.Popen(["find", folder, "-name", file], stdout=subprocess.PIPE)
        file_path=proc.stdout.read().decode("utf-8").replace("\n","")
        tree=tree.replace(file,"<a href=\""+file_path+"\">"+ file +"</a>")
    tree="<pre>\n"+tree+"\n</pre>"
    tree= tree.replace(folder+"/","")
    f = open("index.md", "w")
    f.write(tree)
    f.close()

if __name__ == "__main__":
    main()