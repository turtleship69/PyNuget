import base64
import os
import sys

mimetypes = {
    'aac':'audio/aac',
    'abw':'application/x-abiword',
    'arc':'application/x-freearc',
    'avi':'video/x-msvideo',
    'azw':'application/vnd.amazon.ebook',
    'bin':'application/octet-stream',
    'bmp':'image/bmp',
    'bz':'application/x-bzip',
    'bz2':'application/x-bzip2',
    'csh':'application/x-csh',
    'css':'text/css',
    'csv':'text/csv',
    'doc':'application/msword',
    'docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'eot':'application/vnd.ms-fontobject',
    'epub':'application/epub+zip',
    'gz':'application/gzip',
    'gif':'image/gif',
    'htm':'text/html',
    'html':'text/html',
    'ico':'image/vnd.microsoft.icon',
    'img':'application/img',
    'iso':'application/iso',
    'ics':'text/calendar',
    'jar':'application/java-archive',
    'jpeg':'image/jpeg',
    'jpg':'image/jpeg',
    'js':'text/javascript',
    'json':'application/json',
    'jsonld':'application/ld+json',
    'mid':'audio/midi audio/x-midi',
    'midi':'audio/midi audio/x-midi',
    'mjs':'text/javascript',
    'mp3':'audio/mpeg',
    'mpeg':'video/mpeg',
    'mpkg':'application/vnd.apple.installer+xml',
    'odp':'application/vnd.oasis.opendocument.presentation',
    'ods':'application/vnd.oasis.opendocument.spreadsheet',
    'odt':'application/vnd.oasis.opendocument.text',
    'oga':'audio/ogg',
    'ogv':'video/ogg',
    'ogx':'application/ogg',
    'opus':'audio/opus',
    'otf':'font/otf',
    'png':'image/png',
    'pdf':'application/pdf',
    'php':'application/x-httpd-php',
    'ppt':'application/vnd.ms-powerpoint',
    'pptx':'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'rar':'application/vnd.rar',
    'rtf':'application/rtf',
    'sh':'application/x-sh',
    'svg':'image/svg+xml',
    'swf':'application/x-shockwave-flash',
    'tar':'application/x-tar',
    'tif':'image/tiff',
    'tiff':'image/tiff',
    'ts':'video/mp2t',
    'ttf':'font/ttf',
    'txt':'text/plain',
    'vsd':'application/vnd.visio',
    'wav':'audio/wav',
    'weba':'audio/webm',
    'webm':'video/webm',
    'webp':'image/webp',
    'woff':'font/woff',
    'woff2':'font/woff2',
    'xhtml':'application/xhtml+xml',
    'xls':'application/vnd.ms-excel',
    'xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'xml':'application/xml',
    'xul':'application/vnd.mozilla.xul+xml',
    'zip':'application/zip',
    '3gp':'video/3gpp',
    '3g2':'video/3gpp2',
    '7z':'application/x-7z-compressed'
}

def createNugget(file, nugget, compress=True):

    if compress:
        list = "7z a -mx=9 YouCanDeleteThisArchiveIfItShowsUpInYourFileManagerItsFromPyNuget.7z " + file
        os.popen(str(list), "w")
        
    with open("YouCanDeleteThisArchiveIfItShowsUpInYourFileManagerItsFromPyNuget.7z", 'rb') as f:
        data = f.read()
    
    data = base64.b64encode(data)
    data = str(data)[2:-1]

    with open(nugget, 'w') as f:
        f.write("data:"+mimetypes[file.split('.')[1]]+';base64,'+data)
    print("done")
def readNugget(nugget, file, compress=True):
    with open(nugget, 'r') as f:
        raw = f.read()
    
    extension, data = raw.split(';base64,')
    extension = extension.split('/')[-1]

    data = base64.b64decode(data)
    
    
    with open("YouCanDeleteThisArchiveIfItShowsUpInYourFileManagerItsFromPyNuget.7z", 'wb') as f:
        f.write(data)

    if compress:
        list = "7z e YouCanDeleteThisArchiveIfItShowsUpInYourFileManagerItsFromPyNuget.7z"
        os.popen(str(list), "w")

if sys.argv[1] == "-c":
    createNugget(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "-r":
    readNugget(sys.argv[2], sys.argv[3])
else:
    print ("Suffer from the wrath of my lazyness!")
