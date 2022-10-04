import convertapi
convertapi.api_secret = 'your-convertapi-key'

result = convertapi.convert('pdf', {'File': 'book.epub'})

result.file.save('resbook.pdf')
