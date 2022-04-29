cipher = 'omkf pi hdn cmgef icphsck .H krg vphqkc c, fic mco kqgf ioqag eo qfcmckf oq ficpihdn cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg mfio kdck kha cokh kodjuck vn k fofvfo gqpojicmoqli opiyoa of kihsc nccqki oefc ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya flofigvffic xvgfck. Fio kokfice'
cipher = cipher.lower()


for i in range(1,26):
    plaintext = ''
    for j in cipher:
        if ord(j) in range(97,123):
            plaintext+= chr(ord(j)+i) if ord(j)+i<123 else chr(ord(j)+i-26)
        else:
            plaintext+=j

    print('Plaintext with key',i,':\n',plaintext,end='\n\n\n')
