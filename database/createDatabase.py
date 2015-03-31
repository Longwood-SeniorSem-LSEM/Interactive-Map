fin = open('canvas.txt', 'r')
fout = open('map.sql', 'w')
fout.write("DROP TABLE IF EXISTS locations;\n")
fout.write("CREATE TABLE locations (\n\tname\tTEXT,\n\tx\tINTEGER,\n\ty\tINTEGER,\n\ttype\tTEXT\n);\n")
for line in fin:
	data = line.split('|')
	fout.write("INSERT INTO locations (name,x,y) VALUES ('%s',%s,%s);\n" % (data[0],data[1],data[2]))
