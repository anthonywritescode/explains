import markupsafe


name = 'anthony <script>alert(0)</script> writescode'

result = markupsafe.Markup(
    '''
        Welcome to my website, <strong>{name}</strong>,
    '''
).format(name=name)

print(result)
