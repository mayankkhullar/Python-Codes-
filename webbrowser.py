import webbrowser , time , shutil
t=time.strftime("%Y%m%d")
ol_file = 'words.txt'
new_file = 'words' + t + '.txt'
shutil.move(ol_file , new_file)


webbrowser.open('https://www.google.co.in/')



