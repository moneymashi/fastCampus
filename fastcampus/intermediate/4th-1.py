'''
Created on 2018. 9. 5.

@author: money
'''
from oauth2client.service_account import ServiceAccountCredentials

if __name__ == '__main__':
    pass

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 인증파트
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('./fastcampus.json', scope)
gs = gspread.authorize(credentials);

doc = gs.open_by_url('https://docs.google.com/spreadsheets/d/1dWSsrzRLcovgVxIZB0GK7I5BvmeImxXKAIze_Fyb48E/edit#gid=0');
ws = doc.get_worksheet(0);  # 첫번째 sheet.

# Read gspread
# val = ws.acell('B1').val; # 한칸위치값
# val = ws.row_values('1'); # row1줄값.
# val = ws.col_values('1'); # col1줄값.
# vals = ws.range('A2:B3');  # return list<Class>.
# for val in vals :
#     print(val.value);

# write
# ws.update_acell('B1', 'BB5');
ws.append_row(['AAA1','BBB1','CCC1']);




