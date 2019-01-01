#!/usr/bin/env python
# coding: utf-8

# In[2]:

https://www.youtube.com/watch?v=7I2s81TsCnc
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def main():

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    
    values = [
        [
            1,2,3,4
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    spreadsheet_id = '1X5cJEFRzsNUKMi838I91NJ6YY9ir9Ui97Bwq4AopSJo'
    range_name = 'Sheet1!A1'
    value_input_option = 'USER_ENTERED'
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
   

if __name__ == '__main__':
    main()




