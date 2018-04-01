import tkinter as Tkinter
import tkinter.font as tkFont
from PIL import ImageTk,Image
from sys import exit
import subprocess
import pydot
import graphviz
import os

curr_dir = os.getcwd()
graphvizdir = curr_dir+'\\graphviz-2.38\\release\\bin'
os.environ["PATH"] += os.pathsep + graphvizdir


def my_output():
	f = open("RE.txt", "r")
	arr = f.readline().split()#Inputting tokenized RE
	heading = arr[0]
	heading = heading[:-1]
	tree = pydot.Dot(graph_type='graph', label="Syntax Tree for "+heading, labelloc='top', labeljust='left', fontsize='24', labelfontcolor="#1346c6")
	tree.set_node_defaults(shape='record')
	f.close()
	f = open("followpos.txt", "r")
	arr = list(map(int, f.readline().split()))
	followpos_c = arr[0]
	followpos = []
	for i in range(followpos_c):
		arr = f.readline().split()
		if (len(arr)==0):
		    temp=''
		else:
		    temp = arr[0]
		    temp = temp[:-1]
		followpos.append(temp)
	f.close()
	f = open("stree.txt", "r")
	x = 0
	#print(followpos)
	arr = f.readline().split()
	nodeaddr = arr[0]
	while (nodeaddr != '$&$'):
		arr = f.readline().split()#Inputting symbol
		symbol = arr[0]
		arr = f.readline().split()#Inputting nullable
		nullable = int(arr[0])
		arr = f.readline().split()#Inputting firstpos
		if (len(arr)==0):
		    fpos=''
		else:
		    fpos = arr[0]
		    fpos = fpos[:-1]
		arr = f.readline().split()#Inputting lastpos
		if (len(arr)==0):
		    lpos=''
		else:
		    lpos = arr[0]
		    lpos = lpos[:-1]
		
		arr = f.readline().split()#Inputting child address
		lchild = arr[0]
		rchild = arr[1]
		
		#Printing node data
		output = symbol
		#print(output)
		if(output=='|'):
		   node_content = '{'+'&#124;'+'|'
		else:
		    node_content = '{'+output+'|'
		if (nullable==0):
			output = 'Nullable : No'
		else:
			output = 'Nullable : Yes'
		#print(output)
		node_content = node_content + output + '\n'
		output = 'Firstpos : (' + fpos + ')'
		#print(output)
		node_content = node_content + output + '\n'
		output = 'Lastpos : (' + lpos + ')'
		#print(output)
		node_content = node_content + output
		if (lchild=='0' and rchild=='0'):
		    output = 'Followpos : (' + str(followpos[x]) + ')'
		    x = x+1
		    #print(output)
		    node_content = node_content + '\n' + output
		#print('\n')
		node_content = node_content + '}'
		#print(node_content)
		#Creating pydot node
		node1=pydot.Node(nodeaddr, label=node_content, color="#0e7702")
		tree.add_node(node1)
		if(lchild!='0'):
		    tree.add_edge(pydot.Edge(nodeaddr,lchild))
		if(rchild!='0'):
		    tree.add_edge(pydot.Edge(nodeaddr,rchild))
		
		arr = f.readline().split()
		nodeaddr = arr[0]
	tree.write_svg('Stree.svg')
	f.close()
	#Creating DFA********************************************************************
	f = open("dfa.txt", "r")
	#Reading Tranisition Table from File
	arr = list(map(int, f.readline().split()))
	row_c = arr[0]
	column_c = arr[1]
	fstate_c = arr[2]
	states = f.readline().split()
	symbols = f.readline().split()
	fstates = f.readline().split()
	transition_table=[]
	for i in range(row_c):
		temp = f.readline().split()
		transition_table.append(temp)
		
	#Printing File Data  
	'''print(row_c)
	print(column_c)
	print(fstate_c)
	print(states)
	print(symbols)
	print(fstates)
	print(transition_table)'''

	f.close()

	#Drawing Graph
	graph = pydot.Dot(graph_type='digraph', rankdir='LR', label="DFA for "+heading, labelloc='top', labeljust='left', fontsize='12', labelfontcolor="#c61254")
	node_list = []
	strt_node=pydot.Node("s", fillcolor="white", shape="circle", style="invis")
	graph.add_node(strt_node)
	for i in range(row_c):
		if(states[i] in fstates):
		    node_temp = pydot.Node(states[i], style="filled", fillcolor="white", shape="doublecircle", color="red")
		else:
		    node_temp = pydot.Node(states[i], style="filled", fillcolor="white", shape="circle")
		node_list.append(node_temp)
		graph.add_node(node_list[i])

	#Adding start node
	graph.add_edge(pydot.Edge(strt_node,node_list[0], label="", color="black"))

	for i in range(row_c):
		for j in range(column_c):
		    if(transition_table[i][j] != '_'):
		        #k=int(transition_table[i][j])-1
		        k=states.index(transition_table[i][j])
		        graph.add_edge(pydot.Edge(node_list[i],node_list[k], label=symbols[j], labelfontcolor="#109933", fontsize="10",color="black"))
	graph.write_svg('DFA.svg')
	os.system("start /B Stree.svg && DFA.svg")
	os.system("DFA.svg")
#***************************************************************************************************************
top = Tkinter.Tk()
top.title("RE to DFA Coverter")
top.geometry("490x100")
top.resizable(False, False)
top.iconbitmap("icon.ico")
image2 =Image.open('l.jpg')
image1 = ImageTk.PhotoImage(image2)
background_label = Tkinter.Label(top, image=image1)
background_label.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")
#background_label.pack()
helv10 = tkFont.Font(family="Arial",size=10,weight="bold")
helv12 = tkFont.Font(family="Arial",size=14)

L1 = Tkinter.Label(top, text="Regular Expression:",fg="BLACK",bg="WHITE")
#L1.pack(side="left",fill="x",padx=20, pady=50,anchor="center",expand=True)
L1.grid(row=1, column=0,sticky=(Tkinter.E), padx=5, pady=5)
#L1.place(x=0, y=0, relx=0.1, rely=0.5, anchor="center")

L1.grid_rowconfigure(1,pad=100)
L1.grid_columnconfigure(0,pad=100)

entryText = Tkinter.StringVar()
E1 = Tkinter.Entry(top,bd=0,relief="flat",font=helv12)
entryText.set( "Status Ready.." )
#E1.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")
#E1.pack(side="left",fill="x", ipady=5, padx=20, anchor="center",expand=True)
E1.grid(row=1, column=1, padx=20, pady=20)
E1.focus_set()
E1.grid_columnconfigure(1,pad=200)

L2 = Tkinter.Label(top, textvariable=entryText, fg="BLACK",bg="WHITE")
L2.grid(row=2, column=2,sticky=(Tkinter.W), padx=5, pady=5)
L2.grid_columnconfigure(2,pad=200)
def callback():
	#print E1.get()
	entryText.set( "Processing.." )
	top.update()
	s=E1.get()
	#subprocess.call(["gcc", "hello_world.cpp"])
	tmp=subprocess.call(["re2dfa.exe",s])
	#print "printing result"
	#print tmp
	if(tmp!=1):
		entryText.set( "Error, Try Again.." )
		top.update()
	else:
		my_output()
		entryText.set( "Status Ready.." )
		top.update()
    
    
B4 = Tkinter.Button(top, text ="Generate DFA", anchor="center",relief="flat", bd=1,
                    command=callback,activebackground="#FFBA75",font=helv10)
#B4.pack(side="right",fill="x",padx=20, pady=10,anchor="center",expand=True)
B4.grid(row=1, column=2,sticky=(Tkinter.N, Tkinter.W, Tkinter.E, Tkinter.S), padx=5, pady=5)
#B4.place(x=0, y=0, relx=0.9, rely=0.5, anchor="center")
top.mainloop()
