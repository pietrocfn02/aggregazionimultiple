from django.db import connection
from .models import TimeReport

all_filters = ['Project', 'Employee', 'Date']
filter_to_field = {'Project' : 'ep.project_name', 'Employee' : 'ee.name', 'Date' : 'et.day'  }

def parse_filters(filters: str):
    
    if len(filters) < 2:
        return []
    if filters[0] == ',' :
        filters = filters[1:]
    splitted = filters.split(',')
    remaining = []
    for x in all_filters:
        remaining.append(x)
    print (remaining)
    for s in splitted:
        if s in remaining:
            remaining.remove(s)
    print (remaining)
    return splitted, remaining


def play_with_filters(filters):
    filters_copy = []
    #Creo una copia di filters
    for f in filters:
        filters_copy.append(f)
    stringone = ''
    for f in filters:
        if stringone == '':
            stringone+=filter_to_field[f]
        else:
            stringone+=", "+filter_to_field[f]

    with connection.cursor() as cursor:
        query = """
        select """+stringone+""", sum(et.number_of_hours) from employees_employee ee , employees_project ep , employees_timereport et 
        where ee.id = et.employee_id and ep.id = et.project_id 
        group by """+stringone+""";
        """
        print (query)
        cursor.execute(query)
        row = cursor.fetchall()
        print(row)
        filters_copy.append('Hours')
    
    return filters_copy, row



def update_tables(table,filter_array):
    if len(filter_array) == 0 :
        header = ['Project', 'Employee', 'Date', 'Hours']
        for t in TimeReport.objects.all():
            tmp_row = []
            tmp_row.append(t.project.project_name)
            tmp_row.append(t.employee.name)
            tmp_row.append(t.day)
            tmp_row.append(t.number_of_hours)
            table.append(tmp_row)
    else:
        result = play_with_filters(filter_array)
        header = result[0]
        table = result[1]

    return header, table


def update_filters(filters, filter_array, remaining):
    if filters != '':
        print("**************" + filters)
        result = parse_filters(filters)
        filter_array = result[0]
        remaining = result[1]
    else :
        filter_array = []
        remaining = all_filters

    return filter_array, remaining