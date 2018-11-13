'''
 create ilcsoft authorlist from text file, created with 
 ilcsoft_authorlist.py, i.e. calling 
    git shortlog -e -s -n 
 for each package

  NB: I have manually replaced special characters (Lukic, Ete)
  as I could not get python to treat these correctly ...

 replaces known duplicate entries for authors based on the 
 dictionary 'dsar'

 the final list will be given in descending order of number of commits 
 
Example:

 python ./ilcsoft_authorlist.py | sort -k 2 > author_list_sorted.txt
 python remove_duplicate_authors.py author_list_sorted.txt author_list_unique.txt
 

'''

###############################################

write_total_commit = False

###############################################


# dictionary with strings to replace

dsar = {}
dsar['tomohiko'] = 'Tomohiko Tanabe'
dsar['TANABE Tomohiko'] = 'Tomohiko Tanabe'
dsar['thomson'] = 'Mark Thomson'
dsar['suehara'] = 'Taikan Suehara'
dsar['SUEHARA Taikan'] = 'Taikan Suehara'
dsar['speckmay'] = 'Peter Speckmayer'
dsar['simoniel'] = 'Rosa Simoniello'
dsar['peterkostka'] = 'Peter Kostka'
dsar['pawlikb'] = 'Bogdan Pawlik'
dsar['bogdan'] = 'Bogdan Pawlik'
dsar['marshall'] = 'John Marshall'
dsar['luisaleperez'] = 'Luis Alejandro Perez Perez'
dsar['libo929'] = 'Bo Li'
dsar['Bo LI'] = 'Bo Li'
dsar['Li Bo'] = 'Bo Li'
dsar['huonglantran'] = 'Huong Lan Tran'
dsar['gaede']= 'Frank Gaede'
dsar['engels'] = 'Jan Engels'
dsar['bogdanmishchenko'] = 'Bogdan Mishenko'
dsar['andresailer'] = 'Andre Sailer'
dsar['YancyW'] = 'Yan Wan'
dsar['TiborILD'] = 'Tibor Kurca'
dsar['StrahinjaLukic'] = 'Strahinja Lukic'
dsar['Matthias'] = 'Matthias Weber'
dsar['MarkusFrankATcernch'] = 'Markus Frank'
dsar['Guillaume'] = 'Guillaume Garillot'
dsar['Dan.Y'] ='Dan Yu'
dsar['A.Yamaguchi'] = 'A Yamaguchi'
dsar['KURATA Masakazu'] = 'Masakazu Kurata'
dsar['Ete Remi'] = 'Remi Ete'
dsar[' Multi-algorithm pattern recognition'] = 'John Marshall'
dsar['Carl Mikael Berggren'] =  'Mikael Berggren'
dsar['Yorgos Voutsinas'] = 'Georgios Voutsinas'

# dict for counting and removing duplicates
d = {}



#-----------------------------------


def sar(inf,outf,dict):
    """  put lines with duplicate names into dictionary """

    for line in inf:
        
        if 'No Author' in line:
            continue
        if 'Multi-algorithm' in line:
            continue

        for ksar in dsar.keys():
            line = line.replace( ksar , dsar[ksar] )

        cols = line.split()
        count = int(cols[0])


        key = ''
        if cols[2][0] == '<':
            key = cols[1]
        elif cols[3][0] == '<':
            key = cols[1] + ' ' + cols[2]
        elif cols[4][0] == '<':
            key = cols[1] + ' ' + cols[2]  + ' ' + cols[3] 
        elif cols[5][0] == '<':
            key = cols[1] + ' ' + cols[2]  + ' ' + cols[3]  + ' ' + cols[4] 
        else:
            print "error with key in line: " , line
        print ' key : ' , key
            
        if key in d:
            d[ key ] = d[ key ] + count
        else:
            d[ key ] = count

            

        
if __name__ == '__main__':
    import sys
    
    print sys.argv

    inf = open( sys.argv[1] , 'r' )
    outf = open( sys.argv[2] , 'w' )
    
    sar( inf , outf , d ) 
    

    # ---- sort dict wrt count
    l = []
    for k in d.keys():
        
        l.append( ( d[k] , k ) )

    l.sort(reverse=True)


    for a in l:

        if write_total_commit:
            line = ' ' + a[1] + ' ' + str(a[0]) + '\n'
        else:
            line = ' ' + a[1] + ', '

        outf.write(line)
    

    inf.close()
    outf.close()
