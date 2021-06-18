print("""
    ███        ▄█    █▄    ████████▄
▀█████████▄   ███    ███   ███   ▀███
   ▀███▀▀██   ███    ███   ███    ███
    ███   ▀  ▄███▄▄▄▄███▄▄ ███    ███
    ███     ▀▀███▀▀▀▀███▀  ███    ███
    ███ vv1ck ███    ███   ███    ███
    ███ JOKER ███    ███   ███   ▄███
   ▄████▀     ███    █▀    ████████▀ 
   
   1- Modify headers and data
   2- tool industry
""")
def Add_HEDR_ADT():
  FIL = open(input('[+] Enter the name of the Headers file '),'r')
  FIL2 = open(input('[+] Enter the name of the Data file '),'r')
  
  for DN in FIL:
    try:
      D2 = DN.split()[1]
      DN = DN.split(':')[0]
      H1 = f"'{DN}':"
      H2 = f"'{D2}',"
      print(H1+H2)
      with open('NEW-headers.txt', 'a') as x:
        x.write(H1+H2 + '\n')
    except IndexError:
      pass
  for D2 in FIL2:
    try:
      D3 = D2.split()[1]
      D4 = D2.split(':')[0]
      H3 = f"'{D4}':"
      H4 = f"'{D3}',"
      print(H3+H4)
      with open('NEW-data.txt', 'a') as x:
        x.write(H3+H4 + '\n')
    except IndexError:
      print('\n\n[+] Successfully completed, you can find them in the NEW-headers.txt and NEW-data.txt file')
      exit()
def NEW_TOOLS():
  UL = input('Enter url : ')
  HD = input('\n\nEnter headers : ')
  DT = input('\n\nEnter Data : ')
  TOL="""
  import requests
  
  url = '"""+UL+"""'
  headers = {"""+HD+"""}
  data = {"""+DT+"""}
  
  GO = requests.post(url,headers=headers,data=data)
  
  print(GO.text)
  print(GO)"""
  print(TOL)
  with open('NEW-TOOLS.py', 'a') as x:
    x.write(TOL + '\n')
    
  print('\n\n[+] Successfully completed, you can find them in the NEW-TOOLS.py file')
def returnn():
  vv1ck = input('[+] Enter the number : ')
  if vv1ck=='1':
    Add_HEDR_ADT()
  elif vv1ck=='2':
    NEW_TOOLS()
  else: 
    print('The number is incorrect, try again')
    return returnn()
returnn()
