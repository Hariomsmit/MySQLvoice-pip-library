def query(voicenote):
    global mycursor, tablename # OUR MADE KEYWORDS

    #To see all table details
    if (voicenote.find("show") != -1) and (voicenote.find("all") != -1) and (voicenote.find("details") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    #To see all table details spoken in hindi(regional language)
    elif (voicenote.find("Mujhe") != -1) and (voicenote.find("sari") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM " + " " + tablename
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    #To see all details ordered by Name alphabetically
    elif (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by name") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename + " " + "ORDER BY Name "
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see all details ordered by Salary in ascending order
    elif (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by salary") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename + " " + "ORDER BY Salary "
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see first row of the table
    elif (voicenote.find("show") != -1) and (voicenote.find("First") != -1) and (voicenote.find("detail") != -1) or (voicenote.find("row") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename + " " + "ORDER BY Name LIMIT 1 "
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see first two rows of the table
    elif (voicenote.find("show") != -1) and (voicenote.find("first two") != -1) and (voicenote.find("details") != -1) or (voicenote.find("rows") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename + " " + "ORDER BY Name LIMIT 2"
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see first three rows of the table
    elif (voicenote.find("show") != -1) and (voicenote.find("first three") != -1) and (voicenote.find("details") != -1) or (voicenote.find("rows") != -1):
        from main import tablename, mycursor
        cmd = "SELECT * FROM" + " " + tablename + " " + "ORDER BY Name LIMIT 3 "
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see only Names
    elif (voicenote.find("show only") != -1) and (voicenote.find("names") != -1):
        from main import tablename, mycursor
        cmd = "SELECT Name FROM" + " " + tablename
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    elif (voicenote.find("show ") != -1) and (voicenote.find("all names") != -1):
        from main import tablename, mycursor
        cmd = "SELECT Name FROM" + " " + tablename
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    # To see only Names and Salaries
    elif (voicenote.find("show only name and salaries") != -1) or (voicenote.find("show only salaries") != -1): # OR operator accepts any of the operands
        from main import tablename, mycursor
        cmd = "SELECT Name , Salary FROM" + " " + tablename
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
