import csv


def csv_to_array(name):
    ret = list()
    with open(name) as csv_file:
        line_count =0
        att_name =[]
        csv_reader =  csv.reader(csv_file,  delimiter=',')
        for row in csv_reader:
            if line_count ==0:
                for column in row :
                    if column == '\ufeffage' :
                        column = 'age'
                    att_name.append(column)
            else :
                d = dict()
                i =0
                for col in row:
                    d.update({att_name[i] : col })
                    i +=1
                a =[d['target']]
                del d['target']
                a.append(d)
                ret.append(a) 
            line_count +=1
    return ret

